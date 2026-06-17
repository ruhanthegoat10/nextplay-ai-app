import streamlit as st

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
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .live-badge {
        background: #ef4444;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;
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
st.markdown("<div class='sub-title'>Live World Cup 2026 Tracker</div>", unsafe_allow_html=True)

# -------------------------
# 3. CHAT CANVAS FEED
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay Hub:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 4. DATA PROCESSING LAYERS
# -------------------------
def get_live_scores():
    return """### 📡 Live Match Center Feed (June 17, 2026)

<div class='score-card'>
🏁 <b>Portugal 1 - 1 DR Congo</b> (Group K) <br>
⏱️ <b>Status:</b> Final | Venue: Houston Stadium, Texas
</div>

<div class='score-card'>
🏁 <b>Austria 1 - 0 Jordan</b> (Group J) <br>
⏱️ <b>Status:</b> Final | Venue: San Francisco Bay Area
</div>

*Type **'upcoming matches'** to see what's kicking off later tonight!*"""

def get_upcoming_schedule():
    return """### 📅 Upcoming Fixture Matrix (Today's Later Matches)

<div class='score-card'>
⏳ <b>England vs Croatia</b> (Group L)<br>
⏱️ <b>Kickoff:</b> 4:00 PM ET / 1:00 PM PT | Venue: Dallas Stadium, Texas
</div>

<div class='score-card'>
⏳ <b>Ghana vs Panama</b> (Group L)<br>
⏱️ <b>Kickoff:</b> 7:00 PM ET / 4:00 PM PT | Venue: Toronto Stadium
</div>

<div class='score-card'>
⏳ <b>Uzbekistan vs Colombia</b> (Group K)<br>
⏱️ <b>Kickoff:</b> 10:00 PM ET / 7:00 PM PT | Venue: Mexico City Stadium
</div>"""

# -------------------------
# 5. INPUT FEED FIELD
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Type 'live scores' or 'upcoming matches'...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SCAN 2026 WORLD CUP NETWORK", use_container_width=True)

if submit_button and user_query:
    st.session_state.nexus_history.append({"role": "user", "content": user_query})
    
    query_clean = user_query.lower()
    if "live" in query_clean or "score" in query_clean:
        ai_response = get_live_scores()
    elif "upcoming" in query_clean or "match" in query_clean or "schedule" in query_clean:
        ai_response = get_upcoming_schedule()
    else:
        ai_response = """### 🔍 2026 Navigation Guide
        
Type one of these specific keywords to update the UI components instantly:
1. **"live scores"** - View completed games from earlier today (Portugal/DR Congo).
2. **"upcoming matches"** - View the huge matchups playing later tonight (England/Croatia, Colombia)."""
        
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
