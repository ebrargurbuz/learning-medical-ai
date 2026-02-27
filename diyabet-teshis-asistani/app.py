import pandas as pd
import numpy as np

# Raw dataset 
ham_veri = {
    'Hasta_Kimlik' : [1001,1002,1003,1004,1005,1006,1001], # Duplicate ID: 1001
    'Yas' : [45, 34, 400, 56, 28, 62, 45], # Age 400 is unrealistic
    'Glikoz' : [130, 0, 180, 150, 95, 0, 130], # 0 is invalid for glucose
    'BMI' : [25.5, 22.1, 28.0, np.nan, 19.5, 30.1, 25.5], # One missing value
    'Sonuc' : [1, 0, 1, 1, 0, 1, 1] # 1: Diabetes, 0: Healthy
}

df = pd.DataFrame(ham_veri)
print("Original Dataset")
print(df)

# Remove duplicate patients based on ID
df = df.drop_duplicates(subset = 'Hasta_Kimlik', keep='first')

# Remove unrealistic age values
df = df[df['Yas'] < 120]

# Replace invalid glucose values (0) with NaN
df['Glikoz'] = df['Glikoz'].replace(0, np.nan)

# Fill missing glucose values with median
df['Glikoz'] = df['Glikoz'].fillna(df['Glikoz'].median())

# Fill missing BMI values with median
df['BMI'] = df['BMI'].fillna(df['BMI'].median())

# Drop patient ID column (not useful for modeling)
df = df.drop('Hasta_Kimlik', axis=1) 

X = df.drop('Sonuc', axis=1)
Y = df['Sonuc']

print("\n--- TEMİZLENMİŞ X MATRİSİ (Özellikler) ---")
print(X)


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Train - Test Split
# 80% training, 20% testing

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

print("\nEĞİTİM İÇİN AYRILAN HASTA SAYISI")
print(len(X_train))
print("TEST İÇİN AYRILAN HASTA SAYISI ")
print(len(X_test))

# Makineye "Geçmiş hastaların tahlillerine (X_train) ve sonuçlarına (y_train) bakarak kuralları kendin öğren" diyoruz.

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

print("\nKarar Ağacı Modeli Başarıyla Eğitildi.")


from sklearn.metrics import confusion_matrix, classification_report
tahminler = model.predict(X_test)
matris = confusion_matrix(Y_test, tahminler)
print("\n--- 3. FAZ: KLİNİK TEST SONUCU (Karmaşıklık Matrisi) ---")
print(matris)
print("\n--- DETAYLI KLİNİK RAPOR ---")
print(classification_report(Y_test, tahminler, zero_division=0))


# Model evaluation results:
# Due to the extremely limited dataset size, the model failed to generalize properly.
# The accuracy score is 0%.
# This outcome highlights the need for a larger and more representative dataset.
