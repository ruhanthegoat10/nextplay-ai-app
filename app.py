import streamlit as st
import urllib.request
import json
import datetime

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
        padding: 15px;
        margin-bottom: 15px;
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
st.markdown("<div class='sub-title'>Real-Time Live Sports Tracker Engine</div>", unsafe_allow_html=True)

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
# 4. LIVE LIVE DATA WEB FETCHERS
# -------------------------
def get_live_scores():
    try:
        # Pulls absolute up-to-the-minute live football matches from a public scraper network
        url = "https://worldcupjson.net/matches"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as response:
            matches = json.loads(response.read().decode())
            
        if not matches:
            return "### 🏟️ Live Match Center\n\nNo matches are currently active on the main tournament blocks right now. Check back during scheduled match windows!"
            
        output = "### 📡 Live Match Center Feed\n\n"
        live_count = 0
        
        for m in matches:
            # Look for active games
            if m.get('status') in ['in_progress', 'live']:
                live_count += 1
                home = m['home_team']['name']
                away = m['away_team']['name']
                h_goals = m['home_team'].get('goals', 0)
                a_goals = m['away_team'].get('goals', 0)
                time_status = m.get('time', 'Live')
                
                output += f"""<div class='score-card'>
                🟢 <b>{home} {h_goals} - {a_goals} {away}</b><br>
                ⏱️ Status: {time_status} | Stage: {m.get('stage_name', 'Group Stage')}
                </div>"""
                
        if live_count == 0:
            output += "No games are live right this second. Here are the most recent match outcomes:\n\n"
            # Fallback to display the latest completed results
            for m in matches[-3:]:
                output += f"🏁 **{m['home_team']['name']}** ({m['home_team'].get('goals', 0)}) vs **{m['away_team']['name']}** ({m['away_team'].get('goals', 0)}) - Final\n"
                
        return output
    except Exception as e:
        return """### ❌ Live Network Sync Error
        
The system could not parse the dynamic match data stream. 
* **Fix:** Ensure your Streamlit container internet access loops are clear and refresh the page!"""

def get_upcoming_schedule():
    try:
        url = "https://worldcupjson.net/matches"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as response:
            matches = json.loads(response.read().decode())
            
        output = "### 📅 Upcoming Fixture Matrix\n\n"
        future_count = 0
        
        for m in matches:
            if m.get('status') == 'future':
                future_count += 1
                home = m['home_team']['name']
                away = m['away_team']['name']
                date_str = m.get('datetime', '')[:10]
                
                output += f"🗓️ **{home} vs {away}**\n"
                output += f"* Scheduled Date: `{date_str}`\n\n"
                if future_count >= 5: # Limit list length
                    break
                    
        if future_count == 0:
            return "### 📅 Upcoming Fixture Matrix\n\nAll currently tracked rounds in this database block have been completed!"
        return output
    except Exception:
        return "### 📅 Upcoming Schedule\n\nFixtures are refreshing dynamically. Check back in a few moments for calendar sync."

# -------------------------
# 5. INPUT FEED FIELD
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Type 'live scores' or 'upcoming matches' to query raw web tracking feeds...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ SCAN LIVE SPORTS NETWORK", use_container_width=True)

active_input = None
if submit_button and user_query:
    active_input = user_query

if active_input:
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    
    # Process text queries natively against live scrapers
    query_clean = active_input.lower()
    if "live" in query_clean or "score" in query_clean:
        ai_response = get_live_scores()
    elif "upcoming" in query_clean or "match" in query_clean or "schedule" in query_clean:
        ai_response = get_upcoming_schedule()
    else:
        ai_response = """### 🔍 Query Guide
        
To read raw live data instantly without API authorization barriers, use these precise triggers:
1. Type **"live scores"** to get current scores or recent match outcomes.
2. Type **"upcoming matches"** to view scheduled fixture calendars."""
        
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
