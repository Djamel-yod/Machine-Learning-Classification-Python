import pickle
import numpy as np
import pandas as pd
import streamlit as st
# Load the pickle model
model = pickle.load(open('best_model.pkl', 'rb'))



def predict_churn(data):
  """Predicts customer churn using the loaded model.

  Args:
      data (pd.DataFrame): A DataFrame containing customer features.

  Returns:
      pd.DataFrame: A DataFrame with predicted churn labels (0 or 1).
  """

  # Preprocess data (assuming StandardScaler is used)
  scaled_data = scaler.transform(data)

  # Make predictions
  predictions = model.predict(scaled_data)

  # Convert predictions to DataFrame with descriptive column name
  return pd.DataFrame({'Churn Prediction': predictions})

def main():
  """Streamlit app for customer churn prediction."""

  # Title and description
  st.title("Customer Churn Prediction")
  st.write("Enter customer information to predict their likelihood of leaving the bank.")

  # Input fields with clear labels
  credit_score = st.number_input("Credit Score", min_value=0)
  age = st.number_input("Age", min_value=0)
  tenure = st.number_input("Tenure (Years with Bank)", min_value=0)
  balance = st.number_input("Account Balance", min_value=0.0)
  num_products = st.number_input("Number of Products Held")
  has_cr_card = st.selectbox("Has Credit Card?", options=["Yes", "No"])
  is_active_member = st.selectbox("Is Active Member?", options=["Yes", "No"])
  estimated_salary = st.number_input("Estimated Salary", min_value=0.0)

  # Convert categorical variables to numerical (assuming binary encoding)
  has_cr_card = 1 if has_cr_card == "Yes" else 0
  is_active_member = 1 if is_active_member == "Yes" else 0

  # Location dropdown with clear options
  location = st.selectbox("Location", options=["Germany", "Spain", "France"])

  # Gender dropdown with clear options
  gender = st.selectbox("Gender", options=["Male", "Female"])

  # One-hot encode location and gender (assuming this is the encoding used)
  location_onehot = pd.get_dummies(pd.DataFrame({'Location': [location]}))
  gender_onehot = pd.get_dummies(pd.DataFrame({'Gender': [gender]}))

  # Combine all features into a DataFrame (assuming this aligns with model input)
  data = pd.DataFrame({
      'CreditScore': [credit_score],
      'Age': [age],
      'Tenure': [tenure],
      'Balance': [balance],
      'NumOfProducts': [num_products],
      'HasCrCard': [has_cr_card],
      'IsActiveMember': [is_active_member],
      'EstimatedSalary': [estimated_salary]
  })

  # Concatenate one-hot encoded features
  data = pd.concat([data, location_onehot, gender_onehot], axis=1)

  # Predict
  if st.button("Predict Churn"):
    predictions = predict_churn(data)
    churn_label = predictions.iloc[0]['Churn Prediction']

    if churn_label == 1:
      st.success("The customer is predicted to leave the bank.")
    else:
      st.success("The customer is predicted to stay with the bank.")

if __name__ == '__main__':
  main()
