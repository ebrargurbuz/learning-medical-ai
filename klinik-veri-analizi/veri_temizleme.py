import pandas as pd
import numpy as np

# Hastane sisteminden çekilmiş, standart dışı ve hatalı ham veri
klinik_veri = {
    'Hasta_ID': [101, 102, 103, 104, 105, 106, 101], 
    'Yas': [45, 250, 38, np.nan, 55, 45, 45],  
    'Cinsiyet': ['E', 'Erkek', 'K', 'Kadın', 'e', 'K', 'E'], 
    'Kan_Basinci': [120, 130, np.nan, 140, 125, 120, 120], 
    'Kolesterol': [200, 220, 240, 190, "210 mg/dl", 200, 200] 
}

df = pd.DataFrame(klinik_veri)

print("--- 1. HAM HASTANE VERİSİ ---")
print(df)
print("\n--- 2. VERİ TİPLERİ VE ANATOMİSİ (info) ---")
df.info()


df['Kolesterol'] = df['Kolesterol'].astype(str).str.replace(' mg/dl', '')
df['Kolesterol'] = pd.to_numeric(df['Kolesterol'])
df = df.drop_duplicates(subset='Hasta_ID', keep='first')
print("\n--- 3. MÜDAHALE SONRASI DURUM ---")
print(df)
df.info()


#Gerekli gordugum filtreleme islemlerini yapalim
 
df = df[df['Yas'] < 120]  #Yaş, diğer klinik bulguları etkileyen temel değişkendir; diğer bulgulara bakılarak yaş tahmin edilemez. 250 gibi biyolojik olarak imkansız bir değeri (outlier) ortalamayla doldurmak sentetik (hayali) hasta yaratır. Bu yüzden o satır matristen tamamen silinmelidir.

df = df.dropna() #Elimizdeki veri seti çok küçük olduğu için eksik (NaN) değerleri istatistiksel yöntemlerle doldurmak modelin tarafsızlığını (bias) bozar. Bu boyuttaki bir laboratuvar verisinde en güvenli yöntem NaN barındıran satırları silmektir.

print("\n--- 4. SON TEMİZLİK (EĞİTİME HAZIR VERİ) ---")
print(df)

#Makine öğrenmesi algoritmaları metinlerle (string) matematiksel işlem yapamaz. Cinsiyeti 1 ve 2 yerine 0 ve 1 (Binary Encoding) olarak kodlamak, makinenin cinsiyetler arası matematiksel bir üstünlük/büyüklük ön yargısı kurmasını engeller.

cinsiyet_haritasi = {
    'E': 1, 'Erkek': 1, 'e': 1,
    'K': 0, 'Kadın': 0
}
df['Cinsiyet'] = df['Cinsiyet'].map(cinsiyet_haritasi)

print("\n--- 5. MAKİNE ÖĞRENMESİNE HAZIR, TEMİZ MATRİS ---")
print(df)
df.info()



df['Teshis'] = [0, 1, 0, 1] 

y = df['Teshis']
X = df.drop(['Teshis', 'Hasta_ID'], axis=1)# Hastalik teshisi yaparken Id degerinin herhangi bir anlami yok

print("\n--- X MATRİSİ (Öğrenilecek Tıbbi Özellikler) ---")
print(X)
print("\n--- y VEKTÖRÜ (Tahmin Edilecek Hedef) ---")
print(y)