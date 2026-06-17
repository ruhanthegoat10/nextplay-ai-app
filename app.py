import streamlit as st
import numpy as np
import pandas as pd
import time
import random

# -------------------------
# 1. ENTERPRISE CANVAS SETUP
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Gen-Engine",
    page_icon="🧠",
    layout="wide"
)

# Premium Ultra-Dark Bloomberg Terminal Aesthetics
styles = [
    ".stApp { background: linear-gradient(180deg, #020205 0%, #060711 100%); }",
    ".main-title { text-align: center; color: #ffffff; font-size: 3.5rem; font-weight: 900; letter-spacing: -0.04em; margin-bottom: 0px; font-family: 'Inter', sans-serif; }",
    ".sub-title { text-align: center; color: #a855f7; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 40px; }",
    ".matrix-card { background: #090b14; padding: 25px; border-radius: 14px; border: 1px solid #1e2238; margin-bottom: 20px; }",
    ".vs-badge { text-align: center; font-size: 2.5rem; font-weight: 900; color: #1e2238; line-height: 140px; }",
    ".section-header { color: #64748b; font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 20px; }",
    ".ai-bubble { background: #0f1222; border-left: 4px solid #a855f7; padding: 20px; border-radius: 8px; color: #e2e8f0; font-size: 1.05rem; line-height: 1.6; font-family: 'Inter', sans-serif; }",
    ".telemetry-log { background: #04050b; border-left: 4px solid #a855f7; padding: 12px; border-radius: 6px; color: #a855f7; font-family: monospace; font-size: 0.85rem; margin-bottom: 8px; }",
    "div[data-baseweb='select'] { background-color: #0f1222 !important; border-radius: 8px !important; border: 1px solid #1e2238 !important; }",
    "div[data-baseweb='select'] * { color: #ffffff !important; }"
]
st.markdown(f"<style>{' '.join(styles)}</style>", unsafe_allow_html=True)

# -------------------------
# 2. AUTOMATED GLOBAL LEAGUE ARRAYS (COMPREHENSIVE)
# -------------------------
SOCCER_LEAGUES = {
    "English Premier League": [
        "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", 
        "Crystal Palace", "Everton", "Fulham", "Ipswich Town", "Leicester City", 
        "Liverpool", "Man City", "Man United", "Newcastle", "Nottingham Forest", 
        "Southampton", "Tottenham", "West Ham", "Wolves"
    ],
    "La Liga": [
        "Alaves", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Celta Vigo", 
        "Espanyol", "Getafe", "Girona", "Las Palmas", "Leganes", "Mallorca", 
        "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid", "Real Sociedad", 
        "Sevilla", "Valencia", "Valladolid", "Villarreal"
    ],
    "Serie A": [
        "Atalanta", "Bologna", "Cagliari", "Como", "Empoli", "Fiorentina", "Genoa", 
        "Inter Milan", "Juventus", "Lazio", "Lecce", "AC Milan", "Monza", "Napoli", 
        "Parma", "AS Roma", "Torino", "Udinese", "Venezia", "Verona"
    ],
    "Bundesliga": [
        "Augsburg", "Bayer Leverkusen", "Bayern Munich", "VfL Bochum", "Borussia Dortmund", 
        "Eintracht Frankfurt", "SC Freiburg", "FC Heidenheim", "TSG Hoffenheim", "Holstein Kiel", 
        "RB Leipzig", "FSV Mainz 05", "Monchengladbach", "FC St. Pauli", "VfB Stuttgart", 
        "Union Berlin", "Werder Bremen", "VfL Wolfsburg"
    ]
}

# -------------------------
# 3. INTERACTIVE GENAI INTERFACE
# -------------------------
st.sidebar.markdown("### 🧠 NEXTPLAY MODEL PARAMS")
ai_temperature = st.sidebar.slider("Creativity Context (Temperature)", 0.0, 1.0, 0.7)
model_variant = st.sidebar.selectbox("LLM Core Architecture", ["NextPlay-Gen-v4 (Default)", "NextPlay-Ultra-DeepMind"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗺️ REGIONAL CONTEXT")
sub_league_away = st.sidebar.selectbox("AWAY LEAGUE REGION", list(SOCCER_LEAGUES.keys()), key="reg_away")
sub_league_home = st.sidebar.selectbox("HOME LEAGUE REGION", list(SOCCER_LEAGUES.keys()), key="reg_home")

AWAY_TEAMS = SOCCER_LEAGUES[sub_league_away]
HOME_TEAMS = SOCCER_LEAGUES[sub_league_home]

# -------------------------
# 4. BRANDING DESIGN
# -------------------------
st.markdown("""
<div style="text-align: center; margin-top: 10px;">
    <svg width="65" height="65" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M50 5 L92 25 L92 75 L50 95 L8 75 L8 25 Z" stroke="#a855f7" stroke-width="5" fill="#04050b"/>
        <path d="M50 15 L80 45 L50 75 L20 45 Z" fill="#c084fc" opacity="0.4"/>
        <path d="M35 45 H65 M50 30 V60" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
    </svg>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='main-title'>NEXTPLAY AI GEN-ENGINE</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Generative LLM Sports Intelligence Workspace</div>", unsafe_allow_html=True)

# -------------------------
# 5. INPUT PARAMETER GRID
# -------------------------
col1, col2, col3 = st.columns([9, 2, 9])

with col1:
    st.markdown("<div class='matrix-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>🔴 AWAY OUTPOST FRANCHISE</div>", unsafe_allow_html=True)
    team_away = st.selectbox("Select Club", AWAY_TEAMS, index=0, key="sel_away")
    away_tactics = st.text_input("Tactical Bias Prompt (e.g., High Pressing, Counter)", "High Tempo Pressing Counter-Attack")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='vs-badge'>VS</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='matrix-card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>🔵 HOME OUTPOST FRANCHISE</div>", unsafe_allow_html=True)
    allowable_home = [t for t in HOME_TEAMS if t != team_away or sub_league_away != sub_league_home]
    team_home = st.selectbox("Select Club", allowable_home, index=0, key="sel_home")
    home_tactics = st.text_input("Tactical Bias Prompt (e.g., Tiki-Taka, Low Block)", "Tiki-Taka High Ball Possession Control")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='matrix-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>✍️ GLOBAL AI PROMPT INSTRUCTION OBJECTIVE</div>", unsafe_allow_html=True)
custom_prompt = st.text_area("Instruct the analyst engine on specific focus vectors:", 
                             "Analyze the midfield transitional overload. Focus deeply on xG generation via wings and defensive positional breakdowns under high fatigue environments.")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 6. DYNAMIC TEXT GENERATION ENGINE ROUTINE
# -------------------------
def generate_ai_analysis(home, away, h_tac, a_tac, user_prompt):
    # Generative thematic matrices based on tactical prompts
    scenarios = [
        f"The tactical matrix confirms a direct structural conflict between {away}'s {a_tac} schema and {home}'s structural deployment. Under the context of '{user_prompt}', computational data arrays show severe stress coordinates in the half-spaces.",
        f"Evaluating match-up nodes... {home} is utilizing hyper-compact passing channels to counter {away}'s system. Based on the user focus parameter, transition tracking indicates that defensive line mechanics will fluctuate rapidly during minute 60-75 intervals.",
        f"Generative modeling outputs show that {away}'s transitional velocity shifts the win probability index significantly if defensive rotations stall. On the other side, {home}'s {h_tac} layout creates high value expected goal clusters in central zones."
    ]
    
    conclusions = [
        f"FINAL SYSTEM EVALUATION: {home} secures tactical dominance inside the midfield engine room, creating a projected scoreline variance favoring a tight home victory or draw.",
        f"FINAL SYSTEM EVALUATION: {away}'s high intensity matrix successfully punctures the central low-block structures, shifting the ultimate simulation edge toward an away clean sheet execution."
    ]
    
    return "\n\n".join(random.sample(scenarios, 2)) + "\n\n" + random.choice(conclusions)

# -------------------------
# 7. EXECUTION TRIGGER & STREAMER
# -------------------------
if st.button("🔮 INITIALIZE DEEP GENERATIVE INFERENCE", use_container_width=True):
    st.markdown("### 📡 SYSTEM ATTENTION HEURISTICS")
    log_box = st.empty()
    
    logs = [
        f"[LLM] Activating neural attention tokens under {model_variant}...",
        f"[LLM] Parsing system configurations: {team_away} ({away_tactics}) vs {team_home} ({home_tactics})...",
        f"[LLM] Applying prompt context filters: '{user_prompt if 'user_prompt' in locals() else custom_prompt}'",
        f"[LLM] Sampling dynamic text vector streams at temperature={ai_temperature}..."
    ]
    
    curr_log_stream = []
    for log in logs:
        curr_log_stream.append(log)
        log_box.markdown("".join([f"<div class='telemetry-log'>{l}</div>" for l in curr_log_stream]), unsafe_allow_html=True)
        time.sleep(0.2)
        
    # Generate the output text dynamically
    analysis_text = generate_ai_analysis(team_home, team_away, home_tactics, away_tactics, custom_prompt)
    
    st.markdown("<div class='matrix-card' style='border-top: 4px solid #a855f7; margin-top: 15px;'>", unsafe_allow_html=True)
    st.markdown("### 🤖 NEXTPLAY GEN-AI DEEP SCOUTING ARCHIVE")
    st.markdown("---")
    
    # Text Streamer Animation to simulate native OpenAI/Gemini real-time completion
    output_container = st.empty()
    words = analysis_text.split(" ")
    streamed_text = ""
    
    for word in words:
        streamed_text += word + " "
        output_container.markdown(f"<div class='ai-bubble'>{streamed_text}█</div>", unsafe_allow_html=True)
        time.sleep(0.02)
        
    # Remove the cursor block on finish
    output_container.markdown(f"<div class='ai-bubble'>{streamed_text}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# SYSTEM FOOTER
# -------------------------
st.markdown("<br><hr style='border-color: #1e2238;'>", unsafe_allow_html=True)
st.caption("NextPlay GenAI Platform Core • Version 13.0 Generative Master Matrix • Enterprise Ecosystem")
