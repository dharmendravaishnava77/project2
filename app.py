import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.sav')

st.title("Sales Prediction App")
st.write("Predict sales based on advertising budgets for TV, Radio, and Newspaper.")

# Input fields for user
tv_budget = st.number_input("TV Budget ($)", min_value=0.0, value=100.0, step=1.0)
radio_budget = st.number_input("Radio Budget ($)", min_value=0.0, value=20.0, step=1.0)
newspaper_budget = st.number_input("Newspaper Budget ($)", min_value=0.0, value=15.0, step=1.0)

# Predict button
if st.button("Predict Sales"):
    input_data = pd.DataFrame({
        'TV': [tv_budget],
        'Radio': [radio_budget],
        'Newspaper': [newspaper_budget]
    })
    
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Sales: {prediction:.2f}")
