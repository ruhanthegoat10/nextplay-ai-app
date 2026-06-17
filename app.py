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
# 4. HUMANIZED CURRENT EVENTS ROUTER
# -------------------------
def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    inp_title = user_input.title()
    
    # Isolate capital letter terms smoothly using regex
    words = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', inp_title)
    ignore_list = ["Vs", "And", "What", "The", "Analyze", "Predict", "Score", "In", "Simulation", "Tactics", "Run", "Me", "Game", "Will", "Be", "World", "Cup", "Transfer", "Sign", "Player", "Injury", "Injured"]
    found_entities = [w for w in words if w not in ignore_list]
    
    t1 = found_entities[0] if len(found_entities) > 0 else "The Favorites"
    t2 = found_entities[1] if len(found_entities) > 1 else "The Underdogs"

    # --- NODE A: SQUAD TRANSFERS & MARKET MOVEMENT ---
    if any(x in inp_lower for x in ["transfer", "sign", "joined", "move to", "market"]):
        player = found_entities[0] if len(found_entities) > 0 else "their target player"
        team = found_entities[1] if len(found_entities) > 1 else "the club"
        
        response = f"""### 📰 Live Transfer Window Analysis

This market move completely alters the squad blueprint. If **{player}** officially slots into **{team}**, it resolves an immediate tactical puzzle regarding final-third efficiency. 

From an analytical standpoint, it’s a massive offensive upgrade. However, it means the coaching staff will have to modify their defensive pressing lines to preserve team balance. If they adapt quickly, their tactical ceiling points straight toward silverware next season."""
        return response

    # --- NODE B: WORLD CUP & INTERNATIONAL TOURNAMENTS ---
    elif any(x in inp_lower for x in ["world cup", "cup", "euro", "copa", "national"]):
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        
        if winner == "Draw":
            verdict_text = "Both national squads possess elite tactical structures. Expect a cagey, high-stakes tournament match where neither side leaves enough space behind, likely ending in a calculated stalemate."
        else:
            verdict_text = f"International group stages are unforgiving, but **{winner}** looks significantly more prepared to exploit transitions in the final twenty minutes."
        
        response = f"""### 🏆 World Cup Tournament Scouting Report: {t1} vs {t2}

International tournament football is an entirely different beast compared to standard club play. There is absolutely zero margin for error under the bright lights of the World Cup stage. **{t1}** relies heavily on possession-oriented control, whereas **{t2}** brings an intense mid-block counter-press capable of forcing fatal backline errors.

---

🔮 **Predicted Group Score:** {t1} **{s1} - {s2}** {t2}
**Tournament Verdict:** {verdict_text}"""
        return response

    # --- NODE C: INJURY & LINEUP DISRUPTIONS ---
    elif any(x in inp_lower for x in ["injury", "injured", "out for", "torn", "hamstring"]):
        key_player = found_entities[0] if len(found_entities) > 0 else "their star playmaker"
        
        response = f"""### 🏥 Injury Impact Report

Losing **{key_player}** sends immediate shockwaves through the tactical setup. He serves as the primary engine for transition sequences, and without his progressive distribution, the buildup play runs the risk of looking entirely too predictable.

Expect the manager to adapt by executing a much more conservative shape to shelter the defensive lines. It's a huge test of squad depth."""
        return response

    # --- NODE D: BASKETBALL / NBA ---
    elif any(x in inp_lower for x in ["nba", "basketball", "lakers", "celtics", "hoops", "warriors"]):
        s1, s2 = random.randint(104, 122), random.randint(104, 122)
        winner = t1 if s1 > s2 else t2
        
        response = f"""### 🏀 Hoops Deep-Dive: {t1} vs {t2}

This game is going to be dictated strictly out on the perimeter. If **{t1}** fails to fight over screens and close out effectively, **{t2}** is going to punish them with high-percentage looks all night long. 

---

🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}
**Quick Verdict:** A pure matchup of adjustments, but **{winner}** edges it out due to depth in secondary shot creation during crunch time."""
        return response

    # --- NODE E: STANDARD CLUB MATCHUP FALLBACK ---
    else:
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        verdict = f"**{winner}** looks slightly cleaner in mid-week fitness loops, which should provide the winning edge." if winner != "Draw" else "These clubs match up evenly on current form. A high-stakes draw feels highly realistic."
        
        response = f"""### 📋 Tactical Scouting: {t1} vs {t2}

An incredibly close tactical matchup on paper. **{t1}** will aim to dominate spatial possession and construct phases cleanly from the back, but that inevitably leaves open counter-attacking corridors out wide for **{t2}** to exploit with vertical speed.

---

🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}
**Quick Verdict:** {verdict}"""
        return response

# -------------------------
# 5. CONVERSATIONAL FIELD INPUT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask anything! 'England vs Croatia in the World Cup' or 'Alvarez transfer to Arsenal'...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Modern UI Suggestion Tags
st.markdown("<p style='color: #4b5563; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 25px; margin-bottom: 12px;'>Suggested Prompts</p>", unsafe_allow_html=True)
chip_col1, chip_col2, chip_col3 = st.columns(3)

active_input = None

with chip_col1:
    if st.button("🏆 Predict England vs Croatia in the World Cup", use_container_width=True):
        active_input = "Predict England vs Croatia in the World Cup"
with chip_col2:
    if st.button("🔄 Analyze Julian Alvarez transfer to Arsenal", use_container_width=True):
        active_input = "Analyze Julian Alvarez transfer to Arsenal"
with chip_col3:
    if st.button("🏥 Check the impact of recent squad injuries", use_container_width=True):
        active_input = "Check the impact of recent squad injuries"

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
st.caption("NextPlay AI Nexus • Version 15.5 Real-Time Sports Context Engine")
