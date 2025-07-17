import streamlit as st
import pandas as pd
import joblib
import json

# Load model and threshold
model = joblib.load("final_model_pipeline.pkl")
with open("best_threshold.txt", "r") as f:
    threshold = float(f.read())

# Load top 20 SHAP features
with open("top_20_features.json", "r") as f:
    top_20_features = list(json.load(f).keys())

st.title("Customer Churn Predictor (Top 20 Features)")

# Separate numerical and categorical features
raw_numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
raw_categorical_cols = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
    'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod'
]

# Filter only the categorical features present in top_20_features
used_categorical = [col for col in raw_categorical_cols if col in top_20_features]
used_numerical = [col for col in raw_numerical_cols if col in top_20_features]

# Define dropdown options for categorical features
category_options = {
    'gender': ['Male', 'Female'],
    'SeniorCitizen': ['0', '1'],
    'Partner': ['Yes', 'No'],
    'Dependents': ['Yes', 'No'],
    'PhoneService': ['Yes', 'No'],
    'MultipleLines': ['No phone service', 'No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No internet service', 'No', 'Yes'],
    'OnlineBackup': ['No internet service', 'No', 'Yes'],
    'DeviceProtection': ['No internet service', 'No', 'Yes'],
    'TechSupport': ['No internet service', 'No', 'Yes'],
    'StreamingTV': ['No internet service', 'No', 'Yes'],
    'StreamingMovies': ['No internet service', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['Yes', 'No'],
    'PaymentMethod': [
        'Electronic check', 'Mailed check',
        'Bank transfer (automatic)', 'Credit card (automatic)'
    ]
}

# Collect user inputs
user_input = {}
st.header("Enter Customer Information")

# Input widgets for top 20 features
for feature in top_20_features:
    if feature in used_categorical:
        user_input[feature] = st.selectbox(feature, category_options[feature])
    elif feature in used_numerical:
        user_input[feature] = st.number_input(feature, value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input], columns=top_20_features)

# Prediction
if st.button("Predict Churn"):
    probability = model.predict_proba(input_df)[0][1]
    st.subheader(f"Predicted Churn Probability: {probability:.2f}")
    prediction = "Likely to Churn" if probability >= threshold else "Likely to Stay"
    st.success(f"Prediction: {prediction}")
