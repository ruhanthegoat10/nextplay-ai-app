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
# Added Records, Streaks, and Head-to-Head matchup data
TEAM_DATA = {
    "Celtics": {"off": 120.8, "def": 110.6, "pace": 98.4, "wins": 54, "losses": 18, "streak": "W4", "h2h_vs": {"Lakers": [1, 1, 0], "Warriors": [1, 0, 1]}},
    "Nuggets": {"off": 118.5, "def": 112.3, "pace": 97.1, "wins": 51, "losses": 21, "streak": "W1", "h2h_vs": {"Lakers": [1, 1, 1], "Warriors": [1, 1, 0]}},
    "Bucks": {"off": 117.9, "def": 115.1, "pace": 100.8, "wins": 48, "losses": 24, "streak": "L1", "h2h_vs": {}},
    "Mavericks": {"off": 117.2, "def": 114.8, "pace": 100.1, "wins": 46, "losses": 26, "streak": "W3", "h2h_vs": {}},
    "Warriors": {"off": 116.2, "def": 115.5, "pace": 101.5, "wins": 42, "losses": 30, "streak": "W2", "h2h_vs": {"Celtics": [0, 1, 0]}},
    "Knicks": {"off": 116.0, "def": 111.4, "pace": 96.2, "wins": 45, "losses": 27, "streak": "W5", "h2h_vs": {}},
    "Lakers": {"off": 115.4, "def": 112.1, "pace": 100.2, "wins": 43, "losses": 29, "streak": "L2", "h2h_vs": {"Celtics": [0, 0, 1], "Nuggets": [0, 0, 0]}},
    "Suns": {"off": 114.8, "def": 114.2, "pace": 99.0, "wins": 41, "losses": 31, "streak": "W1", "h2h_vs": {}},
    "Timberwolves": {"off": 113.5, "def": 108.4, "pace": 97.5, "wins": 50, "losses": 22, "streak": "L1", "h2h_vs": {}},
    "Heat": {"off": 112.1, "def": 110.2, "pace": 95.8, "wins": 39, "losses": 33, "streak": "L3", "h2h_vs": {}}
}

# -------------------------
# 3. SIDEBAR LEAGUE STANDINGS
# -------------------------
st.sidebar.markdown("## 📊 League Leaderboard")
st.sidebar.markdown("Current NBA Power Rankings & Streaks")

# Sort teams by total wins
sorted_teams = sorted(TEAM_DATA.items(), key=lambda x: x[1]
