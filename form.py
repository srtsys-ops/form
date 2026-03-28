import pickle
import streamlit as st

diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# input_data = [[
#     6,178,90,35,220,34.60,1.450,62
# ]]

# input_data = [[
#     3,126,88,41,235,39.30,0.704,27
# ]]

# Pregnancies = 3
# Glucose = 126
# BloodPressure = 88
# SkinThickness = 41
# Insulin = 235
# BMI = 39.30
# DiabetesPedigreeFunction = 0.704
# Age = 27

Pregnancies = 6
Glucose = 178
BloodPressure = 98
SkinThickness = 35
Insulin = 220
BMI = 34.6
DiabetesPedigreeFunction = 1.45
Age = 62



input_data = [[
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
]]

with st.form("diabetes_form"):

    # --- Row 1 ---
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = input(
            "Number of Pregnancies", 0, 20, key="Pregnancies"
        )
    with col2:
        Glucose = st.number_input(
            "Glucose Level (mg/dL)", 0, 300, key="Glucose"
        )
    with col3:
        BloodPressure = st.number_input(
            "Blood Pressure (mm Hg)", 0, 200, key="BloodPressure"
        )       

    # --- Row 2 ---
    col1, col2, col3 = st.columns(3)
    with col1:
        SkinThickness = st.number_input(
            "Skin Thickness (mm)", 0, 100, key="SkinThickness"
        )
    with col2:
        Insulin = st.number_input(
            "Insulin Level (µU/mL)", 0, 900, key="Insulin"
        )
    with col3:
        BMI = st.number_input(
            "BMI", 0.0, 70.0, format="%.2f", key="BMI"
        )

    # --- Row 3 ---
    col1, col2 = st.columns(2)
    with col1:
        DPF = st.number_input(
            "Diabetes Pedigree Function", 0.0, 3.0, format="%.3f", key="DPF"
        )
    with col2:
        Age = st.number_input(
            "Age", 1, 120, key="Age"
        )

    # -------------------------------------------------
    # 8️⃣ PREDICTION BUTTON
    # -------------------------------------------------
    col1, col2 = st.columns(2)
    with col1:
        predict_btn = st.form_submit_button("🔍 Diabetes Test Result", type="primary") 


diab_prediction = diabetes_model.predict(input_data)

# Display prediction result
if diab_prediction[0] == 1:
    st.error("🔴 The person is Diabetic")
else:
    st.success("🟢 The person is not Diabetic")
