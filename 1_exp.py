import streamlit as st

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="ScentSense", layout="wide")

# -------------------- STYLING --------------------
page_bg = """
<style>
/* Entire app background */
.stApp {
    background-color: #F8F7F3 !important;
    background-image: none !important;
}

/* Remove Streamlit's default white backgrounds */
[data-testid="stAppViewContainer"] {
    background-color: #F8F7F3 !important;
}

[data-testid="stHeader"] {
    background: none !important;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Freestyle+Script:wght@300;500&family=Playfair+Display:wght@600&family=Poppins:wght@400;500&display=swap');

html, body, [class*="css"] {
    background-color: #F8F7F3;
    color: #3B2A4A;
    font-family: 'Poppins', sans-serif;
}

/* Remove Streamlit default padding */
[data-testid="stAppViewContainer"] {
    padding-top: 0rem !important;
    padding-left: 2rem !important;
    margin-top: 0rem !important;
}

/* Header font */
h1 {
    font-family: 'Freestyle Script', cursive !important;
    text-align: left;
    font-size: 8em !important;
    color: #0A0A0A !important;
    margin-top: -5rem !important;
    margin-bottom: 0.1em !important;
}

/* Paragraphs */
p, h2 {
    text-align: left;
    font-size: 1.1em;
}

/* Button styling */
.stButton>button {
    background-color: #B088F9;
    color: white;
    border: none;
    padding: 0.8em 2em;
    border-radius: 30px;
    font-size: 1.2em;
    transition: 0.3s ease-in-out;
    display: block;
    margin: 2em auto;
}

.stButton>button:hover {
    background-color: #A16AE8;
    transform: scale(1.05);
}

/* Animation */
@keyframes fadeIn {
  from {
