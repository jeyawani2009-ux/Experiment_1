import streamlit as st

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="ScentSense", layout="wide")

# -------------------- STYLING --------------------

page_bg = """
<style>
/* Entire app background */
.stApp {
    background-color: #F8F7F3 !important;  /* a slightly darker, aesthetic beige */
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
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Freestyle+Script:wght@300;500&family=Playfair+Display:wght@600&display=swap');

html, body, [class*="css"] {
    background-color: #F8F7F3; /* darker aesthetic beige */
    background-attachment: fixed;
    background-size: cover;
    color: #3B2A4A;
    font-family: 'Poppins', sans-serif;
}

/* Remove Streamlit's default padding */
[data-testid="stAppViewContainer"] {
    padding-top: 0rem !important;
    padding-left: 2rem !important;
    margin-top: 0rem !important;
}

/* Handwritten header animation */
h1 {
    font-family: 'Freestyle Script', cursive !important;
    text-align: left;
    font-size: 8em !important;
    color: #A66790;
    margin-top: -5rem !important;
    margin-bottom: 0.1em !important;
}
p, h2 {
    text-align: left
    font-size: 1.1em;
}

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

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}0

div, h1, h2, p {
  animation: fadeIn 1.5s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown(page_bg, unsafe_allow_html=True)

# -------------------- NAVIGATION --------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------- HOME PAGE --------------------
if st.session_state.page == "home":
    st.markdown("<h1>ScentSense</h1>", unsafe_allow_html=True)
    st.markdown("<p>Write your app’s description here later...</p>", unsafe_allow_html=True)

    if st.button("Take Quiz"):
        st.session_state.page = "quiz"

# -------------------- QUIZ PAGE --------------------
elif st.session_state.page == "quiz":
    st.markdown("<h1 style='text-align:center;'>Find Your Calming Scent</h1>", unsafe_allow_html=True)
    st.write("This is where your quiz questions will go!")

    # Example quiz question placeholder
    mood = st.radio("How do you usually feel after a stressful day?",
                    ["Tired and drained", "Restless and anxious", "Sad or heavy", "Irritable or tense"])

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
