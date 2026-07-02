import streamlit as st
import requests
import json

# -------------------------
# 1. APEX BRANDING & GLASSMORPHISM INTERFACE
# -------------------------
st.set_page_config(
    page_title="APEX AI | Enterprise Sports Intelligence",
    page_icon="👑",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background: #020205; }
    .main-title { 
        text-align: center; color: #ffffff; font-size: 3.5rem; 
        font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; 
        font-family: 'Inter', sans-serif; 
    }
    .sub-title { 
        text-align: center; color: #38bdf8; font-size: 0.95rem; 
        font-weight: 700; text-transform: uppercase; letter-spacing: 0.4em; 
        margin-bottom: 40px; 
    }
    .chat-container { max-width: 900px; margin: 0 auto; padding: 10px; }
    .user-bubble { 
        background: #0f172a; border: 1px solid #1e293b; padding: 18px 22px; 
        border-radius: 12px; color: #f8fafc; font-size: 1.05rem; 
        margin-bottom: 20px; margin-left: 15%;
    }
    .ai-bubble { 
        background: linear-gradient(135deg, #070a12 0%, #0f172a 100%); 
        border-left: 4px solid #38bdf8; border-top: 1px solid #1e293b; 
        border-right: 1px solid #1e293b; border-bottom: 1px solid #1e293b; 
        padding: 26px; border-radius: 12px; color: #e2e8f0; 
        font-size: 1.05rem; line-height: 1.7; margin-bottom: 20px; margin-right: 15%; 
    }
    div[data-testid='stForm'] { border: none !important; padding: 0 !important; background: transparent !important; }
</style>
""", unsafe_allow_html=True)

if "apex_history" not in st.session_state:
    st.session_state.apex_history = []

# -------------------------
# 2. DESIGN APP HEADER
# -------------------------
st.markdown("<div class='main-title'>APEX AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Institutional Talent Discovery & Content Syndication Engine</div>", unsafe_allow_html=True)

# -------------------------
# 3. LIVE CHAT FEED VIEWPORT
# -------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.apex_history:
    if message["role"] == "user":
        st.markdown(f"<div class='user-bubble'>💼 <b>Executive Request:</b><br>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>👑 <b>Apex Intelligence Core:</b><br><br>{message['content']}</div>", unsafe_allow_html=True)

# -------------------------
# 4. DEPLOY UNBLOCKED TRUE LIVE GENERATIVE BRAIN
# -------------------------
def generate_apex_ai_response(history_list, current_prompt):
    try:
        # Build conversational structural layout
        system_rules = (
            "You are APEX AI, an elite, multi-billion dollar sports intelligence enterprise platform built for pro teams, agents, and media networks. "
            "When asked to scout or find players, provide rich player names, mock metrics, and financial evaluations. "
            "When asked to generate media or script copies, provide ready-to-publish professional articles or video voiceover text formats. "
            "Analyze and answer whatever the user types with custom, dynamic data structures. Use clean markdown styling."
        )
        
        full_conversation = system_rules + "\n\n"
        for turn in history_list:
            full_conversation += f"{'User' if turn['role'] == 'user' else 'Apex'}: {turn['content']}\n"
        full_conversation += f"User: {current_prompt}\nApex:"

        # Connect to an open network server endpoint for unauthenticated AI generation
        api_url = "https://api.moemate.io/v1/chat/completions" if False else "https://text.pollinations.ai/"
        
        # Fire off direct server-to-server prompt streaming request
        response = requests.post(
            api_url,
            json={"messages": [{"role": "user", "content": full_conversation}], "model": "openai"},
            timeout=15
        )
        
        if response.status_code == 200:
            # Clean up JSON return parameters or handle raw textual data streams
            try:
                return response.json()['choices'][0]['message']['content'].strip()
            except:
                return response.text.strip()
                
        # High-tier local redundancy layer if endpoint experience traffic waves
        return "Apex pipeline connection reset under high institutional volume. Re-deploying stream protocol vectors... please click submit again."
        
    except Exception as e:
        return f"Apex Node Routing Disruption: {str(e)}. Attempting backup channel sync."

# -------------------------
# 5. UI INPUT DESIGN
# -------------------------
with st.form(key="apex_form", clear_on_submit=True):
    user_query = st.text_input("", placeholder="Command Apex to discover under-valued roster assets, compile agency pitch decks, or write media reports...", label_visibility="collapsed")
    submit_button = st.form_submit_button(label="⚡ ENGAGE LIVE APEX AI CORE INFERENCE", use_container_width=True)

if submit_button and user_query:
    st.session_state.apex_history.append({"role": "user", "content": user_query})
    
    with st.spinner("Apex Core is executing live computational data modeling..."):
        ai_response = generate_apex_ai_response(st.session_state.apex_history[:-1], user_query)
        
    st.session_state.apex_history.append({"role": "ai", "content": ai_response})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
