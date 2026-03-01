# 🩺 Diyabet Teşhis ve Risk Asistanı

Bu proje, **Pima Indians Diabetes Dataset** kullanılarak geliştirilmiş bir makine öğrenmesi tabanlı diyabet risk tahmin uygulamasıdır.  
Uygulama, kullanıcıdan alınan sağlık verilerine göre diyabet risk oranını tahmin eder ve sonucu görsel olarak sunar.

Streamlit ile geliştirilmiş interaktif bir web arayüzüne sahiptir.

---

## 🚀 Proje Amacı

Bu projenin amacı:

- Sağlık verileri üzerinden diyabet risk tahmini yapmak
- Makine öğrenmesi modeli ile sınıflandırma gerçekleştirmek
- Streamlit ile kullanıcı dostu bir arayüz geliştirmek
- Feature engineering ve veri ön işleme tekniklerini uygulamak

---

## 🧠 Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Random Forest Classifier

---

## 📊 Veri Seti

Kullanılan veri seti:

- **diabetes.csv**
- 768 gözlem
- 8 bağımsız değişken
- 1 hedef değişken (Outcome)

### Özellikler:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (0 = Diyabet Yok, 1 = Diyabet Var)

---

## 🔎 Veri Ön İşleme

Projede aşağıdaki veri temizleme ve feature engineering adımları uygulanmıştır:

- 0 değerleri (Glucose, BloodPressure, SkinThickness, Insulin, BMI) → NaN yapıldı
- Eksik değerler median ile dolduruldu
- Insulin değeri 350 üst sınır ile clip edildi
- Age değeri 65 üst sınır ile clip edildi
- StandardScaler ile veriler ölçeklendirildi

---

## 🌲 Kullanılan Model

Model: **RandomForestClassifier**

Parametreler:

- n_estimators = 100
- class_weight = "balanced"
- max_depth = 12
- min_samples_leaf = 5
- random_state = 42

Model tüm veri üzerinde eğitilmiştir ve kullanıcı girdisine göre tahmin üretmektedir.

---

## 🖥️ Uygulama Arayüzü

Streamlit arayüzünde:

- Sidebar üzerinden hasta verileri girilir
- "Risk Analizini Başlat" butonuna basılır
- Model tahmin sonucu gösterilir
- Risk yüzdesi progress bar ile görselleştirilir
- Uyarı mesajı gösterilir

---

pip install streamlit pandas numpy scikit-learn
streamlit run app.py
