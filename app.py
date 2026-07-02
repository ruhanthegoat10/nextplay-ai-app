import streamlit as st
import requests
import json

# -------------------------
# 1. APEX CORPORATE THEME & GLASSMORPHISM
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
st.markdown("<div class='sub-title'>Institutional Talent Discovery & Automated Media Syndication Engine</div>", unsafe_allow_html=True)

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
# 4. HIGH-SPEED FREE LIVE GENERATIVE LLM CHANNEL
# -------------------------
def generate_apex_ai_response(history_list, current_prompt):
    try:
        # Strict business rule setting to ensure the model combines scouting analytics with media outputs
        system_instruction = (
            "You are APEX AI, a multi-billion dollar enterprise sports platform combining AI Player Scouting with Automated Media Syndication. "
            "When the user asks about scouting, finding, or analyzing players, you MUST provide two distinct components in your answer:\n"
            "1. THE SCOUTING DATA: Highly technical player stats, realistic metric comparisons, age, positional traits, and clear transfer values.\n"
            "2. THE AUTOMATED MEDIA PACKET: A complete, ready-to-publish professional press release, agency pitch deck, or video broadcast script highlighting that player's value.\n"
            "Respond dynamically to what the user types using this dual strategy-plus-content model. Format with clean, executive markdown."
        )
        
        # Build prompt payload
        full_prompt = f"{system_instruction}\n\n"
        for turn in history_list:
            full_prompt += f"{'User' if turn['role'] == 'user' else 'Apex'}: {turn['content']}\n"
        full_prompt += f"User: {current_prompt}\nApex:"

        # Call stable, unauthenticated high-speed inference cluster
        api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        payload = {
            "inputs": full_prompt,
            "parameters": {"max_new_tokens": 700, "temperature": 0.6, "return_full_text": False}
        }
        
        response = requests.post(api_url, json=payload, timeout=20)
        
        if response.status_code == 200:
            res_json = response.json()
            if isinstance(res_json, list) and len(res_json) > 0:
                output_text = res_json[0].get('generated_text', '').strip()
                if output_text:
                    return output_text
                    
        return "Apex intelligence routing node is recalibrating data clusters. Please re-submit the request to execute line inference."
        
    except Exception as e:
        return f"Apex Node Connection Disruption: {str(e)}. Re-engaging link framework."

# -------------------------
# 5. USER INTERFACE FORM STRUCTURE
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
