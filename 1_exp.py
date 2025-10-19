import streamlit as st

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="ScentSense", page_icon="🌸", layout="wide")

# -------------------- CUSTOM STYLE --------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #F5F5DC;  /* Beige/off-white */
    color: #3B2A4A;
    font-family: 'Poppins', sans-serif;
}

h1 {
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 3em;
    color: #6D2E46;
    margin-top: 2em;
}

.stButton>button {
    background-color: #B088F9;
    color: white;
    border: none;
    padding: 0.7em 2em;
    border-radius: 30px;
    font-size: 1.2em;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #A16AE8;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# -------------------- HOME PAGE CONTENT --------------------
st.markdown("<h1>🌸 ScentSense</h1>", unsafe_allow_html=True)

# Placeholder for description
st.write("Your description goes here…")

st.markdown("<br><br>", unsafe_allow_html=True)

# Button to navigate to quiz
if st.button("🧘 Take Quiz"):
    st.session_state['page'] = 'quiz'

# -------------------- NAVIGATION LOGIC --------------------
# Initialize session_state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Redirect to quiz page if button clicked
if st.session_state['page'] == 'quiz':
    # Here you can import and run your quiz code
    # For demo, just show placeholder
    st.write("🚀 Quiz Page Placeholder - Add your quiz here")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)


h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    text-align: center;
}

st.markdown("""
<style>
h1 {
    font-size: 2.5em;
    color: #6D2E46;
    text-align: center;
}
.stButton>button {
    background-color: #B088F9;
    color: white;
    border-radius: 30px;
    padding: 0.6em 2em;
    font-size: 1em;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stButton>button {
    background-color: #B088F9;
    color: white;
    border: none;
    padding: 0.6em 2em;
    border-radius: 30px;
    font-size: 1em;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #A16AE8;
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html = True)
@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}
div, h1, h2, p {
  animation: fadeIn 1.5s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOTTIE ANIMATION --------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_flower = load_lottie("https://assets10.lottiefiles.com/packages/lf20_hbr24nwy.json")

# -------------------- SIDEBAR NAV --------------------
st.sidebar.header("☁️ Menu")
page = st.sidebar.radio("", ["🏠 Home", "🧘 Take Quiz", "🌿 About"])

# -------------------- HOME PAGE --------------------
if page == "🏠 Home":
    st.markdown("<h1>🌸 ScentSense</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Discover your personalized stress-relief scent</h3>", unsafe_allow_html=True)
    st_lottie(lottie_flower, height=250, key="flower")

    st.write("""
    Welcome to **ScentSense**, your personal aromatherapy companion.  
    Answer a few reflective questions, and we’ll match you with the scent  
    that helps you unwind, recharge, and feel your calmest self.
    """)
    st.divider()
    st.info("✨ Tip: Take the quiz in a quiet space for the best experience.")

# -------------------- QUIZ PAGE --------------------
elif page == "🧘 Take Quiz":
    st.markdown("<h1>🧘 Find Your Calming Scent</h1>", unsafe_allow_html=True)
    st.write("Let's discover what scent soothes *your* stress the best.")

    # Quiz Questions
    mood = st.radio("How do you usually feel after a stressful day?",
                    ["Tired and drained", "Restless and anxious", "Sad or heavy", "Irritable or tense"])

    env = st.radio("Which environment feels most relaxing to you?",
                   ["Beach", "Forest", "Spa", "Garden", "Mountains"])

    scent_pref = st.radio("Which type of smell do you usually enjoy?",
                          ["Floral", "Woody", "Citrus", "Herbal", "Sweet"])

    activity = st.radio("What do you do to unwind?",
                        ["Read or journal", "Walk outdoors", "Listen to music", "Meditate", "Sleep"])

    st.divider()

    if st.button("✨ Show My Calming Scent"):
        # Very simple scent matching logic (you can replace with your model)
        if scent_pref == "Floral" or env == "Garden":
            scent = "Lavender"
            desc = "Lavender calms anxiety and improves sleep quality."
        elif scent_pref == "Citrus" or env == "Beach":
            scent = "Bergamot"
            desc = "Bergamot uplifts your spirit and reduces fatigue."
        elif scent_pref == "Woody" or env == "Forest":
            scent = "Sandalwood"
            desc = "Sandalwood grounds emotions and promotes inner peace."
        elif scent_pref == "Herbal":
            scent = "Eucalyptus"
            desc = "Eucalyptus refreshes your mind and clears tension."
        else:
            scent = "Vanilla"
            desc = "Vanilla comforts your mood and creates warmth."

        st.markdown(f"""
        <div style='background-color:#E5D4ED; border-radius:20px; padding:30px; text-align:center;'>
            <h2 style='color:#6D2E46;'>🌿 Your Stress-Relief Scent: <span style='color:#A16AE8;'>{scent}</span></h2>
            <p style='font-size:18px;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("💬 Save this recommendation and try diffusing it in your room tonight.")

# -------------------- ABOUT PAGE --------------------
elif page == "🌿 About":
    st.markdown("<h1>🌿 About ScentSense</h1>", unsafe_allow_html=True)
    st.write("""
    **ScentSense** blends the science of aromatherapy with personal reflection.  
    Each quiz response helps us understand your emotional landscape,  
    guiding you to the scent family that brings balance and serenity.

    🌸 Built with **Streamlit**, designed for mindfulness and personalization.  
    """)

    st.markdown("""
    <div style='text-align:center; font-style:italic; margin-top:40px;'>
    “Peace begins the moment you take a deep breath.” 🌷
    </div>
    """, unsafe_allow_html=True)
