import ast
from unittest import result

import numpy as np
import pandas as pd
from flask import Flask, request
from scipy.spatial.distance import euclidean
import nltk
from sklearn.feature_extraction.text import CountVectorizer

from preprocess import wnl, token_list, cv, lda

app = Flask(__name__)

df = pd.read_csv('kaggle_dataset/recipe_data.csv')
token_list = pd.read_csv('kaggle_dataset/token_list.csv')
token_list = set(token_list['0'])
nltk.download('wordnet')
wnl = nltk.WordNetLemmatizer()


@app.route("/", methods=["GET"])
def get_foods():  # put application's code here
    args = request.args
    recipe_id = args.get('recipe_id', type=int)
    sort_order = args.get('sort_order', type=int)
    return read_csw(recipe_id, sort_order)


if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=4000)


class SelectedFoods:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def read_csw(recipe_id, sort_order):
    recipe = pd.read_csv('kaggle_dataset/raw-data_recipe.csv')
    recipe_df = recipe.set_index('recipe_id')
    df_normalized = pd.read_csv('normalized_nutritions.csv', index_col=0)
    all_recipes_euclidean = pd.DataFrame(df_normalized.index)
    all_recipes_euclidean = all_recipes_euclidean[all_recipes_euclidean.recipe_id != recipe_id]
    all_recipes_euclidean["distance"] = all_recipes_euclidean["recipe_id"].apply(
        lambda x: euclidean(df_normalized.loc[recipe_id], df_normalized.loc[x]))
    top10_recommendation_euclidean = all_recipes_euclidean.sort_values(["distance"]).head(10).sort_values(
        by=['distance', 'recipe_id'])
    hybrid_top_n_recommendation = pd.concat([top10_recommendation_euclidean])
    aver_rate_list = []
    review_nums_list = []
    for recipeid in top10_recommendation_euclidean.recipe_id:
        aver_rate_list.append(recipe_df.at[recipeid, 'aver_rate'])
        review_nums_list.append(recipe_df.at[recipeid, 'review_nums'])
    hybrid_top_n_recommendation['aver_rate'] = aver_rate_list
    hybrid_top_n_recommendation['review_nums'] = review_nums_list
    if sort_order == 0:
        sort_order = "aver_rate"
    elif sort_order == 1:
        sort_order = "review_nums"
    try:
        top_n_recommendation = hybrid_top_n_recommendation.sort_values(by=[sort_order], ascending=False).head(15)
    except KeyError as e:
        print(e)
    recipeid_list = list(top_n_recommendation.recipe_id)
    sorted_names = recipe_df.loc[recipeid_list, ["recipe_name", "image_url"]]
    json_view = sorted_names.to_json(orient="split")
    return json_view


def deneme():
    cv = CountVectorizer(max_df=0.95, stop_words='english')
    cv_text = cv.fit_transform(df['tokens'])
    features = cv.get_feature_names()
    from sklearn.decomposition import LatentDirichletAllocation
    lda = LatentDirichletAllocation(n_components=100)
    lda.fit(cv_text)
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')


def query_process(sentence):
    arr = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(sentence.lower())]
    tag_predict = nltk.pos_tag(arr, tagset="universal")
    search_queue = []
    no_tag = set(['VERB', 'PRON', 'DET', '.', 'CONJ'])
    time_list = set(['h', 'm', 'hour', 'minute', 'min'])
    no_flag = False
    time_set = 1
    for element in tag_predict:
        if element[1] not in no_tag:
            if element[0] == 'no' or element[0] == 'not':
                no_flag = True
            elif element[1] == 'ADP':
                if element[0] == 'without':
                    no_flag = True
            elif element[1] == 'NUM':
                time_set = int(element[0])
            elif element[0] in time_list:
                if element[0] == 'h' or element[0] == 'hour':
                    search_queue.append(time_set * 60)
                else:
                    search_queue.append(time_set)
                continue
            else:
                if no_flag:
                    search_queue.append("!" + element[0])
                    no_flag = False
                else:
                    search_queue.append(element[0])
    return search_queue


def intents(word_list):
    # negative flag
    negative_word = []
    # nutrition
    nut_list = set(['sugars', 'fat', 'calories', 'sodium'])
    nut_word = []
    # time
    cook_time = []
    # 나머지
    search_word = []

    for word in word_list:
        if isinstance(word, int):
            cook_time.append(word)
        elif word[0] == "!":
            negative_word.append(word[1:])
        elif word in nut_list:
            nut_word.append(word)
        else:
            if word in token_list:
                search_word.append(word)

    # topic1
    cv_query = cv.transform([' '.join(search_word)])
    query_topic = np.argmax(lda.transform(cv_query))

    return negative_word, nut_word, cook_time, search_word, query_topic


@app.route("/hel", methods=["GET"])
def hello():
    args = request.args

    suggest = request.args.get('username')
    den = search_recipe(suggest)
    amac = den.to_json(orient="split")
    print(amac)

    return amac


# Pass the required route to the decorator

def search_recipe(query):
    word_list = query_process(query)
    negative_word, nut_word, cook_time, search_word, query_topic = intents(word_list)

    # Recipe_Name
    score_list = []
    for element in df['name']:
        res = ast.literal_eval(element)
        score = 0
        for word in search_word:
            if word in res:
                score += 1
        score_list.append(10 * score * score / len(res))
    df['score'] = score_list

    # Topic
    topic_list = set(df.nlargest(10, 'score')['topic'].values.tolist())
    topic_list.add(query_topic)
    df_filter = pd.DataFrame(df.loc[df['topic'].isin(topic_list), :])

    # Nut
    for word in nut_word:
        df_filter = pd.DataFrame(df_filter.loc[df_filter[word], :])

    # Scoring
    score_list = df_filter['score'].values.tolist()

    # time
    tot_time = 0
    for time in cook_time:
        tot_time += time

    for idx, element in enumerate(df_filter['time']):
        time_element = int(element)
        if time_element >= tot_time:
            score_list[idx] -= (time_element - tot_time) / 5

    # neg_filter + ingtool
    for idx, element in enumerate(df_filter['ing_tool']):
        ing_set = ast.literal_eval(element)
        score = 0
        for word in negative_word:
            if word in ing_set:
                score -= 4
        for word in search_word:
            if word in ing_set:
                score += 2
        score_list[idx] += score

    df_filter['score'] = score_list
    df_filter['score'] = df_filter.apply(
        lambda row: row['score'] + row['aver_rate'] * (1 + 0.2 * (min(row['review_nums'] / 100, 1))) / 5, axis=1)

    return df_filter.nlargest(10, 'score')[['recipe_name', 'ingredients', 'time', 'recipe', 'image_url']]
