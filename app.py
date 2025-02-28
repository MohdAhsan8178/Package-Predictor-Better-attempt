from joblib import load
from numpy import array
import streamlit as st
import time

# Load the model
model = load("model.pkl")

# Custom Page Config
st.set_page_config(page_title="Placement Package Prediction", page_icon="📊", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    * { font-family: 'Poppins', sans-serif; }
    .stApp {
        background: url("https://github.com/MohdAhsan8178/Package-Predictor-Better-attempt/blob/main/background.jpg?raw=true") no-repeat center center fixed;
        background-size: cover;
    }
    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 2.5rem;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 1.2rem;
    }
    .result-box {
        text-align: center;
        background: #F0F2F6;
        padding: 15px;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title & Subtitle
st.markdown("<h1 class='title'>📊 Placement Package Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Enter your CGPA and get your estimated package!</h3>", unsafe_allow_html=True)

# Input Section
col1, col2 = st.columns([2, 1])
with col1:
    cgpa_input = st.number_input("Enter CGPA", max_value=10.0, min_value=0.0, step=0.1)
with col2:
    st.image("https://github.com/MohdAhsan8178/Package-Predictor-Better-attempt/blob/main/unnamed.jpg?raw=true", width=100)

# Predict Button with Progress Animation
if st.button("Predict"):
    with st.spinner("Predicting..."):
        time.sleep(2)  # Simulate processing time
    inputf = array([[cgpa_input]])
    prediction = model.predict(inputf)[0]
    st.markdown(f"<div class='result-box'>Predicted Package: ₹{prediction:.2f} LPA 🎉</div>", unsafe_allow_html=True)

# Social Media Links
st.markdown(
    """
    <p style='text-align: center;'>
        <a href="https://github.com/MohdAhsan8178" target="_blank">
            <img src="https://img.icons8.com/material-rounded/48/github.png" width="30px">
        </a>
        <a href="https://www.linkedin.com/in/mohd-ahsan8178/">
            <img src="https://img.icons8.com/material-rounded/48/linkedin.png" width="30px">
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
