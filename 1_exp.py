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
  from {opacity: 0;}
  to {opacity: 1;}
}

div, h1, h2, p {
  animation: fadeIn 1.5s ease-in-out;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------------------- NAVIGATION --------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------- HOME PAGE --------------------
if st.session_state.page == "home":
    st.markdown("""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
        position: relative;
        text-align: center;
        animation: fadeIn 1.5s ease-in-out;">
        
        <!-- Decorative scent bubbles -->
        <div style="
            position: absolute;
            top: 10%;
            left: 5%;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle at center, #EBD9FF, #F8F7F3);
            border-radius: 50%;
            filter: blur(25px);
            opacity: 0.8;
            z-index: 0;">
        </div>

        <div style="
            position: absolute;
            bottom: 15%;
            right: 10%;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle at center, #D0B8FF, #F8F7F3);
            border-radius: 50%;
            filter: blur(35px);
            opacity: 0.7;
            z-index: 0;">
        </div>

        <!-- Title -->
        <h1 style="
            font-family: 'Freestyle Script', cursive;
            font-size: 7em;
            color: #3B2A4A;
            z-index: 1;
            margin-bottom: 0.2em;">
            ScentSense
        </h1>

        <!-- Description Card -->
        <div style="
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            max-width: 700px;
            padding: 2em 3em;
            z-index: 1;">
            
            <p style="
                font-family: 'Poppins', sans-serif;
                color: #4B3F5A;
                font-size: 1.1em;
                line-height: 1.7em;">
                Discover your signature calming scent through a mood-based journey. 
                <br><br>
                Whether you’re drawn to the soft whisper of lavender fields, the warmth of vanilla,
                or the crisp freshness of citrus — <b>ScentSense</b> helps you uncover the fragrance 
                that truly speaks to your soul.
            </p>
        </div>

        <!-- Take Quiz Button -->
        <div style="margin-top: 3em; z-index: 1;">
            <button id="quiz-btn" 
                style="
                    background-color: #B088F9;
                    color: white;
                    border: none;
                    padding: 1em 2.5em;
                    border-radius: 30px;
                    font-size: 1.2em;
                    cursor: pointer;
                    transition: 0.3s ease-in-out;">
                Take Quiz
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Streamlit button to change page
    if st.button("Take Quiz", key="quiz_start"):
        st.session_state.page = "quiz"

# -------------------- QUIZ PAGE --------------------
elif st.session_state.page == "quiz":
    st.markdown("<h1 style='text-align:center;'>Find Your Calming Scent</h1>", unsafe_allow_html=True)
    st.write("This is where your quiz questions will go!")

    # Example quiz question
    mood = st.radio("How do you usually feel after a stressful day?",
                    ["Tired and drained", "Restless and anxious", "Sad or heavy", "Irritable or tense"])

    # Back button
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"

