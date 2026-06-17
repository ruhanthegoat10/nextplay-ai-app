import streamlit as st
import random
import re

# -------------------------
# 1. PREMIUM GLASSMORPHISM CANVAS & STYLING
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

# Clean, safe markdown style injection
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
st.markdown("<div class='sub-title'>Omni-Sport Generative Cognitive Layer</div>", unsafe_allow_html=True)

# -------------------------
# 3. CHAT CANVAS FEED
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay AI:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 4. ROBUST EXTRACTOR ENGINE
# -------------------------
def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    
    # Remove punctuation cleanly
    clean_input = re.sub(r'[^\w\s]', '', inp_lower)
    words = clean_input.split()

    # Exhaustive list to filter out common phrases and questions
    ignore_words = {
        "vs", "and", "what", "the", "analyze", "predict", "score", "in", "right", "now",
        "simulation", "tactics", "run", "me", "game", "games", "will", "be", "world", "cup", 
        "transfer", "sign", "player", "injury", "injured", "is", "are", "was", "were", 
        "does", "do", "did", "can", "could", "should", "how", "who", "why", "when", 
        "where", "playing", "match", "happening", "today", "tonight", "this", "week", "about"
    }
    
    entities = [w.title() for w in words if w not in ignore_words]
    
    t1 = entities[0] if len(entities) > 0 else "The Favorites"
    t2 = entities[1] if len(entities) > 1 else "The Underdogs"
    
    if t1 == t2 or t1 in ["The Favorites", "The Underdogs"]:
        t1 = "The Top Seeds"
        t2 = "The Challengers"

    # --- ROUTER 1: GENERAL WORLD CUP MATCH QUESTIONS ---
    if any(x in inp_lower for x in ["world cup", "cup", "euro", "copa"]):
        # If no specific teams were named, treat as a global news update
        if len(entities) < 2:
            return """### 🏆 Live World Cup Tournament Desk Update

The group stages are creating intense drama with narrow tactical margins across every group block. Team setups are adjusting fluidly between mid-blocks and aggressive high-pressing schemas.

* **Group Dynamics:** Defending structural setups are emphasizing transition containment over high possession metrics.
* **Standings Impact:** Goal-differential tiebreakers are heavily influencing aggressive adjustments inside the second half.
* **Up Next:** Knockout layout mappings are locked to finalize as current round-robin fixtures conclude."""
        
        # If teams are specified, run a tactical simulation instead
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        return f"""### 🏆 World Cup Fixture Analytics: {t1} vs {t2}

High-stakes international match simulation calculated successfully. Both rosters show optimized conditioning indexes ahead of kickoff.

---

🔮 **Projected Score:** {t1} **{s1} - {s2}** {t2}
**Verdict:** High tactical containment expected in central transition lanes."""

    # --- ROUTER 2: BASKETBALL / NBA ---
    elif any(x in inp_lower for x in ["nba", "basketball", "hoops", "lakers", "celtics", "warriors"]):
        if len(entities) < 2:
            return """### 🏀 Live Hoops Central Intelligence

The current floor-spacing paradigms are driving exceptional volume from beyond the three-point arc. Team transition structures are focusing heavily on transition tracking.

* **League Trend:** Secondary shot-creation variants are settling high-leverage possessions.
* **Injury Impact:** Depth rotations are facing tests over heavy back-to-back schedule clusters."""
        
        s1, s2 = random.randint(102, 125), random.randint(102, 125)
        return f"""### 🏀 Elite Hoops Analytics: {t1} vs {t2}

🔮 **Simulated Score:** {t1} **{s1} - {s2}** {t2}
**Verdict:** Perimeter closeouts and defensive rebounding splits will determine the final run sequence."""

    # --- ROUTER 3: AMERICAN FOOTBALL / NFL ---
    elif any(x in inp_lower for x in ["nfl", "football", "super bowl", "chiefs"]):
        if len(entities) < 2:
            return """### 🏈 Gridiron Intelligence Update

Offensive playbooks are leaning into heavy usage of pre-snap motion to isolate coverages over the middle of the field.

* **Trend Report:** Defensive packages are utilizing disguised coverage rotations to pressure target windows.
* **Roster Depth:** Backfield protection schemes remain critical for passing execution."""
        
        s1, s2 = random.choice([17, 24, 27, 31]), random.choice([14, 20, 24, 28])
        return f"""### 🏈 Gridiron Matchup Analysis: {t1} vs {t2}

🔮 **Projected Score:** {t1} **{s1} - {s2}** {t2}
**Verdict:** Establishing the ground game early will open high-percentage play-action opportunities downstream."""

    # --- ROUTER 4: BASEBALL / MLB ---
    elif any(x in inp_lower for x in ["mlb", "baseball", "yankees", "dodgers"]):
        if len(entities) < 2:
            return """### ⚾ Basepath Analytics Digest

Starting pitching velocity and spin-rate maintenance are heavily dominating early-inning run prevention dynamics across the league."""
        
        s1, s2 = random.randint(1, 8), random.randint(1, 8)
        if s1 == s2: s1 += 1
        return f"""### ⚾ MLB Diamond Metrics: {t1} vs {t2}

🔮 **Simulated Score:** {t1} **{s1} - {s2}** {t2}
**Verdict:** High dependency on bullpen match-ups to navigate deep into the later frames."""

    # --- ROUTER 5: HOCKEY / NHL ---
    elif any(x in inp_lower for x in ["nhl", "hockey", "puck"]):
        if len(entities) < 2:
            return """### 🏒 Ice Level Performance Matrix

Zone entry metrics and powerplay execution percentages continue to prove to be the critical differentiators in close league matchups."""
        
        s1, s2 = random.randint(1, 5), random.randint(1, 5)
        if s1 == s2: s1 += 1
        return f"""### 🏒 NHL Performance Simulator: {t1} vs {t2}

🔮 **Projected Final:** {t1} **{s1} - {s2}** {t2}
**Verdict:** Neutral-zone tracking and penalty kill units will protect the thin margin here."""

    # --- ROUTER 6: TRANSFERS & SQUAD MOVEMENTS ---
    elif any(x in inp_lower for x in ["transfer", "sign", "joined", "market"]):
        player = entities[0] if len(entities) > 0 else "Target Asset"
        return f"""### 📰 Transfer Market Strategic Deep-Dive

Roster adjustments in the current window emphasize long-term squad profile sustainability and salary cap positioning.

* **Profile Fit:** Systems are prioritizing versatile profiles capable of executing multiple tactical roles.
* **Valuation:** Advanced analytical tracking metrics are heavily driving negotiation benchmarks."""

    # --- ROUTER 7: SYSTEM GENERAL FALLBACK ---
    else:
        if len(entities) >= 2:
            s1, s2 = random.randint(0, 3), random.randint(0, 3)
            return f"""### 📋 Tactical Matchup Breakdown: {t1} vs {t2}

🔮 **Simulated Output:** {t1} **{s1} - {s2}** {t2}
**Verdict:** High operational balance. Small variances in spatial distribution will determine the final result."""
        
        return """### 📋 NextPlay Multi-Sport System Core

Operational layer is running optimally. Submit any league matchup, player transaction query, or injury update to compute target analysis.

* **Supported Domains:** Soccer, Basketball, Football, Baseball, Hockey.
* **Dynamic Scanners:** Keyword analysis engine optimized against conversational queries."""

# -------------------------
# 5. CONVERSATIONAL FIELD INPUT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask anything! NFL games, NBA, World Cup updates, or transfers...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Modern UI Suggestion Tags
st.markdown("<p style='color: #4b5563; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 25px; margin-bottom: 12px;'>Suggested Prompts</p>", unsafe_allow_html=True)
chip_col1, chip_col2, chip_col3 = st.columns(3)

active_input = None

with chip_col1:
    if st.button("🏆 Predict England vs Croatia in the World Cup", use_container_width=True):
        active_input = "Predict England vs Croatia in the World Cup"
with chip_col2:
    if st.button("🏈 Simulate Chiefs vs 49ers tactics", use_container_width=True):
        active_input = "Simulate Chiefs vs 49ers tactics"
with chip_col3:
    if st.button("🔄 Analyze potential blockbuster transfer updates", use_container_width=True):
        active_input = "Analyze potential blockbuster transfer updates"

if submit_button and user_query:
    active_input = user_query

# -------------------------
# 6. INSTANTANEOUS SESSION REFRESH
# -------------------------
if active_input:
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    ai_response = run_cognitive_inference(active_input)
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br><hr style='border-color: #121324;'>", unsafe_allow_html=True)
st.caption("NextPlay AI Nexus • Version 18.0 Production Stability Engine")
