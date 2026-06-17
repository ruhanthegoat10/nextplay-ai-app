import streamlit as st
from google import genai
from google.genai import types

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
    div[data-testid='stForm'] { border: none !important; padding: 0 !important; background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# Initialize deep memory logs
if "nexus_history" not in st.session_state:
    st.session_state.nexus_history = []

# Verify API key availability from secrets securely
if "GEMINI_API_KEY" in st.secrets:
    # Initialize the client automatically pulling from the environment key
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
else:
    client = None

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
st.markdown("<div class='sub-title'>Live Omni-Sport Generative Cognitive Layer</div>", unsafe_allow_html=True)

# -------------------------
# 3. INTERACTIVE CHIP SELECTION COLUMNS
# -------------------------
st.markdown("<div style='max-width: 800px; margin: 0 auto 20px auto;'>", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
quick_query = None

with c1:
    if st.button("🏆 World Cup", use_container_width=True): quick_query = "Give me a detailed update on the live matches, status, and standout news for the 2026 FIFA World Cup right now."
with c2:
    if st.button("⚾ MLB Board", use_container_width=True): quick_query = "What are the latest baseball scores, schedules, and major highlights from today's MLB action?"
with c3:
    if st.button("🏎️ Formula 1", use_container_width=True): quick_query = "Provide the current driver standings, team dynamics, and technical updates for the 2026 Formula 1 season."
with c4:
    if st.button("🔮 Predictor", use_container_width=True): quick_query = "Run a predictive analytical scenario on upcoming high-profile sports matchups this week with estimated probabilities."
with c5:
    if st.button("📊 Fantasy Scout", use_container_width=True): quick_query = "Give me advanced analytics, waiver wire suggestions, and efficiency metrics for sports fantasy formats right now."
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 4. CHAT CANVAS FEED
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay Core AI Engine:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 5. REAL GENAI INFERENCE ENGINE
# -------------------------
def query_live_ai(history_list, current_prompt):
    if not client:
        return "⚠️ **System Notification:** `GEMINI_API_KEY` was not found or recognized in your Streamlit secrets configurations. Please check your dashboard setup."
        
    try:
        # Build chat turn structures for conversation memory maintenance
        contents_payload = []
        for turn in history_list:
            role_type = "user" if turn["role"] == "user" else "model"
            contents_payload.append(
                types.Content(role=role_type, parts=[types.Part.from_text(text=turn["content"])])
            )
            
        # Append the current fresh prompt to the stack
        contents_payload.append(
            types.Content(role="user", parts=[types.Part.from_text(text=current_prompt)])
        )
        
        # Deploy high-performance analytical system instruction sets
        system_rules = (
            "You are NextPlay AI Nexus, a brilliant, premium, ultra-knowledgeable sports predictive platform. "
            "You provide highly detailed, sophisticated sports insight, analysis, scores, and statistics. "
            "Format your data elegantly with markdown, using bold titles, lists, or clean sections to make it look "
            "professional, sharp, and matching a futuristic dashboard feel."
        )
        
        # Fire request to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents_payload,
            config=types.GenerateContentConfig(
                system_instruction=system_rules,
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        return f"❌ **Inference Error encountered during generation:** {str(e)}"

# -------------------------
# 6. INPUT FLOW MANAGEMENT
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Ask anything about current tournaments, player stats, or match analyses...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ ENGAGE LIVE AI ENGINE PROCESSING", use_container_width=True)

active_input = user_query if (submit_button and user_query) else quick_query

if active_input:
    # Save user message to layout instantly
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    
    # Run the live model inference
    with st.spinner("Synthesizing real-time sports intelligence assets..."):
        ai_response = query_live_ai(st.session_state.nexus_history[:-1], active_input)
        
    # Commit result to state and update app canvas
    st.session_state.nexus_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
