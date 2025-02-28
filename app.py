import streamlit as st
import base64
from joblib import load

# Load Model
model = load("model.pkl")

# Set Page Config
st.set_page_config(page_title="Placement Package Predictor", page_icon="💼", layout="centered")

# ----------------- Background Image -----------------
def set_bg(image_url):
    """
    Function to set background image using base64 encoding.
    """
    with open(image_url, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode()
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_img}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# Call Background Function (Change the file path below)
set_bg("https://github.com/MohdAhsan8178/Package-Predictor-Better-attempt/blob/main/background.jpg?raw=true")  # <-- REPLACE WITH YOUR IMAGE FILE PATH

# ----------------- Logo & Title -----------------
st.markdown("<h1 style='text-align: center; color: white;'>📊 Placement Package Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Enter your CGPA and get your estimated package!</p>", unsafe_allow_html=True)

# Sidebar with Logo (Dropdown Effect)
with st.sidebar:
    with st.expander("Mohd Ahsan 👇"):
        st.image("https://github.com/MohdAhsan8178/Package-Predictor-Better-attempt/blob/main/unnamed.jpg?raw=true", width=80)  # <-- REPLACE WITH YOUR LOGO FILE PATH
        st.markdown("[GitHub](https://github.com/MohdAhsan8178)", unsafe_allow_html=True)
        st.markdown("[LinkedIn](https://www.linkedin.com/in/mohd-ahsan8178/)", unsafe_allow_html=True)

# ----------------- Input Section -----------------
cgpa = st.slider("Enter CGPA", min_value=0.0, max_value=10.0, value=7.0, step=0.1)

if st.button("Predict"):
    package = model.predict([[cgpa]])[0]
    
    # Display Prediction in Magenta Text
    st.markdown(f"""
    <div style="background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 10px; text-align: center;">
        <h2 style="color: magenta;">Predicted Package: ₹{package:.2f} LPA</h2>
    </div>
    """, unsafe_allow_html=True)
