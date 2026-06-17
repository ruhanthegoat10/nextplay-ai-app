import streamlit as st
import random
import hashlib

# -------------------------
# 1. PREMIUM GLASSMORPHISM CANVAS & STYLING
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background: #030307; }
    .main-title { 
        text-align: center; color: #ffffff; font-size: 3.2rem; 
        font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; 
        font-family: 'Inter', sans-serif; 
    }
    .sub-title { 
        text-align: center; color: #a855f7; font-size: 1.05rem; 
        font-weight: 700; text-transform: uppercase; letter-spacing: 0.25em; 
        margin-bottom: 45px; 
    }
    .chat-container { max-width: 800px; margin: 0 auto; padding: 10px; }
    .user-bubble { 
        background: #16192b; border: 1px solid #2e3556; padding: 16px 20px; 
        border-radius: 16px; color: #f1f5f9; font-size: 1.05rem; 
        margin-bottom: 20px; margin-left: 10%; box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
    }
    .ai-bubble { 
        background: linear-gradient(135deg, #0d0e1a 0%, #121324 100%); 
        border-left: 4px solid #a855f7; border-top: 1px solid #1e213d; 
        border-right: 1px solid #1e213d; border-bottom: 1px solid #1e213d; 
        padding: 22px; border-radius: 16px; color: #e2e8f0; 
        font-size: 1.05rem; line-height: 1.65; margin-bottom: 20px; margin-right: 10%; 
    }
    .score-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(168, 85, 247, 0.15);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .badge {
        display: inline-block;
        padding: 3px 9px;
        border-radius: 5px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .badge-live { background: #ef4444; color: white; }
    .badge-final { background: #3b82f6; color: white; }
    .badge-scheduled { background: #10b981; color: white; }
    .badge-alert { background: #f59e0b; color: white; }
    div[data-testid='stForm'] { border: none !important; padding: 0 !important; background: transparent !important; }
</style>
""", unsafe_allow_html=True)

if "nexus_history" not in st.session_state:
    st.session_state.nexus_history = []

# -------------------------
# 2. APP LOGO & HEADER
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
st.markdown("<div class='sub-title'>Ultimate Omni-Sport Quantum Matrix</div>", unsafe_allow_html=True)

# -------------------------
# 3. INTERACTIVE CHIP SELECTION COLUMNS
# -------------------------
st.markdown("<div style='max-width: 800px; margin: 0 auto 20px auto;'>", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
quick_query = None

with c1:
    if st.button("🏆 World Cup", use_container_width=True): quick_query = "World Cup matches"
with c2:
    if st.button("⚾ MLB Board", use_container_width=True): quick_query = "MLB Baseball update"
with c3:
    if st.button("🏎️ Formula 1", use_container_width=True): quick_query = "Formula 1 standings"
with c4:
    if st.button("🔮 Predictor", use_container_width=True): quick_query = "Predict match analytics"
with c5:
    if st.button("📊 Fantasy Scout", use_container_width=True): quick_query = "Scout reports fantasy analytics"
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 4. CHAT CANVAS FEED
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay Core Engine:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 5. GENERATIVE PSEUDO-LLM RESPONSE CORE
# -------------------------
def generate_conversational_sports_quote(user_text):
    subjects = ["tactical baseline", "offensive distribution index", "defensive shape rotation", "transitional matrix acceleration"]
    verbs = ["re-aligns premium roster assets against", "neutralizes high-volume threat channels inside", "optimizes efficiency tracking variables for", "outpaces legacy tactical formations facing"]
    trends = ["high-pressing counter-attack thresholds.", "advanced floor-spacing layouts.", "split-safety defensive coverages.", "under-lapping full-back configurations."]
    
    seed = int(hashlib.md5(user_text.encode('utf-8')).hexdigest(), 16)
    random.seed(seed)
    
    sub = random.choice(subjects)
    vrb = random.choice(verbs)
    trnd = random.choice(trends)
    rating = round(random.uniform(1.1, 1.9), 2)
    
    # Using a raw string r""" here stops any backslash-t syntax escape problems dead in their tracks!
    return r"""### 🧠 NextPlay Cognitive Synthesis Analysis
    
*"Analyzing your strategic inquiry regarding: '{0}'..."*

Our live intelligence tracking platform notes that the current **{1}** dynamically **{2}** modern **{3}** 📊 **Advanced Performance Index:**
* **Synergy Index Rating:** $\sigma = {4}$
* **Tactical Conversion Efficiency:** $94.6\%$
* **Scouting Consensus Vector:** Highly volatile upper-tier roster depth allocation recommended.

*Type 'MLB', 'NBA', 'Formula 1', 'Predict', or 'Scout' to view deep-dive targeted data feeds!*""".format(user_text, sub, vrb, trnd, rating)

# -------------------------
# 6. MASTER DATA FEED LAYER
# -------------------------
def process_sports_query(user_input):
    inp = user_input.lower()
    
    if "predict" in inp or "probability" in inp or "odds" in inp:
        return r"""### 🔮 Quantum Predictive Projections Engine

<div class='score-card'>
<span class='badge badge-alert'>📈 WIN PROBABILITY MARGINS</span><br>
⚽ <b>England vs Croatia</b> (Group L)<br>
* **England Win Odds:** $54.2\%$ | **Croatia Win Odds:** $21.8\%$ | **Draw Index:** $24.0\%$
* **Expected Goals Formats:** $X_G = 1.64$ vs $0.92$
</div>

<div class='score-card'>
<span class='badge badge-alert'>📈 TOTALS OVER/UNDER</span><br>
⚾ <b>Yankees vs White Sox</b><br>
* **Projected Run Limits:** $8.5$ runs (Confidence coefficient: $88\%$)
* **Starting Pitcher Strikeout Line:** $K_{\text{proj}} = 7.4$ across $6.1$ innings.
</div>"""

    elif "scout" in inp or "fantasy" in inp or "stats" in inp:
        return r"""### 📊 Fantasy Metrics & Waiver Scout Panels

<div class='score-card'>
<span class='badge badge-scheduled'>💎 HIGH-VALUE WAIVER TARGET</span><br>
🏀 **Advanced Floor-Spacing Index Formulas**<br>
* **Efficiency Indicator:** Effective Field Goal Percentage metric calculated as:
$$eFG\% = \frac{\text{Field Goals Made} + 0.5 \times \text{3PM}}{\text{Field Goal Attempts}}$$
* **Scout Verdict:** Roster additions flashing an $eFG\% > 58.5\%$ in transition sets are highly prioritized.
</div>"""

    elif any(x in inp for x in ["f1", "formula", "race", "grand"]):
        return """### 🏎️ Formula 1 Championship Leaderboards (2026)

<div class='score-card'>
<span class='badge badge-live'>🟢 SEASON STANDINGS ACTIVE</span><br>
🏁 <b>1. Max Verstappen (Red Bull Racing)</b> — 184 pts<br>
🏁 <b>2. Charles Leclerc (Ferrari)</b> — 156 pts<br>
🏁 <b>3. Lando Norris (McLaren)</b> — 142 pts
</div>

<div class='score-card'>
📊 **Technical Metrics:**
* **Aero-Efficiency Coefficient:** McLaren holding marginal speed gains in medium-speed downforce layouts.
* **Tire Degradation Index:** Ferrari displaying improved thermal tracking properties across long tire stints.
</div>"""

    elif any(x in inp for x in ["baseball", "mlb", "yankees", "dodgers"]):
        return """### ⚾ MLB Real-Time Scoreboards (June 17, 2026)

<div class='score-card'>
<span class='badge badge-final'>🏁 FINAL</span><br>
🔥 <b>Miami Marlins 12 - 4 Philadelphia Phillies</b><br>
⏱️ Game Complete | Venue: Citizens Bank Park, Pennsylvania
</div>

<div class='score-card'>
<span class='badge badge-live'>🟢 IN PROGRESS (7th Inning)</span><br>
🔥 <b>Houston Astros 4 - 1 Detroit Tigers</b><br>
⏱️ Live Broadcast | Venue: Daikin Park, Texas
</div>"""

    elif any(x in inp for x in ["nba", "basketball", "knicks", "spurs"]):
        return """### 🏀 NBA Championship Finals Summary (June 2026)

<div class='score-card'>
<span class='badge badge-final'>🏆 SERIES COMPLETE</span><br>
👑 <b>New York Knicks (4) - (1) San Antonio Spurs</b><br>
⏱️ **Result:** The Knicks capture the NBA title, ending a 53-year wait.
🏅 **Finals MVP:** Jalen Brunson
</div>"""

    elif any(x in inp for x in ["world cup", "matches", "soccer", "scores", "portugal"]):
        return """### 🏆 World Cup 2026 Live Match Center (June 17, 2026)

<div class='score-card'>
<span class='badge badge-final'>🏁 FINAL OUTCOME</span><br>
⚽ <b>Portugal 1 - 1 DR Congo</b> (Group K)<br>
⏱️ Venue: Houston Stadium, Texas
</div>

<div class='score-card'>
<span class='badge badge-scheduled'>⏳ KICKING OFF SOON</span><br>
⚽ <b>England vs Croatia</b> (Group L)<br>
⏱️ Time: 4:00 PM ET / 1:00 PM PT | Venue: Dallas Stadium, Texas
</div>"""

    else:
        return generate_conversational_sports_quote(user_input)

# -------------------------
# 7. INPUT FLOW LOGIC
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask about F1, MLB, World Cup, or chat freely with the sports engine...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ DEPLOY QUANTUM PIPELINE EXTRACTION", use_container_width=True)

active_input = user_query if (submit_button and user_query) else quick_query

if active_input:
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    ai_response = process_sports_query(active_input)
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
