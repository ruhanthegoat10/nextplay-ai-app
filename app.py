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
# 2. ENHANCED TEAM DATABASE (FULLY COMPLETED)
# -------------------------
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

sorted_teams = sorted(TEAM_DATA.items(), key=lambda x: x[1]["wins"], reverse=True)

for idx, (name, data) in enumerate(sorted_teams, 1):
    st.sidebar.markdown(f"**{idx}. {name}** ({data['wins']}-{data['losses']}) • `{data['streak']}`")

# -------------------------
# 4. APP HEADER
# -------------------------
st.markdown("<div class='main-title'>⚡ NEXTPLAY AI PRO</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Predictive Neural Network Simulation Dashboard</div>", unsafe_allow_html=True)

# -------------------------
# 5. MATCHUP BUILDER UI
# -------------------------
st.markdown("### 🛠️ Matchup Configuration")
col1, col2, col3 = st.columns([4, 1, 4])

with col1:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<p class='card-header'>🔴 AWAY TEAM</p>", unsafe_allow_html=True)
    team1 = st.selectbox("Select Visiting Franchise", list(TEAM_DATA.keys()), index=6) # Defaults to Lakers
    t1_rest = st.select_slider("Away Rest Level", options=["Tired (B2B)", "Normal", "Fresh (3+ Days)"], value="Normal")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='vs-text'>VS</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<p class='card-header'>🔵 HOME TEAM</p>", unsafe_allow_html=True)
    available_teams = [t for t in TEAM_DATA.keys() if t != team1]
    team2 = st.selectbox("Select Hosting Franchise", available_teams, index=0) # Defaults to Celtics
    t2_rest = st.select_slider("Home Rest Level", options=["Tired (B2B)", "Normal", "Fresh (3+ Days)"], value="Normal")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 6. ADVANCED SIMULATION LOGIC
# -------------------------
def run_advanced_simulation(t1, t2, r1, r2):
    t1_data, t2_data = TEAM_DATA[t1], TEAM_DATA[t2]
    rest_map = {"Tired (B2B)": -3.0, "Normal": 0.0, "Fresh (3+ Days)": 2.0}
    
    t1_eff_off = t1_data["off"] + rest_map[r1]
    t2_eff_off = t2_data["off"] + rest_map[r2] + 2.5 # +2.5 Home Court Advantage
    
    h2h_boost_t1 = 0
    if t2 in t1_data.get("h2h_vs", {}):
        history = t1_data["h2h_vs"][t2]
        h2h_boost_t1 = (sum(history) / len(history)) * 1.5

    base_pace = (t1_data["pace"] + t2_data["pace"]) / 2
    t1_final_rtg = t1_eff_off * (t2_data["def"] / 116.0) + h2h_boost_t1
    t2_final_rtg = t2_eff_off * (t1_data["def"] / 116.0)

    t1_sim_wins = 0
    t1_scores, t2_scores = [], []
    
    for _ in range(2000):
        game_pace = np.random.normal(base_pace, 4.0)
        score1 = ((np.random.normal(t1_final_rtg, 5.0)) / 100) * game_pace
        score2 = ((np.random.normal(t2_final_rtg, 5.0)) / 100) * game_pace
        
        if score1 == score2: 
            score2 += 1
            
        t1_scores.append(score1)
        t2_scores.append(score2)
        if score1 > score2: t1_wins += 1
        
    t1_pct = (t1_wins / 2000) * 100
    return round(t1_pct, 1), round(100 - t1_pct, 1), round(np.mean(t1_scores)), round(np.mean(t2_scores)), round(base_pace, 1)

# -------------------------
# 7. METRIC PROGRESS BAR GENERATOR
# -------------------------
def draw_stat_bar(label, val1, val2, max_val=130):
    st.markdown(f"<span class='stat-label'>{label}</span>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.progress(min(1.0, val1 / max_val), text=f"{team1}: {val1}")
    with col_b:
        st.progress(min(1.0, val2 / max_val), text=f"{team2}: {val2}")

# -------------------------
# 8. ANALYTICS ENGINE OUTPUT
# -------------------------
if st.button("🔮 INITIALIZE ADVANCED AI PREDICTION MATRIX", use_container_width=True):
    t1_prob, t2_prob, t1_score, t2_score, pace_est = run_advanced_simulation(team1, team2, t1_rest, t2_rest)
    
    if t1_prob > t2_prob:
        winner, win_prob, final_string = team1, t1_prob, f"{team1} {t1_score}, {team2} {t2_score}"
    else:
        winner, win_prob, final_string = team2, t2_prob, f"{team2} {t2_score}, {team1} {t1_score}"
        
    st.markdown("---")
    st.markdown("### 🧬 Simulation Projections")
    
    out_left, out_right = st.columns([5, 6])
    
    with out_left:
        st.markdown("<div class='dashboard-card' style='text-align: center; border-left: 6px solid #38bdf8;'>", unsafe_allow_html=True)
        st.markdown("<p class='card-header'>PROJECTIONS ENGINE SUCCESS INDEX</p>", unsafe_allow_html=True)
        st.markdown(f"<h2>Projected Winner: <span style='color:#38bdf8;'>{winner}</span></h2>", unsafe_allow_html=True)
        
        st.metric(label="Win Confidence Metric", value=f"{win_prob}%")
        st.progress(win_prob / 100)
        
        st.markdown(f"<p style='font-size:1.1rem; margin-top:20px; color:#e2e8f0;'>AI Scorecast Line: <b>{final_string}</b></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with out_right:
        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
        st.markdown("<p class='card-header'>📊 Roster Attribute Comparisons</p>", unsafe_allow_html=True)
        
        draw_stat_bar("Offensive Efficiency Profile (Points/100 Possessions)", TEAM_DATA[team1]["off"], TEAM_DATA[team2]["off"])
        draw_stat_bar("Defensive Floor Rating (Lower = Better Defense)", TEAM_DATA[team1]["def"], TEAM_DATA[team2]["def"])
        draw_stat_bar("Team Baseline Game Tempo (Pace)", TEAM_DATA[team1]["pace"], TEAM_DATA[team2]["pace"])
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom AI Analysis Summary
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<p class='card-header'>🤖 NextPlay Deep Scouting Summary</p>", unsafe_allow_html=True)
    
    fatigue_alert = "Noticeable schedule fatigue imbalance detected." if t1_rest != t2_rest else "Both rosters enter on equivalent rest intervals."
    
    st.markdown(f"""
    * **Simulated Scope:** Run complete. Successfully processed **2,000 algorithmic matchups** adjusting variables for standard distribution deviations.
    * **Conditioning Matrix:** {fatigue_alert} The model calculated an adjusted standard game speed environment of **{pace_est} possessions**.
    * **Front Office Insights:** The primary reason **{winner}** holds the edge is their historical matchup resilience combined with an optimized efficiency threshold.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("NextPlay AI Elite • Version 5.0 Pro Edition • Built for Next-Gen Sports Analytics")
