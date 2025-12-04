# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Bank Customer Churn Prediction", layout="centered")

st.title("🏦 Bank Customer Churn Prediction")
st.write("Enter customer details and click **Predict**. The app will apply the same feature engineering used during training and show prediction + probability.")

#Paths
PIPELINE_PATH = "best_churn_pipeline.pkl"
TRAIN_CSV = "customer_data.csv"   # optional: used to compute 75th percentile for high_balance

#Load pipeline
if not os.path.exists(PIPELINE_PATH):
    st.error(f"Saved pipeline not found: {PIPELINE_PATH}. Please put your `best_churn_pipeline.pkl` in the same folder as this app.")
    st.stop()

try:
    pipeline = joblib.load(PIPELINE_PATH)
except Exception as e:
    st.error(f"Failed to load pipeline: {e}")
    st.stop()

#Compute high_balance threshold from training data if available
if os.path.exists(TRAIN_CSV):
    try:
        df_train = pd.read_csv(TRAIN_CSV)
        if 'balance' in df_train.columns:
            balance_75 = df_train['balance'].quantile(0.75)
        else:
            st.warning("Training CSV found but it does not contain 'balance' column. Falling back to default threshold.")
            balance_75 = 50000.0
    except Exception:
        st.warning("Could not read training CSV — falling back to default high_balance threshold.")
        balance_75 = 50000.0
else:
    balance_75 = 50000.0  # fallback if training CSV not provided

#Input form 
with st.form("input_form"):
    st.subheader("Customer Information")
    customer_id = st.number_input("Customer ID", min_value=1, value=373292028, step=1)
    credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=650)
    country = st.text_input("Country / Geography", value="France")
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    age = st.number_input("Age", min_value=18, max_value=120, value=40)
    tenure = st.number_input("Tenure (years with bank)", min_value=0, max_value=100, value=3)
    balance = st.number_input("Account Balance", min_value=0.0, value=50000.0, format="%.2f")
    products_number = st.number_input("Number of Products", min_value=0, max_value=10, value=2, step=1)
    credit_card = st.selectbox("Has Credit Card? (0 = No, 1 = Yes)", [0, 1], index=1)
    active_member = st.selectbox("Active Member? (0 = No, 1 = Yes)", [0, 1], index=1)
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=60000.0, format="%.2f")
    submit = st.form_submit_button("Predict")

if submit:
    # Build input dataframe exactly like your notebook did
    sample = {
        'customer_id': int(customer_id),
        'credit_score': float(credit_score),
        'country': country,
        'gender': gender,
        'age': int(age),
        'tenure': int(tenure),
        'balance': float(balance),
        'products_number': int(products_number),
        'credit_card': int(credit_card),
        'active_member': int(active_member),
        'estimated_salary': float(estimated_salary)
    }

    input_df = pd.DataFrame([sample])

    #Feature engineering
    # 1) balance_per_product
    input_df['balance_per_product'] = input_df['balance'] / (input_df['products_number'].replace(0, np.nan))
    input_df['balance_per_product'].fillna(0, inplace=True)

    # 2) salary_balance_ratio
    input_df['salary_balance_ratio'] = input_df['estimated_salary'] / (input_df['balance'].replace(0, np.nan))
    input_df['salary_balance_ratio'].replace([np.inf, -np.inf], np.nan, inplace=True)
    # Fill NaN with training median if available, otherwise 0
    if 'df_train' in locals() and 'estimated_salary' in df_train.columns and 'balance' in df_train.columns:
        sbr_median = df_train['estimated_salary'].div(df_train['balance'].replace(0, np.nan)).replace([np.inf, -np.inf], np.nan).median()
        input_df['salary_balance_ratio'].fillna(sbr_median, inplace=True)
    else:
        input_df['salary_balance_ratio'].fillna(0, inplace=True)

    # 3) age_group (same bins/labels as in notebook)
    bins = [0,25,35,45,55,65,100]
    labels = ['<25','25-34','35-44','45-54','55-64','65+']
    input_df['age_group'] = pd.cut(input_df['age'], bins=bins, labels=labels)

    # 4) tenure_bucket (same bins/labels)
    input_df['tenure_bucket'] = pd.cut(input_df['tenure'], bins=[-1,0,2,5,10,100], labels=['0','1-2','3-5','6-10','10+'])

    # 5) high_balance using 75th percentile from training (or fallback)
    input_df['high_balance'] = (input_df['balance'] > balance_75).astype(int)

    # Ensure categorical dtypes match training expectations
    categorical_features = ['country','gender','credit_card','active_member','age_group','tenure_bucket','high_balance']
    for c in categorical_features:
        if c in input_df.columns:
            input_df[c] = input_df[c].astype('object')

    # Drop ID as in training
    if 'customer_id' in input_df.columns:
        input_for_model = input_df.drop(columns=['customer_id'])
    else:
        input_for_model = input_df.copy()

    # Final: attempt prediction
    try:
        pred = pipeline.predict(input_for_model)[0]
        proba = pipeline.predict_proba(input_for_model)[0,1]
    except Exception as e:
        st.error("Prediction failed — pipeline reported an error.")
        st.exception(e)
        st.stop()

    # Show results
    st.subheader("Prediction Result")
    if pred == 1:
        st.error(f"🚨 Predicted: Customer WILL CHURN (probability = {proba:.3f})")
    else:
        st.success(f"✔ Predicted: Customer WILL NOT CHURN (probability = {proba:.3f})")

    st.write("### Prepared input used for prediction (after feature engineering):")
    st.json(input_for_model.to_dict(orient='records')[0])

    st.write("**Notes:**")
    st.markdown(f"- `high_balance` threshold (75th percentile) = **{balance_75:.2f}** (computed from `{TRAIN_CSV}` if available; else fallback).")
    st.markdown("- The app applies the same engineered features and dtypes as used during training.")

