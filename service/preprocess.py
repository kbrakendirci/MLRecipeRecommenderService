import pandas as pd
import numpy as np
import csv
import sklearn
import ast
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

read_csv = pd.read_csv('kaggle_dataset/raw-data_recipe.csv')
read_csv = read_csv.drop(columns=['reviews', 'recipe_id'])


def time_to_num(time_var):
    time_arr = re.split(' ', time_var)
    total_time = 0
    time_type = set(['m', 'h', 'd'])
    for element in time_arr:
        if element not in time_type:
            time = int(element)
        else:
            if element == 'd':
                total_time = 24 * 60 * time
            elif element == 'h':
                total_time = 60 * time
            else:
                total_time += time

    return total_time


def get_time(element):
    res = ast.literal_eval(element)
    arr = re.split('\n', res['directions'])
    if len(arr) > 5 and arr[4] == 'Ready In':
        time = time_to_num(arr[5])
        direction = ' '.join(arr[6:])
    elif len(arr) > 4 and arr[0] == 'Prep':
        time = time_to_num(arr[1]) + time_to_num(arr[3])
        direction = ' '.join(arr[4:])
    elif arr[0] == 'Cook':
        time = time_to_num(arr[3])
        direction = ' '.join(arr[4:])
    elif arr[0] == 'Ready In':
        time = time_to_num(arr[1])
        direction = ' '.join(arr[2:])
    elif arr[0] == 'Prep':
        time = -1
        direction = 'None'
    else:
        time = -1
        direction = ' '.join(arr)
    return time, direction


read_csv["time"] = read_csv["cooking_directions"].apply(lambda x: get_time(x)[0])
read_csv["recipe"] = read_csv["cooking_directions"].apply(lambda x: get_time(x)[1])
read_csv = read_csv.drop(columns=['cooking_directions'])


nltk.download('wordnet')
wnl = nltk.WordNetLemmatizer()


def word_tokenize(element):
    x = element.replace('^', ' ').replace('(', ' ').replace(')', ' ').replace('®', '').lower()
    arr = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(x)]
    return ' '.join(arr)


read_csv['name'] = read_csv['recipe_name'].apply(lambda x: word_tokenize(x))
read_csv["ingredients_token"] = read_csv["ingredients"].apply(lambda x: word_tokenize(x))
read_csv["tool"] = read_csv["recipe"].apply(lambda x: word_tokenize(x))
read_csv["ing_tool"] = read_csv[['ingredients_token', 'tool']].agg(' '.join, axis=1)
read_csv = read_csv.drop(columns=['tool', 'ingredients_token'])


read_csv["tokens"] = read_csv[['name', 'ing_tool']].agg(' '.join, axis=1)


def str_set(element):
    return set(re.split(' ', element))


read_csv['name'] = read_csv['name'].apply(lambda x: str_set(x))

read_csv["ing_tool"] = read_csv["ing_tool"].apply(lambda x: str_set(x))

nut_dict = {'sugars': 0, 'fat': 0, 'calories': 0, 'sodium': 0}
for element in read_csv.nutritions:
    res = ast.literal_eval(element)
    if res['sugars']['name']:
        nut_dict['sugars'] += res['sugars']['amount']
    if res['fat']['name']:
        nut_dict['fat'] += res['fat']['amount']
    if res['calories']['name']:
        nut_dict['calories'] += res['calories']['amount']
    if res['sodium']['name']:
        nut_dict['sodium'] += res['sodium']['amount']


def low_check(element, nutrition):
    res = ast.literal_eval(element)
    if res[nutrition]['name'] and nut_dict[nutrition] > res[nutrition]['amount'] * len_df:
        return True
    else:
        return False


len_df = len(read_csv)
for nut in nut_dict.keys():
    read_csv[nut] = read_csv["nutritions"].apply(lambda x: low_check(x, nut))

count = 0
for element in read_csv['tokens']:
    count += len(re.split(' ', element))
print(count // len_df)

cv = CountVectorizer(max_df=0.95, stop_words='english')
cv_text = cv.fit_transform(read_csv['tokens'])
features = cv.get_feature_names_out()

lda = LatentDirichletAllocation(n_components=100)
lda.fit(cv_text)

test = lda.transform(cv_text)

temp = []
for element in test:
    temp.append(np.argmax(element))
topic_class = temp

read_csv['topic'] = topic_class

read_csv = read_csv.drop(columns=['nutritions'])

read_csv.to_csv("kaggle_dataset/recipe_data.csv")

token_list = set()

for element in read_csv['ingredients']:
    x = element.replace('^', ' ').replace('(', ' ').replace(')', ' ').replace('®', '').lower()
    arr = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(x)]
    for ing in arr:
        token_list.add(ing)
for element in read_csv["recipe"]:
    x = ' '.join(re.split(r"\W+", element)).lower()
    arr = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(x)]
    for tool in arr:
        token_list.add(tool)
for element in read_csv['recipe_name']:
    x = element.replace('^', ' ').replace('(', ' ').replace(')', ' ').replace('®', '').lower()
    arr = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(x)]
    for ing in arr:
        token_list.add(ing)
token_list = pd.DataFrame(token_list)

token_list.to_csv("kaggle_dataset/token_list.csv")

print(token_list)
