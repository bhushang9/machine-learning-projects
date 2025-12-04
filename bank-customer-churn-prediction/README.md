# 🏦 Bank Customer Churn Prediction

This project predicts whether a bank customer is likely to exit (churn) using machine learning classification techniques. The dataset contains customer demographics, banking details, product usage, and activity information. The model analyzes these features to identify customers with a high churn probability so banks can take retention measures proactively.

---

## 📊 Dataset Features Used

1. Credit Score
2. Country
3. Gender
4. Age
5. Tenure
6. Balance
7. Number of Products
8. Credit Card Status
9. Active Member
10. Estimated Salary
11. Exited (Target Variable)
    
---

## 🎯 Project Overview

- Loaded and explored the Bank Customer Dataset.
- Performed data cleaning and preprocessing.
- Encoded categorical variables.
- Split data into training and testing sets.
- Built a machine learning model to classify churn vs non-churn customers.
- Evaluated performance using metrics like accuracy, ROC-AUC, classification report, etc.
- Deployment using Streamlit.

---

## 🧠 Machine Learning Pipeline

1. Import required libraries
2. Load dataset
3. Encode categorical columns (Country, Gender)
4. Split data into features & target variable
5. Train model
6. Evaluate predictions
7. Plot metrics & store results

---

## 📈 Machine Learning Models Used

The following models were trained and evaluated during experimentation:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier
4. AdaBoost Classifier
5. Support Vector Classifier (SVC)

After comparison, Gradient Boosting Classifier was chosen as the final model for deployment due to consistently better performance during evaluation.

---

## ✔ Output

- Predicts whether a customer will churn using ML model inference.
- Performance metrics like Accuracy & ROC score used for evaluation.

---
