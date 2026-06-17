import streamlit as st
import time
import random
import re

# -------------------------
# 1. PREMIUM GLASSMISM CANVAS & STYLING
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

# Custom premium chat portal styling
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
# 4. HUMANIZED ANALYSIS ENGINE (CURRENT EVENTS ROUTER)
# -------------------------
def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    inp_title = user_input.title()
    
    # Isolate entity names smoothly using regex
    words = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', inp_title)
    ignore_list = ["Vs", "And", "What", "The", "Analyze", "Predict", "Score", "In", "Simulation", "Tactics", "Run", "Me", "Game", "Will", "Be", "World", "Cup", "Transfer", "Sign", "Player", "Injury", "Injured"]
    found_entities = [w for w in words if w not in ignore_list]
    
    t1 = found_entities[0] if len(found_entities) > 0 else "The Favorites"
    t2 = found_entities[1] if len(found_entities) > 1 else "The Underdogs"

    # --- NODE A: TRANSFERS & SQUAD MOVEMENTS ---
    if "transfer" in inp_lower or "sign" in inp_lower or "joined" in inp_lower or "move to" in inp_lower:
        player = found_entities[0] if len(found_entities) > 0 else "their target player"
        team = found_entities[1] if len(found_entities) > 1 else "the club"
        
        response = f"""### 📰 Real-Time Transfer Strategy Analysis

This move completely reshapes the tactical layout. If **{player}** officially slots into **{team}**, it solves an immediate problem for them in terms of creation efficiency. 

From a tactical perspective, it's a huge upgrade, but it means their manager will have to shift their current pressing system to accommodate his defensive work rate. If they pull it off, their offensive ceiling goes up significantly for next season, making them direct title contenders."""
        return response

    # --- NODE B: WORLD CUP / TOURNAMENTS ---
    elif "world cup" in inp_lower or "cup" in inp_lower or "euro" in inp_lower or "copa" in inp_lower:
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        
        verdict_text = f"Given the high stakes of tournament knockout pressure, expect a very cagey match. But I see **{winner}** unlocking the defense late in the second half." if winner != "Draw" else "Both national squads are defensively elite. Expect a long, tactical chess match that likely heads to extra time or a draw in group stages."
        
        response = f"""### 🏆 International Tournament Analysis: {t1} vs {t2}

Tournament football is a completely different beast than club football. There’s zero room for error, especially on the big stage like the World Cup. **{t1}** has the tournament experience, but **{t2}** brings insane high-intensity energy that can catch organized backlines off guard. 

---

🔮 **Predicted Final Score:** {t1} **{s1} - {s2}** {t2}
**Tournament Verdict:** {verdict_text}"""
        return response

    # --- NODE C: INJURIES & SQUAD UPDATES ---
    elif "injury" in inp_lower or "injured" in inp_lower or "out for" in inp_lower:
        key_player = found_entities[0] if len(found_entities) > 0 else "their star player"
        
        response = f"""### 🏥 Injury Impact Scouting Report

Losing **{key_player}** changes everything for this upcoming stretch. He's the focal point of transition play, so without him, the team is going to look much more predictable going forward. 

Expect the coaching staff to play a more conservative mid-block to shield the defense until he returns. Other players will get their chance to step up, but their overall fluidity takes a massive hit here."""
        return response

    # --- NODE D: STANDARD BASKETBALL ---
    elif any(x in inp_lower for x in ["nba", "basketball", "lakers", "celtics", "hoops", "warriors", "nuggets"]):
        s1, s2 = random.randint(104, 122), random.randint(104, 122)
        winner = t1 if s1 > s2 else t2
        
        response = f"""### 🏀 Match Analysis: {t1} vs {t2}

This one is going to be won or lost beyond the arc. If **{t1}** can't contain the pick-and-roll switches, **{t2}** will just generate open look after open look. Watch out for secondary fast breaks—whoever controls the glass and limits turnovers wins the night.

---

🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}
**Quick Verdict:** Expect a close game, but **{winner}** clutches it with better free-throw execution in crunch time."""
        return response

    # --- NODE E: STANDARD SOCCER / GENERAL FALLBACK ---
    else:
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        verdict = f"**{winner}** looks slightly more balanced in mid-week form, giving them the edge." if winner != "Draw" else "Both teams match up too closely right now. A high-scoring draw feels highly probable."
        
        response = f"""### 📋 Match Analysis: {t1} vs {t2}

This is a massive tactical matchup. **{t1}** is going to want to dictate the tempo and build slowly from the back, but that opens up giant structural windows for **{t2}** to exploit on quick, direct counter-attacks out wide. 

---

🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}
**Quick Verdict:** {verdict}"""
        return response

# -------------------------
# 5. CONVERSATIONAL FIELD INPUT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask anything! 'Mbappe transfer to Real Madrid', 'World Cup match', or injuries...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Modern UI Suggestion Tags
st.markdown("<p style='color: #4b5563; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 25px; margin-bottom: 12px;'>Suggested Prompts</p>", unsafe_allow_html=True)
chip_col1, chip_col2, chip_col3 = st.columns(3)

active_input = None

with chip_col1:
    if st.button("🏆 Predict Argentina vs Portugal in the World Cup", use_container_width=True):
        active_input = "Predict Argentina vs Portugal in the World Cup"
with chip_col2:
    if st.button("🔄 Analyze Haaland transferring to Real Madrid", use_container_width=True):
        active_input = "Analyze Haaland transferring to Real Madrid"
with chip_col3:
    if st.button("🏥 Analyze how the injury affects the team", use_container_width=True):
        active_input = "Analyze how the injury affects the team"

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
st.caption("NextPlay AI Nexus • Version 15.2 Contextual Event Processing Hub")
