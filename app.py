
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Smart Soil", layout="wide")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1 style='text-align:center; color:#2E7D32;'>🌱 Smart Soil AI Dashboard</h1>
<p style='text-align:center;'>AI-powered Soil Fertility, Soil Type & Crop Recommendation</p>
<hr>
""", unsafe_allow_html=True)

# -----------------------------
# -----------------------------
data = pd.DataFrame({
    'N': [90,60,30,20,70,50],
    'P': [80,50,20,10,60,40],
    'K': [70,40,30,20,65,35],
    'pH': [6.5,7.0,5.5,5.0,6.8,6.2],
    'Temp': [30,28,35,32,31,29],
    'Rain': [250,150,80,60,200,120],
    'Hum': [70,65,50,45,75,60],
    'Fertility': ['High','Medium','Low','Low','High','Medium'],
    'Soil': ['Loamy','Loamy','Sandy','Sandy','Loamy','Loamy']
})

# -----------------------------
# TRAIN MODEL
# -----------------------------
X = data[['N','P','K','pH','Temp','Rain','Hum']]
y_f = data['Fertility']
y_s = data['Soil']

model_f = RandomForestClassifier().fit(X, y_f)
model_s = RandomForestClassifier().fit(X, y_s)

# -----------------------------
# SIDEBAR INPUT
# -----------------------------
st.sidebar.title("🌾 Input Parameters")

n = st.sidebar.slider("Nitrogen (N)", 0, 150, 50)
p = st.sidebar.slider("Phosphorus (P)", 0, 150, 50)
k = st.sidebar.slider("Potassium (K)", 0, 150, 50)
ph = st.sidebar.slider("pH", 0.0, 14.0, 6.5)
temp = st.sidebar.slider("Temperature (°C)", 0, 50, 30)
rain = st.sidebar.slider("Rainfall (mm)", 0, 500, 100)
hum = st.sidebar.slider("Humidity (%)", 0, 100, 60)

predict = st.sidebar.button("🚀 Predict")

# -----------------------------
# PREDICTION
# -----------------------------
if predict:

    sample = [[n,p,k,ph,temp,rain,hum]]

    fertility = model_f.predict(sample)[0]
    soil = model_s.predict(sample)[0]

    # Crop Logic
    if fertility == "High":
        crop = "Rice" if rain > 200 else "Wheat"
        reason = "High nutrients support high-yield crops"
    elif fertility == "Medium":
        crop = "Maize" if temp > 30 else "Barley"
        reason = "Moderate fertility supports seasonal crops"
    else:
        crop = "Pulses"
        reason = "Low fertility crops improve soil health"

    # -----------------------------
    # RESULT
    # -----------------------------
    st.subheader("🌾 Prediction Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Fertility", fertility)
    col2.metric("Soil Type", soil)
    col3.metric("Crop", crop)

    st.success(f"Reason: {reason}")



# -----------------------------
st.markdown("---")
st.write("Developed by Akshaya Kumar,Theepak T")
