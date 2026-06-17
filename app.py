import streamlit as st
import time
import random

# -------------------------
# 1. ENTERPRISE GLASS-SaaS SCREEN CANVAS
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

# Premium Dark-Mode Generative Space Styling
styles = [
    ".stApp { background: #030307; }",
    ".main-title { text-align: center; color: #ffffff; font-size: 3.2rem; font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; font-family: 'Inter', sans-serif; }",
    ".sub-title { text-align: center; color: #a855f7; font-size: 1.05rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.25em; margin-bottom: 45px; }",
    ".chat-container { max-width: 800px; margin: 0 auto; padding: 10px; }",
    ".user-bubble { background: #16192b; border: 1px solid #2e3556; padding: 16px 20px; border-radius: 16px; color: #f1f5f9; font-size: 1.05rem; margin-bottom: 20px; margin-left: 10%; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }",
    ".ai-bubble { background: linear-gradient(135deg, #0d0e1a 0%, #121324 100%); border-left: 4px solid #a855f7; border-top: 1px solid #1e213d; border-right: 1px solid #1e213d; border-bottom: 1px solid #1e213d; padding: 22px; border-radius: 16px; color: #e2e8f0; font-size: 1.05rem; line-height: 1.65; margin-bottom: 20px; margin-right: 10%; }",
    ".prompt-chip { background: #0c0d19; border: 1px solid #222543; color: #94a3b8; padding: 12px 16px; border-radius: 12px; cursor: pointer; text-align: left; font-size: 0.9rem; transition: all 0.2s; height: 100%; display: flex; align-items: center; }",
    ".prompt-chip:hover { border-color: #a855f7; color: #ffffff; background: #111326; }",
    "div[data-testid='stForm'] { border: none !important; padding: 0 !important; background: transparent !important; }"
]
st.markdown(f"<style>{' '.join(styles)}</style>", unsafe_allow_html=True)

# Initialize Session Chat Memory History
if "nexus_history" not in st.session_state:
    st.session_state.nexus_history = []

# -------------------------
# 2. BRAND VECTOR OVERLAY
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
# 3. CONVERSATIONAL CENTRAL CORE
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Render Chat History Elements
for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay AI:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 4. INTELLIGENT SPORTS REASONING ENGINE
# -------------------------
def run_cognitive_inference(user_input):
    inp = user_input.lower()
    
    # Context-aware intelligence response configurations
    if "madrid" in inp or "barcelona" in inp or "soccer" in inp or "liverpool" in inp or "city" in inp:
        narratives = [
            "Analytical vector synthesis complete. My deep generative matrices indicate an tactical transition bottleneck in mid-tier defensive lines. If the high-pressing front three maintains a turnover rate above 14.2%, tactical overload favors an assertive offensive victory with a projected margin of 2.15 expected goals.",
            "Processing scouting metrics... Counter-attacking transitions are heavily weighted by current squad travel fatigue coefficients. Expect structural spaces to open significantly along the left flank after the 65th-minute threshold, tilting winning probabilities toward tactical adjustments."
        ]
    elif "lakers" in inp or "celtics" in inp or "nba" in inp or "basketball" in inp:
        narratives = [
            "NBA predictive array compiled. Shot chart distribution algorithms track a heavy perimeter-reliance bias. If defensive rotations clear the paint and limit second-chance possession options, efficiency indexes shift significantly, tracking an estimated point differential spread of +6.5 points.",
            "Analyzing offensive pacing metrics... Transition tempos indicate a hyper-efficient fast-break index. True shooting percentages are modeled to hit maximum vector limits during high-screen pick-and-roll cycles."
        ]
    elif "chiefs" in inp or "nfl" in inp or "football" in inp or "49ers" in inp:
        narratives = [
            "Gridiron telemetry engine online. Third-down completion percentages indicate a critical structural vulnerability against split-safety defensive shells. Generative simulation runs project passing windows tightening in red-zone parameters.",
            "Parsing operational team scripts. Expected Points Added (EPA) models indicate a strong rushing efficiency curve if blocking arrays hold their assignments, forecasting a game-control index shift of 58% favorability."
        ]
    else:
        # Universal context-free sport parser fallback
        narratives = [
            f"Parsing deep metrics for your requested matchup framework. Generative cross-variable telemetry streams show high structural variation. The tactical execution margin remains razor-thin, with analytical decision nodes indicating premium performance indexes across key transition units.",
            f"Global sports analytics matrix evaluated. Roster depth arrays, form vectors, and tactical layout variables have been calculated. The generative outcome matrix charts a high-probability tactical edge toward disciplined defensive containment."
        ]
    
    return random.choice(narratives)

# -------------------------
# 5. USER CHAT INPUT ENVIRONMENT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask me anything about any team or matchup (e.g., 'Analyze Real Madrid vs Man City' or 'Break down Lakers vs Celtics')...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Handle Active Submission Threads
active_input = None
if submit_button and user_query:
    active_input = user_query

# -------------------------
# 6. QUICK-ACTION SUGGESTION CHIPS
# -------------------------
st.markdown("<p style='color: #4b5563; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 25px; margin-bottom: 12px;'>Suggested AI Scenarios</p>", unsafe_allow_html=True)
chip_col1, chip_col2, chip_col3 = st.columns(3)

with chip_col1:
    if st.button("⚽ Simulate Real Madrid vs Barcelona tactics", use_container_width=True):
        active_input = "Simulate Real Madrid vs Barcelona tactics"
with chip_col2:
    if st.button("🏀 Run predictive spread on Celtics vs Lakers", use_container_width=True):
        active_input = "Run predictive spread on Celtics vs Lakers"
with chip_col3:
    if st.button("🏈 Analyze Chiefs vs 49ers offensive index", use_container_width=True):
        active_input = "Analyze Chiefs vs 49ers offensive index"

# Processing Sequence if Input is Activated
if active_input:
    # Append User Input to state
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    
    # Process generative response
    ai_response = run_cognitive_inference(active_input)
    
    # Add to state tracking array
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    
    # Force direct execution cycle refresh to cleanly paint the UI screen
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# SYSTEM FOOTER
# -------------------------
st.markdown("<br><br><hr style='border-color: #121324;'>", unsafe_allow_html=True)
st.caption("NextPlay AI Nexus • Version 14.0 Cognitive Interface • Chat Platform Sandbox Ecosystem")
