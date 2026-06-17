
    import streamlit as st
import time
import random

# -------------------------
# 1. ENTERPRISE CANVAS SETUP & STYLING
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

# Dark-mode styling mimicking modern premium GenAI portals
styles = [
    ".stApp { background: #030307; }",
    ".main-title { text-align: center; color: #ffffff; font-size: 3.2rem; font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; font-family: 'Inter', sans-serif; }",
    ".sub-title { text-align: center; color: #a855f7; font-size: 1.05rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.25em; margin-bottom: 45px; }",
    ".chat-container { max-width: 800px; margin: 0 auto; padding: 10px; }",
    ".user-bubble { background: #16192b; border: 1px solid #2e3556; padding: 16px 20px; border-radius: 16px; color: #f1f5f9; font-size: 1.05rem; margin-bottom: 20px; margin-left: 10%; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }",
    ".ai-bubble { background: linear-gradient(135deg, #0d0e1a 0%, #121324 100%); border-left: 4px solid #a855f7; border-top: 1px solid #1e213d; border-right: 1px solid #1e213d; border-bottom: 1px solid #1e213d; padding: 22px; border-radius: 16px; color: #e2e8f0; font-size: 1.05rem; line-height: 1.65; margin-bottom: 20px; margin-right: 10%; }",
    "div[data-testid='stForm'] { border: none !important; padding: 0 !important; background: transparent !important; }"
]
st.markdown(f"<style>{' '.join(styles)}</style>", unsafe_allow_html=True)

# Initialize Session Chat Memory History
if "nexus_history" not in st.session_state:
    st.session_state.nexus_history = []

# -------------------------
# 2. BRAND LOGO OVERLAY
# -------------------------
st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <svg width="70" height="70" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="44" stroke="#a855f7" stroke-width="4" fill="#090a14"/>
        <path d="M30 50 Q50 20 70 50 Q50 80 30 50 Z" stroke="#c084fc" stroke-width="3" fill="none"/>
        <circle cx="50" cy="50" r="6" fill="#ffffff"/>
    </svg>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='main-title'>NEXTPLAY AI NEXUS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Omni-Sport Generative Cognitive Layer</div>", unsafe_allow_html=True)

# -------------------------
# 3. CHAT DISPLAY CORE
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Render Chat History Elements
for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay AI:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 4. SPORTS REASONING ENGINE
# -------------------------
def run_cognitive_inference(user_input):
    inp = user_input.lower()
    
    # Contextual parsing responses based on keywords
    if any(x in inp for x in ["madrid", "barcelona", "soccer", "liverpool", "city", "arsenal"]):
        narratives = [
            "Analytical vector synthesis complete. My generative simulation indicates a critical tactical bottleneck in mid-tier defensive line transitions. If the high-pressing front three maintains a turnover rate above 14.2%, tactical overload heavily favors an assertive offensive victory with an expected score margin of +2 goals.",
            "Processing scouting metrics... Counter-attacking transitions are heavily weighted by recent match congestion coefficients. Expect tactical spaces to open up significantly along the wings after the 60th-minute threshold, tilting winning probabilities toward the squad utilizing dynamic wing-backs."
        ]
    elif any(x in inp for x in ["lakers", "celtics", "nba", "basketball", "bucks", "warriors"]):
        narratives = [
            "NBA predictive arrays compiled. Shot chart distribution tracking algorithms detect a heavy perimeter-reliance bias. If defensive rotations successfully protect the paint and eliminate second-chance opportunities, efficiency indexes shift, tracking a spread favorability of +6.5 points.",
            "Analyzing offensive pacing metrics... Transition tempos indicate a hyper-efficient fast-break index. True shooting percentages are modeled to hit maximum vector limits during high-screen pick-and-roll cycles tonight."
        ]
    elif any(x in inp for x in ["chiefs", "nfl", "football", "49ers"]):
        narratives = [
            "Gridiron telemetry engine online. Third-down conversion variables indicate an exploitable vulnerability against split-safety defensive shells. Generative simulation runs project tight passing windows inside the red-zone parameter.",
            "Parsing operational team data. Expected Points Added (EPA) models indicate a strong rushing efficiency curve if protection schemes maintain block assignments, forecasting an overall game-control favorability index of 58%."
        ]
    else:
        narratives = [
            "Parsing global metric datasets for your specified sports matchup framework. Generative cross-variable telemetry streams show high structural variation. The tactical execution margin remains razor-thin, with analytical nodes indicating premium performance indexes across key transition units.",
            "Global sports analytics matrix evaluated. Roster depth arrays, form vectors, and tactical layouts have been fully computed. The generative outcome matrix charts a high-probability edge toward disciplined defensive containment."
        ]
    
    return random.choice(narratives)

# -------------------------
# 5. USER CHAT INTERFACE
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask anything about any sport or matchup (e.g., 'Analyze Chelsea' or 'Lakers vs Celtics')...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Quick Action Suggestions
st.markdown("<p style='color: #4b5563; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 25px; margin-bottom: 12px;'>Suggested Prompts</p>", unsafe_allow_html=True)
chip_col1, chip_col2, chip_col3 = st.columns(3)

active_input = None

with chip_col1:
    if st.button("⚽ Predict Real Madrid vs Barcelona", use_container_width=True):
        active_input = "Predict Real Madrid vs Barcelona"
with chip_col2:
    if st.button("🏀 Run Celtics vs Lakers simulation", use_container_width=True):
        active_input = "Run Celtics vs Lakers simulation"
with chip_col3:
    if st.button("🏈 Analyze Chiefs vs 49ers metrics", use_container_width=True):
        active_input = "Analyze Chiefs vs 49ers metrics"

# If the text bar was used instead
if submit_button and user_query:
    active_input = user_query

# -------------------------
# 6. CONVERSATIONAL STATE UPDATE
# -------------------------
if active_input:
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    ai_response = run_cognitive_inference(active_input)
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br><hr style='border-color: #121324;'>", unsafe_allow_html=True)
st.caption("NextPlay AI Nexus • Version 14.1 Clean Chat Architecture")
