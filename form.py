import pickle
import streamlit as st

diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

#======== Direct values ===============
# input_data = [[
#     6,178,90,35,220,34.60,1.450,62
# ]]

# input_data = [[
#     3,126,88,41,235,39.30,0.704,27
# ]]

#=========== Values getting from Variable ===========
# Pregnancies = 3
# Glucose = 126
# BloodPressure = 88
# SkinThickness = 41
# Insulin = 235
# BMI = 39.30
# DiabetesPedigreeFunction = 0.704
# Age = 27

# Pregnancies = 6
# Glucose = 178
# BloodPressure = 98
# SkinThickness = 35
# Insulin = 220
# BMI = 34.6
# DiabetesPedigreeFunction = 1.45
# Age = 62

defaults = {
    "Pregnancies": 0, "Glucose": 0, "BloodPressure": 0,
    "SkinThickness": 0, "Insulin": 0,  "BMI": 0.0,
    "DPF": 0.0,  "Age": 1
}

#=========== Clear & Title ============

def clear_diabetes_form(): 
    for key, value in defaults.items():
        st.session_state[key] = value    
        

col_title, col_btn1, col_btn2 = st.columns([4, 1, 1])

with col_title:
    st.header("🩸 Diabetes Prediction", divider="blue")

with col_btn1:
    st.markdown("<br>", unsafe_allow_html=True)
        
with col_btn2:      
    st.button("🧹 Clear", type="secondary", on_click=clear_diabetes_form)

#=================== Sample Data ==============
DIABETES_SAMPLES = {
    "Select Sample": None,

    "1️⃣ Sample Data": {
        "Pregnancies": 3, "Glucose": 126, "BloodPressure": 88,
        "SkinThickness": 41, "Insulin": 235, "BMI": 39.3,
        "DPF": 0.704, "Age": 27
    },

    "2️⃣ Sample Data": {
        "Pregnancies": 2, "Glucose": 135, "BloodPressure": 82,
        "SkinThickness": 28, "Insulin": 140, "BMI": 28.9,
        "DPF": 0.78, "Age": 45
    },

    "3️⃣ Sample Data": {
        "Pregnancies": 6, "Glucose": 178, "BloodPressure": 90,
        "SkinThickness": 35, "Insulin": 220, "BMI": 34.6,
        "DPF": 1.45, "Age": 62
    }
}


st.selectbox(
    "🧪 Load Sample Patient",
    list(DIABETES_SAMPLES.keys()),
    key="diabetes_sample"
)


# =============== values getting from User interface(form) ==============

with st.form("diabetes_form"):

    # --- Row 1 ---
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input(
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
        DiabetesPedigreeFunction = st.number_input(
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

if predict_btn:

    diab_prediction = diabetes_model.predict(input_data)

    # Display prediction result
    if diab_prediction[0] == 1:
        st.error("🔴 The person is Diabetic")
    else:
        st.success("🟢 The person is not Diabetic")
