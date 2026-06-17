import streamlit as st
import time
import random
import re

# -------------------------
# 1. PREMIUM GLASSMORPHISM CANVAS & STYLING
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Nexus",
    page_icon="🧠",
    layout="wide"
)

# Unified, clean style injection block to avoid list token errors
st.markdown("""
<style>
    .stApp { 
        background: #030307; 
    }
    .main-title { 
        text-align: center; 
        color: #ffffff; 
        font-size: 3.2rem; 
        font-weight: 900; 
        letter-spacing: -0.05em; 
        margin-bottom: 5px; 
        font-family: 'Inter', sans-serif; 
    }
    .sub-title { 
        text-align: center; 
        color: #a855f7; 
        font-size: 1.05rem; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.25em; 
        margin-bottom: 45px; 
    }
    .chat-container { 
        max-width: 800px; 
        margin: 0 auto; 
        padding: 10px; 
    }
    .user-bubble { 
        background: #16192b; 
        border: 1px solid #2e3556; 
        padding: 16px 20px; 
        border-radius: 16px; 
        color: #f1f5f9; 
        font-size: 1.05rem; 
        margin-bottom: 20px; 
        margin-left: 10%; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); 
    }
    .ai-bubble { 
        background: linear-gradient(135deg, #0d0e1a 0%, #121324 100%); 
        border-left: 4px solid #a855f7; 
        border-top: 1px solid #1e213d; 
        border-right: 1px solid #1e213d; 
        border-bottom: 1px solid #1e213d; 
        padding: 22px; 
        border-radius: 16px; 
        color: #e2e8f0; 
        font-size: 1.05rem; 
        line-height: 1.65; 
        margin-bottom: 20px; 
        margin-right: 10%; 
    }
    div[data-testid='stForm'] { 
        border: none !important; 
        padding: 0 !important; 
        background: transparent !important; 
    }
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
st.markdown("<div class='sub-title'>Omni-Sport Generative Cognitive Layer</div>", unsafe_allow_html=True)

# -------------------------
# 3. CHAT CANVAS FEED
# -------------------------
