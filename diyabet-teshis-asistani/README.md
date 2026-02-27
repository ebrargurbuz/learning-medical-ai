# 🩺 Diyabet Sınıflandırma Projesi (Decision Tree)

## 📌 Proje Amacı

Bu proje, basit bir makine öğrenmesi sürecini uçtan uca göstermek amacıyla hazırlanmıştır.  
Karar Ağacı (Decision Tree) algoritması kullanılarak diyabet tahmini yapılmaktadır.

Proje kapsamında:

- Ham veri oluşturma
- Veri temizleme (Data Cleaning)
- Özellik / hedef değişken ayrımı
- Eğitim – Test bölme işlemi
- Model eğitimi
- Model performans değerlendirmesi

adımları uygulanmıştır.

---

## 📂 Veri Seti Özellikleri

Veri setinde aşağıdaki değişkenler bulunmaktadır:

| Değişken | Açıklama                |
| -------- | ----------------------- |
| Yas      | Hastanın yaşı           |
| Glikoz   | Kan şekeri seviyesi     |
| BMI      | Vücut Kitle İndeksi     |
| Sonuc    | 1: Diyabet, 0: Sağlıklı |

### ⚠ Ham Veride Bulunan Problemler

- Tekrarlanan hasta kimliği
- Gerçekçi olmayan yaş değeri (400)
- Geçersiz glikoz değeri (0)
- Eksik BMI değeri

Bu problemler veri ön işleme aşamasında düzeltilmiştir.

---

## 🧹 Veri Ön İşleme Adımları

1. Yinelenen kayıtlar kaldırıldı
2. Gerçekçi olmayan yaş değerleri filtrelendi (Yas < 120)
3. Glikoz değeri 0 olan kayıtlar NaN ile değiştirildi
4. Eksik Glikoz ve BMI değerleri medyan ile dolduruldu
5. Modelleme için gereksiz olan Hasta_Kimlik kolonu kaldırıldı

---

## 🤖 Kullanılan Model

- DecisionTreeClassifier
- Eğitim/Test oranı: %80 / %20
- random_state=42 (tekrar üretilebilirlik için)

---

## 📊 Model Performansı

Model, test verisi üzerinde %0 doğruluk oranı elde etmiştir.

Bu sonuç, veri setinin son derece küçük olmasından kaynaklanmaktadır.  
Yetersiz veri, modelin genelleme yapmasını engellemiştir.

Kurulan modelleme mantığı doğru olmakla birlikte, daha büyük ve temsili bir veri seti ile yeniden değerlendirilmelidir.

---

## 🛠 Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-learn
