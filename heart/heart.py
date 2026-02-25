import pandas as pd

df = pd.read_csv(r'C:\Users\gurbu\OneDrive\Desktop\archive\heart.csv')
print(df.head(10))
print(df.info())  #Dtype bilgisi 
print(df.describe())

wrong_ca_number = len(df[df['ca'] == 4])
print("Number of wrong information in Ca",wrong_ca_number)

wrong_thal_number = len(df[df['thal'] == 0])
print("Number of wrong information in Thal",wrong_thal_number)


df = df[(df['ca'] != 4) & (df['thal'] != 0)]
print("Temizlenmiş matristeki toplam hasta sayısı:", len(df))

import matplotlib.pyplot as plt
import seaborn as sns

correlation_matrix = df.corr() # Tum sutunlar arasindaki istatistiksel iliski heasaplandi 
plt.figure(figsize=(12,7)) # grafik icin boyut ayarla
sns.heatmap(correlation_matrix, annot = True, cmap='coolwarm', fmt=".2f")
plt.title("Tıbbi Özellikler Korelasyon Isı Haritası")
plt.show()

from sklearn.model_selection import train_test_split
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Eğitim için ayrılan hasta sayısı (X_train):", X_train.shape)
print("Test için ayrılan hasta sayısı (X_test):", X_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
tahminler = model.predict(X_test)
basari_orani = accuracy_score(y_test, tahminler)
print(f"Yapay Zeka Modelinin Başarı Oranı: % {basari_orani * 100:.2f}")


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, tahminler)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds')
plt.title("Modelin Karmaşıklık Matrisi (Confusion Matrix)")
plt.xlabel("Yapay Zekanın Tahmini (0: Sağlıklı, 1: Hasta)")
plt.ylabel("Hastanın Gerçek Durumu (0: Sağlıklı, 1: Hasta)")
plt.show()





olasiliklar = model.predict_proba(X_test)[:, 1]
yeni_esik = 0.30

yeni_tahminler = (olasiliklar >= yeni_esik).astype(int)

from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

cm_yeni = confusion_matrix(y_test, yeni_tahminler)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_yeni, annot=True, fmt='d', cmap='Blues')
plt.title("Yeni Karar Eşiği (0.30) ile Karmaşıklık Matrisi")
plt.xlabel("Yapay Zekanın Tahmini")
plt.ylabel("Hastanın Gerçek Durumu")
plt.show()

print(classification_report(y_test, yeni_tahminler))