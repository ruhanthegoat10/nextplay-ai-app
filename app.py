import streamlit as st
import random
import numpy as np

# -------------------------
# 1. PAGE CONFIG & DESIGN
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Pro",
    page_icon="⚡",
    layout="wide"
)

# Custom Premium Dark Mode Theme
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #020617 0%, #0b1329 60%, #1e1b4b 100%); }
    .main-title { text-align: center; color: #ffffff; font-size: 3.8rem; font-weight: 900; letter-spacing: -0.05em; margin-bottom: 0px; }
    .sub-title { text-align: center; color: #38bdf8; font-size: 1.2rem; font-weight: 500; margin-bottom: 40px; }
    
    /* Card Styles */
    .dashboard-card { background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px); padding: 25px; border-radius: 18px; border: 1px solid rgba(56, 189, 248, 0.15); margin-bottom: 20px; }
    .vs-text { text-align: center; font-size: 2rem; font-weight: 800; color: #64748b; margin-top: 25px; }
    
    /* Text Styles */
    .card-header { color: #94a3b8; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 10px; }
    .stat-label { color: #cbd5e1; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. ENHANCED TEAM DATABASE
# -------------------------
TEAM_DATA = {
    "Celtics": {"off": 120.8, "def": 110.6, "pace": 98.4, "wins": 54, "losses": 18, "streak": "W4", "h2h_vs": {"Lakers": [1, 1, 0], "Warriors": [1, 0, 1]}},
    "Nuggets": {"off": 118.5, "def": 112.3, "pace": 97.1, "wins": 51, "losses": 21, "streak": "W1", "h2h_vs": {"Lakers": [1, 1, 1], "Warriors": [1, 1, 0]}},
    "Bucks": {"off": 117.9, "def": 115.1, "pace": 100.8, "wins": 48
