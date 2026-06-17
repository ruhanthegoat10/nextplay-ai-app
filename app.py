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
# 4. HUMANIZED ANALYSIS ENGINE
# -------------------------
def run_cognitive_inference(user_input):
    inp = user_input.title()
    
    # Intelligently isolate team names from the text string
    words = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', inp)
    ignore_list = ["Vs", "And", "What", "The", "Analyze", "Predict", "Score", "In", "Simulation", "Tactics", "Run", "Me", "Game", "Will", "Be", "Manchester", "City"]
    found_teams = [w for w in words if w not in ignore_list]
    
    # Custom clean-up specifically for Manchester City if requested
    if "Manchester City" in user_input.title() or "Man City" in user_input.title():
        if len(found_teams) > 0 and found_teams[0] == "Liverpool":
            t1 = "Liverpool"
            t2 = "Manchester City"
        else:
            t1 = "Manchester City"
            t2 = found_teams[0] if len(found_teams) > 0 else "The Opposition"
    else:
        t1 = found_teams[0] if len(found_teams) > 0 else "The Home Team"
        t2 = found_teams[1] if len(found_teams) > 1 else "The Away Team"
    
    # Identify sport context
    inp_lower = user_input.lower()
    if any(x in inp_lower for x in ["nba", "basketball", "lakers", "celtics", "hoops", "warriors"]):
        sport = "basketball"
    elif any(x in inp_lower for x in ["nfl", "football", "chiefs", "49ers", "cowboys"]):
        sport = "american_football"
    else:
        sport = "soccer"

    # Human-like conversation responses
    if sport == "basketball":
        s1, s2 = random.randint(108, 124), random.randint(108, 124)
        winner = t1 if s1 > s2 else t2
        
        breakdown = f"Honestly, this is going to come down to defensive adjustments on the perimeter. If **{t1}** can't clean up their pick-and-roll defense, **{t2}** is going to generate open three-point opportunities all night. Keep an eye on the third quarter—that's usually where the tactical shifts happen."
        prediction = f"""🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}

**Quick Verdict:** Expect a high-scoring battle, but **{winner}** will likely clutch it out in the final two minutes due to better execution in the clutch."""
        
    elif sport == "american_football":
        s1, s2 = random.randint(17, 34), random.randint(17, 34)
        while s1 == s2: s1 = random.randint(17, 34) # Avoid football ties
        winner = t1 if s1 > s2 else t2
        
        breakdown = f"This matchup looks like a total chess match. **{t1}** has a tough defensive front, but **{t2}** has the explosive playmakers to bypass them if they rely on quick passes. The game will ultimately be decided by whoever controls the line of scrimmage and avoids costly red-zone turnovers."
        prediction = f"""🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}

**Quick Verdict:** It's going to be a physical, grinding game, but I'm giving the edge to **{winner}** to cover the spread."""
        
    else: # Soccer
        s1, s2 = random.randint(0, 3), random.randint(0, 3)
        winner = "Draw" if s1 == s2 else (t1 if s1 > s2 else t2)
        
        breakdown = f"This is an absolute massive tactical matchup. **{t1}** is likely going to try to control possession and press high up the pitch, which leaves them vulnerable to **{t2}**'s rapid counter-attacks out wide. If the midfield battle gets bogged down, expect a moment of individual brilliance to settle it."
        
        if winner == "Draw":
            verdict_text = "Neither side looks ready to give up too much space here. I'm expecting a highly tactical stalemate."
        else:
            verdict_text = f"**{winner}** looks slightly sharper in transition right now, which should give them the crucial advantage."
            
        prediction = f"""🔮 **Predicted Score:** {t1} **{s1} - {s2}** {t2}

**Quick Verdict:** {verdict_text}"""

    # Assemble natural, human-formatted chat structure
    response = f"""### 📋 Match Analysis: {t1} vs {t2}

{breakdown}

---

{prediction}"""
    
    return response

# -------------------------
# 5. CONVERSATIONAL FIELD INPUT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask me anything about any sport or matchup (e.g., 'What will be the score in Liverpool vs Man City?')...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SEND TO COGNITIVE CORE", use_container_width=True)

# Modern UI Suggestion Tags
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
st.caption("NextPlay AI Nexus • Version 14.7 Fixed Structural String Core")
