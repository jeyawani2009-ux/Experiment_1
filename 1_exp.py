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
@import url('https://fonts.googleapis.com/css2?family=Freestyle+Script&display=swap');

html, body, [class*="css"] {
    background-color: #F8F7F3;
    color: #3B2A4A;
    font-family: 'Poppins', sans-serif;
}

/* Center the animation nicely */
.svg-container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 3rem;
    margin-top: -3rem;
}

/* Create the handwriting animation effect */
path {
  fill: none;
  stroke: #6D2E46;
  stroke-width: 3;
  stroke-dasharray: 1800;
  stroke-dashoffset: 1800;
  animation: draw 4s ease-in-out forwards;
}

/* Once the stroke draws, the text fades in */
text {
  font-family: 'Freestyle Script', cursive;
  font-size: 140px;
  fill: #6D2E46;
  opacity: 0;
  animation: fadeInText 2s ease-in-out 3.8s forwards;
}

/* Keyframes for handwriting effect */
@keyframes draw {
  to {
    stroke-dashoffset: 0;
  }
}

/* Keyframes for text fade-in */
@keyframes fadeInText {
  to {
    opacity: 1;
  }
}
</style>

<!-- Handwriting SVG animation for 'Scent Sense' -->
<div class="svg-container">
<svg width="900" height="200" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg">
  <path d="M20,150 Q150,20 300,120 T600,130 T850,80" />
  <text x="100" y="150">Scent Sense</text>
</svg>
</div>
""", unsafe_allow_html=True)
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
