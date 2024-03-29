# MLRecipeRecommenderService

Proje Karabük Üniversitesi 2021-2022 yılı Bilgisayar Mühendisliği bitirme projesidir.İnsanlar yemek yaparken daha fazla alternatif tarife sahip olmayı tercih ederler. Bu projede,İnsanların yemek tarifi ararken zaman kaybını azaltarak pratik yemek tarifi önerileri almalarına veya kişilerin yemek zevklerine benzer öneriler alarak insanların yeme davranışlarını değiştirmelerine yardımcı olacaktır.

# İÇERİĞE BAĞLI YEMEK ÖNERİ 

<img width="500" alt="Ekran Resmi 2022-06-24 16 16 35" src="https://user-images.githubusercontent.com/43795927/175543820-b8ec41f7-4a15-4b2b-ae39-95f8e68886f6.png"><img width="500" alt="Ekran Resmi 2022-06-24 15 53 32" src="https://user-images.githubusercontent.com/43795927/175539953-b817deea-3050-46e6-869b-009350d9af0d.png">

Kullanıcı android uygulama içerisinde bulunan arama kısmına, veri tabanında bulunan herhangi bir yemek tarifinin ismini girerek arama yaptığında,Kullanıcıya,girilen yemeğin içerik (yemek tarifi içerisinde kullanılan malzemeler) kısmına benzer içeriğe sahip tarifler önerilmektedir.Bu işlem İçerik Bazlı Filtreleme ile yemek tariflerinin malzeme listesinde geçen anahtar kelimeleri bulur ve benzer kelimeleri barındıran yemek tariflerini kullanıcıya sunar.Kullanıcı adını girdiği yemeğin oy yada yorum sayısına göre yemek tariflerini listeleyebilir.İçerik bazlı filtreleme için Öklid uzaklığı kullanılmaktadır.Kullanıcılar yemek alışkanlıklarına uygun daha fazla yemek tarif önerisi alabilir ve yemek zevklerine uygun yeni tarifler keşfedebilir.

<img width="767" alt="Ekran Resmi 2022-06-24 16 22 40" src="https://user-images.githubusercontent.com/43795927/175544811-55b92379-08b6-4418-9f37-2e9c615bb6e5.png">




# Metin Analizi ile Yemek Öneri
Metin ile tarif önerisi alma kişilerin yeni lezzet kombinasyonları keşfetmelerine yardımcı olabilir.Kullanıcı yapmak istediği yemeği tarif etmesi gerekmektedir. Uygulamaya yapmak istediğiniz yemeğin malzemeleri, adımları, hazırlık süresi, pişme tipi yemek türü bilgilerini girerek ,parametrelere uygun yemek tarif önerisi alabilirsiniz.

Pythonda bulunan “CountVectorizer” özelliği ile metinde bulunan özellikler çıkarılır.Bu özellik seçilen kelimenin matrisin bir sütunu tarafındantemsil edildiği ve belgedeki her metin örneğinin matriste bir satıra eşlenik olduğu bir matris oluşturur. Her hücrenin değeri, söz konusu metin örneğindeki kelimenin sayısıdır. Bu şekilde girilen metnin özellikleri çıkarılır.Çıkarılan özellikler ile anahtar kelimeleri en çok eşleşen yemek tarifleri benzer olarak önerilir.
Çıkarılan özellikler : Pişirme Yöntemi,Yemek Tarif Süreleri,Besin Değerleri (high protein", "high fiber", "low fat", "low carb", "low sodium" and "balanced"),Yemeklerin içerisinde kullanılan malzelemeler

# Örnek Sorgu 
              Give me a Korean food which could be made without oven. It should be low fat and take less than a hour.                                      

              Steak which contains tomato and bacon could be made without oven.
              
              Meaty pasta which contains tomato and pepper and could be cooked less than 30 mins."
<img width="708" alt="Ekran Resmi 2022-06-24 16 54 57" src="https://user-images.githubusercontent.com/43795927/175550470-363f5121-43d5-4d65-9524-8f8f2fc37dd6.png">

# Veri Seti 

Bu araştırmada, Kaggle.com'dan alınan açık kaynaklı veri kümesi kullanılmıştır. Kaggle websitesi, araştırma amacıyla kullanılmak üzere çeşitli veri türleri sağlayan halka açık bir platformdur. Öneri sistemi için Kaggle veri seti foodRecSys-V1 kullanıldı. Bu veri seti, yemek tarifleri için popüler bir web sitesi olan AllRecipes web sitesinden alınan tarifleri içerir.
Kullanılan Veri Seti:https://www.kaggle.com/datasets/elisaxxygao/foodrecsysv1


