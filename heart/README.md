# Klinik Makine Öğrenmesi Temelleri: Kalp Hastalığı Teşhisi

Bu depo, sağlık verileri üzerinde veri temizleme, özellik seçimi ve temel sınıflandırma algoritmalarının mantığını oturtmak amacıyla oluşturulmuş bir kişisel laboratuvar çalışmasıdır.

---

## 1. Veri Matrisleştirme ve İnceleme

Pandas kütüphanesi kullanılarak ham sağlık verisi (kalp hastalığı veri seti) RAM'e alındı.

- `info()` fonksiyonu ile donanımsal veri tipleri kontrol edildi.
- `describe()` fonksiyonu ile verinin istatistiksel anatomisi çıkarılarak biyolojik uç değerler (anormallikler) analiz edildi.

## 2. Tıbbi Veri Temizleme

Kategorik verilerdeki (`ca` ve `thal`) ölçüm veya sistemsel giriş hataları tespit edildi.

> **Not:** Kategorik verilerde hatalı bilgileri silmek yerine mantıksız sentetik ortalamalar atamak, olmayan yeni hastalık türleri icat etmek anlamına gelir. Bu nedenle veri manipülasyonu yerine bu hastalar doğrudan matristen filtrelenerek temizlendi.

## 3. Korelasyon ve Özellik Seçimi

Yapay zekanın kararlarını hangi verilere dayandıracağını belirlemek için Seaborn ısı haritası (heatmap) kullanıldı. Hedef değişken (`target`) ile en yüksek doğrusal ilişkiye sahip klinik bulgular (`cp`, `exang`, `oldpeak`) matematiksel olarak kanıtlandı.

> **İstatistiksel Mantık - Korelasyon:** İki değişkenin birbirleriyle ne kadar ve hangi yönde ilişkili olduğunu gösteren istatistiksel ölçüdür.
>
> - **+1:** Mükemmel pozitif ilişki (Doğru orantı)
> - **0:** Hiçbir matematiksel ilişki yok
> - **-1:** Mükemmel negatif ilişki (Ters orantı)

## 4. Aşırı Öğrenmeyi (Overfitting) Önleme

Modelin hasta verilerini ezberlemesini engellemek için veri seti Eğitim (%80) ve Test (%20) olarak ikiye bölündü (Train/Test Split).

> **Sistemin Mantığı:** Model ona verilen verilerin tamamını görürse kuralları öğrenmez, satırları ezberler. Alışık olmadığı yeni bir veriyle (hastayla) karşılaştığında çuvallar. Bunu önlemek amacıyla verinin bir kısmını (%20) modelden saklarız ve daha sonrasında tahmin yeteneğini bu hiç görmediği veri üzerinde test ederiz.

## 5. Lojistik Regresyon ile Sınıflandırma

Aşırı öğrenme engellendikten sonra, ayrılan eğitim seti üzerinden ilk tıbbi temel yapay zeka algoritmamız eğitildi. Lojistik Regresyon, hastaları "Hasta" veya "Sağlıklı" olarak sınıflandırmak için kullanıldı.

## 6. Model Değerlendirmesi: Karmaşıklık Matrisi (Confusion Matrix)

Genel başarı oranının (Accuracy) tıbbi projelerde yanıltıcı olması sebebiyle, modelin yaptığı hataların türünü tespit etmek için Karmaşıklık Matrisi kullanıldı.

> **Klinik Karar Mantığı:** Sağlık projelerindeki asıl mühendislik hedefi yüksek doğruluk oranı değil, ölümcül Tip 2 hatalarını (**False Negative**) sıfıra indirmektir. Gerçekte hasta olan birini sağlıklı zannedip evine yollamak en büyük tıbbi hatadır. Bu nedenle asıl odaklanılması gereken metrik **Recall (Duyarlılık)** değeridir.
