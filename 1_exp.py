import streamlit as st

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="ScentSense", layout="wide")

# -------------------- GLOBAL STYLING --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Freestyle+Script:wght@300;500&family=Playfair+Display:wght@600&family=Poppins:wght@400;500&display=swap');

/* Background + font setup */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #F8F7F3 !important;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: none !important;
}

html, body {
    color: #3B2A4A;
    font-family: 'Poppins', sans-serif;
}

/* Buttons */
.stButton>button {
    background-color: #B088F9;
    color: white;
    border: none;
    padding: 0.8em 2em;
    border-radius: 30px;
    font-size: 1.2em;
    transition: 0.3s ease-in-out;
}

.stButton>button:hover {
    background-color: #A16AE8;
    transform: scale(1.05);
}

/* Fade animation */
@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}

div, h1, h2, p {
  animation: fadeIn 1.5s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# -------------------- NAVIGATION --------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------- HOME PAGE --------------------
if st.session_state.page == "home":
    home_html = """
    <div style="
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        height:85vh;
        position:relative;
        text-align:center;
        animation:fadeIn 1.5s ease-in-out;">

        <!-- Decorative scent bubbles -->
        <div style="
            position:absolute;
            top:10%;
            left:5%;
            width:180px;
            height:180px;
            background:radial-gradient(circle at center,#EBD9FF,#F8F7F3);
            border-radius:50%;
            filter:blur(25px);
            opacity:0.8;
            z-index:0;">
        </div>

        <div style="
            position:absolute;
            bottom:15%;
            right:10%;
            width:220px;
            height:220px;
            background:radial-gradient(circle at center,#D0B8FF,#F8F7F3);
            border-radius:50%;
            filter:blur(35px);
            opacity:0.7;
            z-index:0;">
        </div>

        <!-- Title -->
        <h1 style="
            font-family:'Freestyle Script',cursive;
            font-size:7em;
            color:#3B2A4A;
            z-index:1;
            margin-bottom:0.2em;">
            ScentSense
        </h1>

        <!-- Description Card -->
        <div style="
            background:rgba(255,255,255,0.7);
            backdrop-filter:blur(10px);
            border-radius:30px;
            box-shadow:0 4px 20px rgba(0,0,0,0.05);
            max-width:700px;
            padding:2em 3em;
            z-index:1;">
            <p style="
                color:#4B3F5A;
                font-size:1.1em;
                line-height:1.7em;">
                Discover your signature calming scent through a mood-based journey.<br><br>
                Whether you’re drawn to the soft whisper of lavender fields, the warmth of vanilla,
                or the crisp freshness of citrus — <b>ScentSense</b> helps you uncover the fragrance 
                that truly speaks to your soul.
            </p>
        </div>
    </div>
    """
    st.markdown(home_html, unsafe_allow_html=True)

    # Streamlit native button for navigation
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Take Quiz", key="quiz_start"):
        st.session_state.page = "quiz"
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- QUIZ PAGE --------------------
elif st.session_state.page == "quiz":
    st.markdown("<h1 style='text-align:center;'>Find Your Calming Scent</h1>", unsafe_allow_html=True)
    st.write("This is where your quiz questions will go!")

    # Example quiz question
    mood = st.radio(
        "How do you usually feel after a stressful day?",
        ["Tired and drained", "Restless and anxious", "Sad or heavy", "Irritable or tense"]
    )

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
