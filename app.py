import streamlit as st
from groq import Groq

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

if "nexus_history" not in st.session_state:
    st.session_state.nexus_history = []

# Initialize True Groq Client from Streamlit App Secrets
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    client = None

# -------------------------
# 2. DESIGN APP HEADER
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
st.markdown("<div class='sub-title'>Live Open-Access AI Language Matrix</div>", unsafe_allow_html=True)

# -------------------------
# 3. INTERACTIVE NAVIGATION CHIPS
# -------------------------
st.markdown("<div style='max-width: 800px; margin: 0 auto 20px auto;'>", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
quick_query = None

with c1:
    if st.button("🏆 World Cup", use_container_width=True): quick_query = "Give me a breakdown of recent historic matches, metrics, and tactical storylines surrounding the FIFA World Cup."
with c2:
    if st.button("⚾ MLB Board", use_container_width=True): quick_query = "Analyze the current MLB landscape, division standouts, and team dynamics."
with c3:
    if st.button("🏎️ Formula 1", use_container_width=True): quick_query = "Provide tactical driver notes and race strategies for the top teams in Formula 1."
with c4:
    if st.button("🔮 Predictor", use_container_width=True): quick_query = "Simulate an analytical sports prediction scenario for a high profile match including win probabilities."
with c5:
    if st.button("📊 Fantasy Scout", use_container_width=True): quick_width = True; quick_query = "Show advanced math performance indexes or target trends for a sports fantasy roster selection."
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 4. LIVE CHAT CANVAS FEED
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.nexus_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🔹 <b>NextPlay AI:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 5. LIVE GENERATIVE INFERENCE LOGIC
# -------------------------
def run_live_llm_inference(history, current_prompt):
    if not client:
        return "⚠️ **System Notification:** `GROQ_API_KEY` was not found in your Streamlit secrets. Please add it to unlock true AI generations."
        
    try:
        # Build memory profile for the AI model conversation history
        messages_payload = [
            {
                "role": "system",
                "content": (
                    "You are NextPlay AI Nexus, an elite, premium AI sports assistant. "
                    "You break down matchups, rosters, scores, tactics, and trivia with creative insight. "
                    "Do not use simple template arrays. Respond to whatever user says with analytical intelligence. "
                    "Use clean markdown formatting, bold headings, and lists to match a premium dark UI dashboard."
                )
            }
        ]
        
        for turn in history:
            messages_payload.append({"role": turn["role"], "content": turn["content"]})
            
        messages_payload.append({"role": "user", "content": current_prompt})
        
        # Call open-source Llama3 running on fast hardware inference engines
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages_payload,
            temperature=0.7,
            max_tokens=1024
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ **Generation Pipeline Error:** {str(e)}"

# -------------------------
# 6. APPLICATION INPUT MECHANICS
# -------------------------
with st.form(key="nexus_input_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Type any real sports conversation challenge here...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ EXECUTE AI GENERATIVE MATRIX INFERENCE", use_container_width=True)

active_input = user_query if (submit_button and user_query) else quick_query

if active_input:
    st.session_state.nexus_history.append({"role": "user", "content": active_input})
    
    with st.spinner("Streaming analytical intelligence parameters..."):
        ai_response = run_live_llm_inference(st.session_state.nexus_history[:-1], active_input)
        
    st.session_state.nexus_history.append({"role": "assistant", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
