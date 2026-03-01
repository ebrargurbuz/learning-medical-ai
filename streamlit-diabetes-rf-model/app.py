import pandas as pd
import numpy as np

df = pd.read_csv('diabetes.csv')

cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in cols_with_zeros:
    df[col] = df[col].replace(0, np.nan)

for col in cols_with_zeros:
    df[col] = df[col].fillna(df[col].median())
    
print(df.isnull().sum())
print(df.head())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Veri başarıyla ölçeklendi ve bölündü.")
print(f"Eğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

st.set_page_config(page_title="Diyabet Risk Analizi", layout="centered")
st.title("🩺 Diyabet Teşhis ve Risk Asistanı")
st.markdown("Lütfen soldaki bilgileri doldurarak analiz butonuna basın.")

@st.cache_resource
def setup_model():
    data = pd.read_csv('diabetes.csv')
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in cols:
        data[col] = data[col].replace(0, np.nan)
        data[col] = data[col].fillna(data[col].median())
    
    data['Insulin'] = data['Insulin'].clip(upper=350) 
    data['Age'] = data['Age'].clip(upper=65)
    data['Age_Glucose'] = (data['Age'] * data['Glucose']) / 100
    
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
  
    
    model = RandomForestClassifier(n_estimators=100,
                                   class_weight='balanced',
                                   max_depth=12,
                                   min_samples_leaf=5,
                                   random_state=42) 
    model.fit(X_scaled, y)
    return model, scaler
model, scaler = setup_model()


st.sidebar.header("Hasta Verileri")
def user_input_features():
    pregnancies = st.sidebar.slider("Hamilelik Sayısı", 0, 7, 3)
    glucose = st.sidebar.slider("Glikoz (Şeker)", 44, 200, 117)
    blood_p = st.sidebar.slider("Kan Basıncı", 20, 122, 72)
    skin_t = st.sidebar.slider("Deri Kalınlığı", 7, 99, 23)
    insulin = st.sidebar.slider("İnsülin", 14, 300, 30)
    bmi = st.sidebar.slider("Vücut Kitle Endeksi (BMI)", 18.0, 67.1, 32.0)
    dpf = st.sidebar.slider("Diyabet Soy Ağacı Fonksiyonu", 0.07, 2.42, 0.37)
    age = st.sidebar.slider("Yaş", 21, 81, 29)
    
    features = np.array([[pregnancies, glucose, blood_p, skin_t, insulin, bmi, dpf, age]])
    return features 

input_data = user_input_features() 

if st.button("Risk Analizini Başlat"):
    
    age_val = input_data[0][7]     
    glucose_val = input_data[0][1] 
    age_glucose_feat = (age_val * glucose_val) / 100
    final_input = np.append(input_data, [[age_glucose_feat]], axis=1)
    
    
    scaled_input = scaler.transform(final_input)
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)
    risk_percentage = prediction_proba[0][1] * 100
    
    st.divider()
    
    if prediction[0] == 1:
        st.error(f"⚠️ Yüksek Risk Tespit Edildi! Risk Oranı: %{risk_percentage:.1f}")
    else:
        st.success(f"✅ Düşük Risk. Risk Oranı: %{risk_percentage:.1f}")
    
    st.progress(int(risk_percentage))
    
    st.info("Not: Bu bir yapay zeka tahminidir, kesin tıbbi sonuç yerine geçmez.")