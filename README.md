# MLRecipeRecommenderService

İnsanlar yemek yaparken daha fazla alternatif tarife sahip olmayı tercih ederler. Bu projede,İnsanların yemek tarifi ararken zaman kaybını azaltarak pratik yemek tarifi önerileri almalarına veya kişilerin yemek zevklerine benzer öneriler alarak insanların yeme davranışlarını değiştirmelerine yardımcı olacaktır.

İÇERİĞE BAĞLI YEMEK ÖNERİ !

[Uploading Ekran Resmi 2022-06-24 15.47.33.png…]()
<img width="518" alt="Ekran Resmi 2022-06-24 15 47 44" src="https://user-images.githubusercontent.com/43795927/175538966-49f6367e-218d-4b07-a56e-c7dcd2fb4f88.png">

Metin Analizi ile Yemek Öneri
•Pythonda bulunan “CountVectorizer” özelliği ile metinde bulunan özellikler çıkarılır.
•Bu özellik seçilen kelimenin matrisin bir sütunu tarafındantemsil edildiği ve belgedeki her metin örneğinin matriste bir satıra eşlenik
olduğu bir matris oluşturur. 
•Her hücrenin değeri, söz konusu metin örneğindeki kelimenin sayısıdır. Bu şekilde girilen metnin özellikleri çıkarılır. 
•Çıkarılan özellikler ile anahtar kelimeleri en çok eşleşen yemek tarifleri benzer olarak önerilir.
•Çıkarılan özellikler : Pişirme Yöntemi,Yemek Tarif Süreleri,Besin Değerleri (high protein", "high fiber", "low fat", "low carb", "low sodium" and "balanced"),Yemeklerin içerisinde kullanılan malzelemeler.


<img width="473" alt="Ekran Resmi 2022-06-24 15 51 47" src="https://user-images.githubusercontent.com/43795927/175539633-5f468b27-9a00-4546-9935-7589e231a96e.png">
