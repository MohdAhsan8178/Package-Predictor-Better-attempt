import streamlit as st
import requests
from joblib import load

# Load the trained model
model = load("model.pkl")

# Function to set background from URL (Updated)
def set_bg(image_url):
    st.markdown(
    
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
            color: white;
            font-family: 'Arial', sans-serif;
        }}
        .result-box {{
            background-color: rgba(50, 0, 100, 0.8);
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            color: magenta;
            font-size: 24px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }}
        .result-box:hover {{
            transform: scale(1.05);
        }}
        </style>

        unsafe_allow_html=True

# Set the background image (Use RAW GitHub link)
set_bg("https://raw.githubusercontent.com/MohdAhsan8178/Package-Predictor-Better-attempt/main/background.jpg")

# Title and subtitle
st.markdown("<h1 style='text-align: center;'> Placement Package Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Enter your CGPA and get your estimated package!</h3>", unsafe_allow_html=True)

# Input box for CGPA
cgpa = st.slider("Enter CGPA", min_value=0.0, max_value=10.0, value=7.0, step=0.1)

# Predict button
if st.button("Predict"):
    package = model.predict([[cgpa]])[0]  # Predict using the model
    result_text = f"Predicted Package: ₹{package:.2f} LPA 🎉"
    st.markdown(f"<div class='result-box'>{result_text}</div>", unsafe_allow_html=True)
