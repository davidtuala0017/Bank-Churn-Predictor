
import streamlit as st
import pandas as pd
import joblib

# Load the trained model and the column order
model = joblib.load("churn_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("🏦 Bank Customer Churn Predictor")
st.write("Fill in a customer's details to predict if they are likely to leave the bank.")

# Inputs for the user
credit_score = st.slider("Credit Score", 300, 850, 650)
age = st.slider("Age", 18, 95, 40)
tenure = st.slider("Years as Customer (Tenure)", 0, 10, 5)
balance = st.number_input("Account Balance", 0.0, 300000.0, 75000.0)
num_products = st.slider("Number of Products", 1, 4, 1)
has_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active = st.selectbox("Is Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 100000.0)
geography = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])

# Button
if st.button("Predict"):
    row = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "Num Of Products": num_products,
        "Has Credit Card": 1 if has_card == "Yes" else 0,
        "Is Active Member": 1 if is_active == "Yes" else 0,
        "Estimated Salary": salary,
        "Geography_Germany": True if geography == "Germany" else False,
        "Geography_Spain": True if geography == "Spain" else False,
        "Gender_Male": True if gender == "Male" else False,
    }
    X_new = pd.DataFrame([row])[columns]

    prob = model.predict_proba(X_new)[0][1]

    st.write("---")
    if prob >= 0.30:
        st.error(f"⚠️ Likely to LEAVE — {prob*100:.0f}% risk")
    else:
        st.success(f"✅ Likely to STAY — {prob*100:.0f}% risk of leaving")
