import streamlit as st
import time
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

# Unified style injection block
st.markdown("""
<style>
    .stApp { 
        background: #030307; 
    }
    .main-title { 
        text-align: center; 
        color: #ffffff; 
        font-size: 3.2rem; 
        font-weight: 900; 
        letter-spacing: -0.05em; 
        margin-bottom: 5px; 
        font-family: 'Inter', sans-serif; 
    }
    .sub-title { 
        text-align: center; 
        color: #a855f7; 
        font-size: 1.05rem; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.25em; 
        margin-bottom: 45px; 
    }
    .chat-container { 
        max-width: 800px; 
        margin: 0 auto; 
        padding: 10px; 
    }
    .user-bubble { 
        background: #16192b; 
        border: 1px solid #2e3556; 
        padding: 16px 20px; 
        border-radius: 16px; 
        color: #f1f5f9; 
        font-size: 1.05rem; 
        margin-bottom: 20px; 
        margin-left: 10%; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
    }
    .ai-bubble { 
        background: linear-gradient(135deg, #0d0e1a 0%, #121324 100%); 
        border-left: 4px solid #a855f7; 
        border-top: 1px solid #1e213d; 
        border-right: 1px solid #1e213d; 
        border-bottom: 1px solid #1e213d; 
        padding: 22px; 
        border-radius: 16px; 
        color: #e2e8f0; 
        font-size: 1.05rem; 
        line-height: 1.65; 
        margin-bottom: 20px; 
        margin-right: 10%; 
    }
    div[data-testid='stForm'] { 
        border: none !important; 
        padding: 0 !important; 
        background: transparent !important; 
    }
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
# 4. ROBUST MULTI-SPORT COGNITIVE MATRIX
# -------------------------
def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    
    # Intelligently clean up punctuation for keyword scanning
    clean_input = re.sub(r'[^\w\s]', '', inp_lower)
    words = clean_input.split()

    # Dynamic Entity Extractor with deep filtering list
    ignore_words = {
        "vs", "and", "what", "the", "analyze", "predict", "score", "in", "right", "now",
        "simulation", "tactics", "run", "me", "game", "will", "be", "world", "cup", 
        "transfer", "sign", "player", "injury", "injured", "is", "are", "was", "were", 
        "does", "do", "did", "can", "could", "should", "how", "who", "why", "when", 
        "where", "playing", "match", "happening", "today", "tonight", "this", "week", "about"
    }
    
    # Extract candidate nouns/teams that aren't functional words
    entities = [w.title() for w in words if w not in ignore_words]
    
    # Assign names safely based on what was parsed
    t1 = entities[0] if len(entities) > 0 else "The Favorites"
    t2 = entities[1] if len(entities) > 1 else "The Underdogs"
    
    # Unbreakable check: if regex breaks or extracts twin words, assign distinct labels
    if t1 == t2:
        if t1 == "The Favorites":
            t2 = "The Underdogs"
        else:
            t2 = "Their Rivals"

    # --- CATEGORY 1: TRANSFERS & MARKET ---
    if any(x in inp_lower for x in ["transfer", "sign", "joined", "move to", "market", "rumor"]):
        player = entities[0] if len(entities) > 0 else "Target Player"
        destination = entities[1] if len(entities) > 1 else "Prospective Club"
        return f"""### 📰 Live Transfer Window Analysis

This market move completely alters the squad blueprint. If **{player}** officially seals a move to **{destination}**, it resolves an immediate structural puzzle regarding depth and technical flexibility.

From an analytical standpoint, it’s a massive functional upgrade. However, it means the coaching staff will have to modify their baseline tactical systems to preserve team balance. If the pieces fall into place, their project shifts directly into title-contender status."""

    # --- CATEGORY 2: INJURIES & SQUAD DELETIONS ---
    elif any(x in inp_lower for x in ["injury", "injured", "out for", "torn", "hamstring", "acl", "status"]):
        key_player = entities[0] if len(entities) > 0 else "Key Starter"
        return f"""### 🏥 Injury Impact Scouting Report

Losing **{key_player}** sends immediate structural adjustments through the entire tactical layout. As a foundational piece of their transition sequences, losing this asset means the current system risks looking a bit too static going forward.

Expect the managerial staff to rely heavily on a compact defensive shape to shelter the backline while they wait for reinforcements to return from the medical room."""

    # --- CATEGORY 3: INTERNATIONAL TOURNAMENTS (WORLD CUP / COPA / EURO) ---
    elif any(x in inp_lower for x in ["world cup", "cup", "euro", "copa", "international"]):
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        verdict = f"**{winner}** possesses cleaner structural flexibility in mid-tournament formats, giving them the ultimate nod." if winner != "Draw" else "Both national sides display elite positional awareness. Expect a tight tactical block battle ending in a stalemate."
        
        return f"""### 🏆 Tournament Scouting Layer: {t1} vs {t2}

International knockout football represents a unique competitive challenge. With tight schedules and absolute focus on single-elimination stakes, mistakes are magnified instantly under the global spotlight.

---

🔮 **Projected Scoreline:** {t1} **{s1} - {s2}** {t2}
**Tournament Verdict:** {verdict}"""

    # --- CATEGORY 4: BASKETBALL (NBA / COLLEGE) ---
    elif any(x in inp_lower for x in ["nba", "basketball", "hoops", "lakers", "celtics", "warriors", "nuggets"]):
        s1, s2 = random.randint(102, 124), random.randint(102, 124)
        winner = t1 if s1 > s2 else t2
        return f"""### 🏀 Elite Hoops Analytics: {t1} vs {t2}

This matchup will dictate itself purely along perimeter defense and secondary shot creation. If **{t1}** struggles to limit clean catch-and-shoot packages from deep, **{t2}** will simply stretch the floor and control the tempo.

---

🔮 **Simulated Score:** {t1} **{s1} - {s2}** {t2}
**Analytical Verdict:** Expect a heavy run-and-gun affair, but **{winner}** edges execution out inside the final two minutes."""

    # --- CATEGORY 5: AMERICAN FOOTBALL (NFL / NCAAF) ---
    elif any(x in inp_lower for x in ["nfl", "football", "super bowl", "touchdown", "quarterback", "chiefs"]):
        s1, s2 = random.choice([17, 20, 24, 27, 31]), random.choice([14, 21, 24, 28, 35])
        winner = t1 if s1 > s2 else t2
        return f"""### 🏈 Gridiron Tactical Breakdown: {t1} vs {t2}

Victory here is completely contingent upon line-of-scrimmage control and forcing early safety commitments. If **{t1}** establishes their zone-run scheme efficiently, it will open up deep play-action avenues over the middle against **{t2}**'s standard sub-packages.

---

🔮 **Simulated Gridiron Score:** {t1} **{s1} - {s2}** {t2}
**Analytical Verdict:** A pure war of trenches, but **{winner}** features the defensive discipline needed to secure crucial turnovers."""

    # --- CATEGORY 6: BASEBALL (MLB) ---
    elif any(x in inp_lower for x in ["mlb", "baseball", "yankees", "dodgers", "innings", "pitcher"]):
        s1, s2 = random.randint(2, 8), random.randint(2, 8)
        if s1 == s2: s1 += 1 # Avoid baseball ties
        winner = t1 if s1 > s2 else t2
        return f"""### ⚾ Diamond Metrics & Analytics: {t1} vs {t2}

This matchup settles entirely on starting rotation durability and bullpen match-ups through the middle frames. If **{t2}** struggles to pick up breaking balls early in the count, expect **{t1}**'s top-of-the-order hitters to apply pressure quickly on the basepaths.

---

🔮 **Simulated MLB Line Score:** {t1} **{s1} - {s2}** {t2}
**Analytical Verdict:** Pitching changes will tell the story, but **{winner}** holds the run-differential advantage here."""

    # --- CATEGORY 7: HOCKEY (NHL) ---
    elif any(x in inp_lower for x in ["nhl", "hockey", "crease", "puck", "skate"]):
        s1, s2 = random.randint(1, 5), random.randint(1, 5)
        if s1 == s2: s1 += 1
        winner = t1 if s1 > s2 else t2
        return f"""### 🏒 Ice Level Performance Matrix: {t1} vs {t2}

Power play conversion rates and neutral zone turnovers are going to define the pace of this match. If **{t1}** can establish a heavy forecheck and crowd the blue line, they'll choke out **{t2}**'s transition lanes before they ever reach the attacking zone.

---

🔮 **Projected Final:** {t1} **{s1} - {s2}** {t2}
**Analytical Verdict:** High physical velocity expected, with **{winner}** converting late on an advantage window."""

    # --- CATEGORY 8: GENERAL SPORT / SOCCER FALLBACK ---
    else:
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        verdict = f"**{winner}** displays sharper collective performance loops right now, providing the winning margin." if winner != "Draw" else "These operations mirror each other structural-wise. A balanced drawn match feels inevitable."
        
        return f"""### 📋 General Performance Summary: {t1} vs {t2}

An extremely close operational matchup on paper. One side will seek to establish possession hegemony and build sequences progressively from deep layout positions, while the other looks to maximize vertical counters into wide channels.

---

🔮 **Simulated Output:** {t1} **{s1} - {s2}** {t2}
**Quick Verdict:** {verdict}"""

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
st.caption("NextPlay AI Nexus • Version 17.0 Universal Sports Intelligence Stack")
