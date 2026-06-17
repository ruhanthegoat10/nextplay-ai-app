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
# 4. CURRENT EVENTS & CONTEXT INTELLIGENCE ROUTER
# -------------------------
def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    inp_title = user_input.title()
    
    # Isolate capitalized team/player terms out of text strings
    words = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', inp_title)
    ignore_list = ["Vs", "And", "What", "The", "Analyze", "Predict", "Score", "In", "Simulation", "Tactics", "Run", "Me", "Game", "Will", "Be", "World", "Cup", "Transfer", "Sign", "Player"]
    found_entities = [w for w in words if w not in ignore_list]
    
    t1 = found_entities[0] if len(found_entities) > 0 else "The Favorites"
    t2 = found_entities[1] if len(found_entities) > 1 else "The Underdogs"

    # --- ROUTER NODE 1: TRANSFERS / RECENT SIGNINGS ---
    if "transfer" in inp_lower or "sign" in inp_lower or "joined" in inp_lower:
        player_name = found_entities[0] if len(found_entities) > 0 else "their new marquee signing"
        destination_team = found_entities[1] if len(found_entities) > 1 else "their squad"
        
        breakdown = f"""This transfer completely shifts the competitive landscape. Integrating **{player_name}** into **{destination_team}** changes how they will approach their transition play. Structurally, it relieves pressure from their primary creators, but it poses immediate chemistry questions. 
        
        Historically, introducing a high-profile asset mid-cycle temporarily compromises defensive pressing structures while tactical adjustments are finalized, but their offensive expected ceiling just spiked dramatically."""
        
        prediction = f"""🔄 **Roster Update Verdict:** If **{player_name}** is deployed in a fluid, advanced position rather than a rigid central channel, expect **{destination_team}**'s offensive output efficiency to increase by an estimated 15-20% over their upcoming matches."""
        
        return f"### 📰 Real-Time Transfer Impact Analysis\n\n{breakdown}\n\n---\n\n{prediction}"

    # --- ROUTER NODE 2: INTERNATIONAL TOURNAMENTS (WORLD CUP / EUROS) ---
    elif "world cup" in inp_lower or "cup" in inp_lower or "national" in inp_lower:
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        
        breakdown = f"""International tournament football hits entirely different than league play. In a tournament setting like the World Cup, **{t1}** and **{t2}** don't have the luxury of season-long error margins. **{t1}** will likely run a highly protective mid-block to mitigate individual fatigue, whereas **{t2}** will rely on set-pieces and vertical transitions to force mistakes."""
        
        if winner == "Draw":
            verdict_text = "Given the high stakes of knockout or group stage pressure, expect both teams to play it safe. A calculated draw feels highly realistic."
        else:
            verdict_text = f"The depth of **{winner}**'s bench will likely break the game wide open in the final 20 minutes under tournament fatigue."
            
        prediction = f"""🏆 **World Cup Predicted Score:** {t1} **{s1} - {s2}** {t2}

**Tournament Verdict:** {verdict_text}"""
        
        return f"### 🌍 International Tournament Vector: {t1} vs {t2}\n\n{breakdown}\n\n---\n\n{prediction}"

    # --- ROUTER NODE 3: NBA / BASKETBALL ---
    elif any(x in inp_lower for x in
