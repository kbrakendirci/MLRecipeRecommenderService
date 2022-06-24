# MLRecipeRecommenderService

İnsanlar yemek yaparken daha fazla alternatif tarife sahip olmayı tercih ederler. Bu projede,İnsanların yemek tarifi ararken zaman kaybını azaltarak pratik yemek tarifi önerileri almalarına veya kişilerin yemek zevklerine benzer öneriler alarak insanların yeme davranışlarını değiştirmelerine yardımcı olacaktır.

İÇERİĞE BAĞLI YEMEK ÖNERİ !
Kullanıcı android uygulamada sayfada bulunan arama kısmına, veri tabanında bulunan herhangi bir yemek tarifinin ismini girerek arama yaptığında,  yemeğin içerik (yemek tarifi içerisinde kullanılan malzemeler) kısmına benzer içeriğe sahip tarifler önerilmektedir. Bu işlem İçerik Bazlı Filtreleme ile yemek tariflerinin malzeme listesinde geçen anahtar kelimeleri bulur ve benzer kelimeleri barındıran yemek tariflerini kullanıcıya sunar. İçerik bazlı filtreleme için Öklid uzaklığı kullanılmaktadır.
[image](https://user-images.githubusercontent.com/43795927/175541102-3ff72389-45c1-4060-bcc0-fdb40d21efef.png)

Uygulama, kullanıcıların yemek alışkanlıklarına uygun daha fazla yemek tarif önerisi almalarını amaçlar.Bu sayfada kullanıcının içeriğe bağlı öneri almak için sevdiği yemeğin ismini girer. Kullanıcı adını girdiği yemeğin oy yada yorum sayısına göre yemek tariflerini listeleyebilir. Kullanıcının ismini girdiği yemeğin içeriğinde kullanılan malzemelerin en benzer olduğu yemek tarifleri listelenmekte ve kullanıcıya önerilmektedir. Kullanıcı bu özellik ile yemek zevkine uygun yeni tarifler keşfedebilir.![image](https://user-images.githubusercontent.com/43795927/175540973-def94335-edc2-4c58-b7bf-543ccce8f61a.png)


<img width="510" alt="Ekran Resmi 2022-06-24 15 57 24" src="https://user-images.githubusercontent.com/43795927/175540591-0d90d4eb-40e9-4d5e-bc7a-83c128aa14eb.png">



<img width="518" alt="Ekran Resmi 2022-06-24 15 47 44" src="https://user-images.githubusercontent.com/43795927/175538966-49f6367e-218d-4b07-a56e-c7dcd2fb4f88.png">
<img width="518" alt="Ekran Resmi 2022-06-24 15 53 32" src="https://user-images.githubusercontent.com/43795927/175539953-b817deea-3050-46e6-869b-009350d9af0d.png">


Metin Analizi ile Yemek Öneri
•Pythonda bulunan “CountVectorizer” özelliği ile metinde bulunan özellikler çıkarılır.
•Bu özellik seçilen kelimenin matrisin bir sütunu tarafındantemsil edildiği ve belgedeki her metin örneğinin matriste bir satıra eşlenik
olduğu bir matris oluşturur. 
•Her hücrenin değeri, söz konusu metin örneğindeki kelimenin sayısıdır. Bu şekilde girilen metnin özellikleri çıkarılır. 
•Çıkarılan özellikler ile anahtar kelimeleri en çok eşleşen yemek tarifleri benzer olarak önerilir.
•Çıkarılan özellikler : Pişirme Yöntemi,Yemek Tarif Süreleri,Besin Değerleri (high protein", "high fiber", "low fat", "low carb", "low sodium" and "balanced"),Yemeklerin içerisinde kullanılan malzelemeler.


<img width="473" alt="Ekran Resmi 2022-06-24 15 51 47" src="https://user-images.githubusercontent.com/43795927/175539633-5f468b27-9a00-4546-9935-7589e231a96e.png">

Veri Seti

Bu araştırmada, Kaggle.com'dan alınan açık kaynaklı veri kümesi kullanılmıştır. Kaggle websitesi, araştırma amacıyla kullanılmak üzere çeşitli veri türleri sağlayan halka açık bir platformdur. Öneri sistemi için Kaggle veri seti foodRecSys-V1 kullanıldı. Bu veri seti, yemek tarifleri için popüler bir web sitesi olan AllRecipes web sitesinden alınan tarifleri içerir. ![image](https://user-images.githubusercontent.com/43795927/175541411-e7ad1152-3054-41ef-8dba-9d7a761f6755.png)
