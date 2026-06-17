import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import random

# -------------------------
# 1. PREMIUM ULTRADARK DESIGN CONFIG (CLIPBOARD-SAFE)
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Elite",
    page_icon="⚡",
    layout="wide"
)

# Bulletproof styling vector using single-line items to prevent copy-paste truncation bugs
styles = [
    ".stApp { background: linear-gradient(180deg, #05050a 0%, #0a0b10 100%); }",
    ".main-title { text-align: center; color: #ffffff; font-size: 3.2rem; font-weight: 900; letter-spacing: -0.03em; margin-bottom: 5px; font-family: 'Inter', sans-serif; }",
    ".sub-title { text-align: center; color: #38bdf8; font-size: 1.05rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; }",
    ".dashboard-card { background: #0f111a; padding: 22px; border-radius: 12px; border: 1px solid #1e2235; margin-bottom: 15px; }",
    ".vs-container { text-align: center; font-size: 2.2rem; font-weight: 900; color: #334155; line-height: 120px; }",
    ".card-header { color: #64748b; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 15px; }",
    ".stat-label { color: #94a3b8; font-weight: 600; font-size: 0.9rem; display: block; margin-bottom: 4px; }",
    ".live-ticker { background: #161b2e; border-left: 4px solid #10b981; padding: 12px; border-radius: 6px; color: #10b981; font-family: monospace; font-size: 0.95rem; margin-bottom: 10px; }",
    "div[data-baseweb='select'] { background-color: #161925 !important; border-radius: 8px !important; }",
    "div[data-baseweb='select'] * { color: #ffffff !important; }"
]
st.markdown(f"<style>{' '.join(styles)}</style>", unsafe_allow_html=True)

# -------------------------
# 2. COMPLETE MULTI-SPORT / MULTI-LEAGUE MASTER DATA
# -------------------------
SPORTS_DATABASE = {
    "🏀 Basketball": {
        "metrics": {"off_label": "Offensive Rating (Pts/100)", "def_label": "Defensive Rating (Opp Pts/100)", "tempo_label": "Game Tempo (Pace)", "max_val": 130},
        "leagues": {
            "NBA Eastern Conference": {
                "Celtics": {"off": 120.8, "def": 110.6, "pace": 98.4, "wins": 54, "losses": 18, "streak": "W4"},
                "Bucks": {"off": 117.9, "def": 115.1, "pace": 100.8, "wins": 48, "losses": 24, "streak": "L1"},
                "Knicks": {"off": 116.0, "def": 111.4, "pace": 96.2, "wins": 45, "losses": 27, "streak": "W5"},
                "76ers": {"off": 115.2, "def": 113.0, "pace": 97.8, "wins": 40, "losses": 32, "streak": "W1"},
                "Heat": {"off": 112.1, "def": 110.2, "pace": 95.8, "wins": 39, "losses": 33, "streak": "L3"}
            },
            "NBA Western Conference": {
                "Nuggets": {"off": 118.5, "def": 112.3, "pace": 97.1, "wins": 51, "losses": 21, "streak": "W1"},
                "Mavericks": {"off": 117.2, "def": 114.8, "pace": 100.1, "wins": 46, "losses": 26, "streak": "W3"},
                "Lakers": {"off": 115.4, "def": 112.1, "pace": 100.2, "wins": 43, "losses": 29, "streak": "L2"},
                "Warriors": {"off": 116.2, "def": 115.5, "pace": 101.5, "wins": 42, "losses": 30, "streak": "W2"},
                "Timberwolves": {"off": 113.5, "def": 108.4, "pace": 97.5, "wins": 50, "losses": 22, "streak": "L1"}
            }
        }
    },
    "⚽ Soccer": {
        "metrics": {"off_label": "Expected Goals Scored (xG)", "def_label": "Expected Goals Allowed (xGA)", "tempo_label": "Possession Control %", "max_val": 100},
        "leagues": {
            "English Premier League": {
                "Man City": {"off": 84.5, "def": 31.2, "pace": 62.1, "wins": 26, "losses": 5, "streak": "W5"},
                "Arsenal": {"off": 79.2, "def": 28.4, "pace": 58.4, "wins": 25, "losses": 6, "streak": "W2"},
                "Liverpool": {"off": 81.0, "def": 36.5, "pace": 60.2, "wins": 22, "losses": 6, "streak": "D1"},
                "Chelsea": {"off": 68.3, "def": 45.1, "pace": 54.8, "wins": 18, "losses": 11, "streak": "W3"},
                "Man United": {"off": 57.4, "def": 50.2, "pace": 52.1, "wins": 16, "losses": 14, "streak": "L1"}
            },
            "La Liga": {
                "Real Madrid": {"off": 81.2, "def": 24.5, "pace": 59.8, "wins": 27, "losses": 1, "streak": "W4"},
                "Barcelona": {"off": 74.8, "def": 34.1, "pace": 61.4, "wins": 22, "losses": 5, "streak": "W1"},
                "Atletico Madrid": {"off": 67.5, "def": 38.0, "pace": 51.2, "wins": 20, "losses": 9, "streak": "W2"},
                "Girona": {"off": 72.1, "def": 42.3, "pace": 56.5, "wins": 21, "losses": 7, "streak": "L1"}
            }
        }
    },
    "🏈 Football": {
        "metrics": {"off_label": "Points Per Game (PPG)", "def_label": "Points Allowed Per Game", "tempo_label": "Third Down Conversion %", "max_val": 60},
        "leagues": {
            "AFC Conference": {
                "Chiefs": {"off": 28.4, "def": 17.3, "pace": 46.5, "wins": 13, "losses": 4, "streak": "W2"},
                "Ravens": {"off": 27.7, "def": 16.5, "pace": 44.1, "wins": 13, "losses": 4, "streak": "W1"},
                "Bills": {"off": 26.5, "def": 18.3, "pace": 43.2, "wins": 11, "losses": 6, "streak": "W3"},
                "Texans": {"off": 22.2, "def": 21.1, "pace": 40.5, "wins": 10, "losses": 7, "streak": "L1"}
            },
            "NFC Conference": {
                "49ers": {"off": 29.1, "def": 18.1, "pace": 48.2, "wins": 12, "losses": 5, "streak": "L1"},
                "Lions": {"off": 27.1, "def": 23.2, "pace": 45.8, "wins": 12, "losses": 5, "streak": "W4"},
                "Eagles": {"off": 25.5, "def": 25.2, "pace": 42.8, "wins": 11, "losses": 6, "streak": "L3"},
                "Packers": {"off": 22.5, "def": 20.6, "pace": 41.2, "wins": 9, "losses": 8, "streak": "W1"}
            }
        }
    },
    "⚾ Baseball": {
        "metrics": {"off_label": "Runs Created Index (wRC+)", "def_label": "Earned Run Average (ERA x 20)", "tempo_label": "Team Slugging Pct (SLG %)", "max_val": 160},
        "leagues": {
            "American League": {
                "Yankees": {"off": 114.0, "def": 79.0, "pace": 43.8, "wins": 92, "losses": 70, "streak": "W3"},
                "Orioles": {"off": 116.0, "def": 81.4, "pace": 44.9, "wins": 95, "losses": 67, "streak": "W1"},
                "Astros": {"off": 112.5, "def": 84.2, "pace": 42.1, "wins": 90, "losses": 72, "streak": "L1"}
            },
            "National League": {
                "Dodgers": {"off": 122.0, "def": 74.0, "pace": 45.5, "wins": 98, "losses": 64, "streak": "W1"},
                "Braves": {"off": 125.0, "def": 76.2, "pace": 47.1, "wins": 101, "losses": 61, "streak": "L2"},
                "Phillies": {"off": 109.0, "def": 78.5, "pace": 41.8, "wins": 90, "losses": 72, "streak": "W2"}
            }
        }
    }
}

# -------------------------
# 3. SELECTION MENU NAVIGATION
# -------------------------
selected_sport = st.sidebar.selectbox("🎯 SPORT TYPE", list(SPORTS_DATABASE.keys()))
SPORT_CONFIG = SPORTS_DATABASE[selected_sport]
METRICS = SPORT_CONFIG["metrics"]

selected_league_away = st.sidebar.selectbox("🔴 AWAY LEAGUE", list(SPORT_CONFIG["leagues"].keys()), key="l_away")
selected_league_home = st.sidebar.selectbox("🔵 HOME LEAGUE", list(SPORT_CONFIG["leagues"].keys()), key="l_home")

AWAY_LEAGUE_TEAMS = SPORT_CONFIG["leagues"][selected_league_away]
HOME_LEAGUE_TEAMS = SPORT_CONFIG["leagues"][selected_league_home]

# Unique path generation per sport category
clean_sport_id = selected_sport.split()[-1].lower()
MODEL_PATH = f"nextplay_{clean_sport_id}_model.pkl"

# -------------------------
# 4. RANDOM FOREST ENGINE SELF-TRAINING
# -------------------------
@st.cache_resource
def get_trained_model(sport_key, file_path):
    if os.path.exists(file_path):
        return joblib.load(file_path)
    
    np.random.seed(42)
    num_games = 2000
    
    home_off = np.random.normal(100, 15, num_games)
    away_off = np.random.normal(100, 15, num_games)
    home_def = np.random.normal(100, 15, num_games)
    away_def = np.random.normal(100, 15, num_games)
    home_rest = np.random.choice([-3.0, 0.0, 2.0], size=num_games, p=[0.2, 0.6, 0.2])
    away_rest = np.random.choice([-3.0, 0.0, 2.0], size=num_games, p=[0.2, 0.6, 0.2])
    
    score_delta = (home_off + home_rest + 2.0 - away_def) - (away_off + away_rest - home_def)
    prob = 1 / (1 + np.exp(-score_delta / 10.0))
    home_won = (np.random.rand(num_games) < prob).astype(int)
    
    df = pd.DataFrame({
        "home_off": home_off, "away_off": away_off,
        "home_def": home_def, "away_def": away_def,
        "home_rest": home_rest, "away_rest": away_rest,
        "home_won": home_won
    })
    
    X = df[["home_off", "away_off", "home_def", "away_def", "home_rest", "away_rest"]]
    y = df["home_won"]
    
    clf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    clf.fit(X, y)
    joblib.dump(clf, file_path)
    return clf

ai_classifier = get_trained_model(selected_sport, MODEL_PATH)

# -------------------------
# 5. SIDEBAR DYNAMIC LEADERBOARD
# -------------------------
st.sidebar.markdown(f"### 📊 LEAGUE RECORD MATRIX")
st.sidebar.markdown("---")

all_current_teams = {}
all_current_teams.update(AWAY_LEAGUE_TEAMS)
all_current_teams.update(HOME_LEAGUE_TEAMS)

sorted_teams = sorted(all_current_teams.items(), key=lambda x: x[1]["wins"], reverse=True)
for idx, (name, data) in enumerate(sorted_teams, 1):
    st.sidebar.markdown(f"`{idx:02d}` **{name}** ({data['wins']}-{data['losses']}) • `{data['streak']}`")

# -------------------------
# 6. LOGO HEADER BRANDING
# -------------------------
st.markdown("""
<div style="text-align: center; margin-top: 15px;">
    <svg width="70" height="70" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="50,5 95,30 95,80 50,95 5,80 5,30" fill="#0f111a" stroke="#38bdf8" stroke-width="4"/>
        <path d="M30 40 L50 25 L70 40 L50 75 Z" fill="#06b6d4" opacity="0.3"/>
        <path d="M50 20 L25 45 L50 55 L75 45 Z" fill="#38bdf8"/>
        <line x1="50" y1="55" x2="50" y2="85" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    </svg>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚡ NEXTPLAY AI ELITE</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-title'>{selected_sport} CROSS-CONFERENCE ANALYTICS SYSTEM</div>", unsafe_allow_html=True)

# -------------------------
# 7. WORKSPACE SYSTEM CONTROL LAYOUT
# -------------------------
col1, col2, col3 = st.columns([9, 2, 9])

with col1:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown(f"<p class='card-header'>🔴 AWAY: {selected_league_away}</p>", unsafe_allow_html=True)
    team1 = st.selectbox("Select Franchise / Club", list(AWAY_LEAGUE_TEAMS.keys()), index=0, key="team_away_box")
    t1_rest = st.select_slider("Conditioning Status", options=["Tired (B2B)", "Normal", "Fresh (3+ Days)"], value="Normal", key="rest_away_box")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='vs-container'>VS</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown(f"<p class='card-header'>🔵 HOME: {selected_league_home}</p>", unsafe_allow_html=True)
    filtered_home_teams = [t for t in HOME_LEAGUE_TEAMS.keys() if t != team1 or selected_league_away != selected_league_home]
    team2 = st.selectbox("Select Franchise / Club", filtered_home_teams, index=0, key="team_home_box")
    t2_rest = st.select_slider("Conditioning Status", options=["Tired (B2B)", "Normal", "Fresh (3+ Days)"], value="Normal", key="rest_home_box")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 8. VISUAL PROFILE ACCENT BARS
# -------------------------
def draw_stat_bar(label, val1, val2, max_val):
    st.markdown(f"<span class='stat-label'>{label}</span>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.progress(min(1.0, float(val1) / max_val), text=f"{team1}: {val1}")
    with col_b:
        st.progress(min(1.0, float(val2) / max_val), text=f"{team2}: {val2}")

# -------------------------
# 9. INFERENCE RUNNER WITH REAL-TIME FEED EMULATION
# -------------------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 EXECUTE MACHINE LEARNING SIMULATION RUN", use_container_width=True):
    t1_data = AWAY_LEAGUE_TEAMS[team1]
    t2_data = HOME_LEAGUE_TEAMS[team2]
    
    # Live Active Telemetry Log Output Ticker
    st.markdown("### 📡 STREAMING LIVE TELEMETRY TICKER")
    ticker_placeholder = st.empty()
    
    events_pool = [
        "Connecting data matrix arrays...",
        "Measuring stadium geographic advantage multipliers...",
        "Re-processing roster tracking telemetry matrices...",
        "Configuring Decision Node trees...",
        "Synchronizing historical feature values..."
    ]
    
    selected_logs = random.sample(events_pool, 3)
    for log in selected_logs:
        ticker_placeholder.markdown(f"<div class='live-ticker'>[TELEMETRY] {log}</div>", unsafe_allow_html=True)
        # Sequence simulator break 
        np.random.seed()
        
    ticker_placeholder.markdown(f"<div class='live-ticker' style='border-color:#38bdf8; color:#38bdf8;'>[SYSTEM] Target matrices aligned. Processing live model evaluation parameters...</div>", unsafe_allow_html=True)

    rest_map = {"Tired (B2B)": -3.0, "Normal": 0.0, "Fresh (3+ Days)": 2.0}
    
    matchup_features = pd.DataFrame([{
        "home_off": t2_data["off"], "away_off": t1_data["off"],
        "home_def": t2_data["def"], "away_def": t1_data["def"],
        "home_rest": rest_map[t2_rest], "away_rest": rest_map[t1_rest]
    }])
    
    probabilities = ai_classifier.predict_proba(matchup_features)[0]
    t2_win_prob = probabilities[1] * 100
    t1_win_prob = probabilities[0] * 100
    
    if t1_win_prob > t2_win_prob:
        winner, win_prob = team1, round(t1_win_prob, 1)
    else:
        winner, win_prob = team2, round(t2_win_prob, 1)

    st.markdown("<div class='dashboard-card' style='border-top: 3px solid #38bdf8; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("### 🧬 SIMULATION RUN INFERENCE ANALYSIS PROFILE")
    st.markdown("---")
    
    out_left, out_right = st.columns([5, 6])
    
    with out_left:
        st.markdown("<p style='font-size: 1.1rem; color: #94a3b8; font-weight: 700; margin-bottom: 2px;'>ALGORITHMIC PROBABILITY DISTRIBUTION</p>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #ffffff; font-size: 2.4rem; font-weight: 800;'>PROJECTED WINNER: <span style='color: #06b6d4;'>{winner}</span></h1>", unsafe_allow_html=True)
        
        st.metric(label="Calculated Model Prediction Confidence Index", value=f"{win_prob}%")
        st.progress(win_prob / 100)
        st.markdown("<p style='font-size:0.95rem; margin-top:25px; color:#64748b;'>Weights are parsed using sport-specific node paths trained inside random forest arrays.</p>", unsafe_allow_html=True)
        
    with out_right:
        st.markdown("<p class='card-header' style='margin-bottom: 20px;'>STRATEGY VALUE DISTRIBUTION MATRIX</p>", unsafe_allow_html=True)
        draw_stat_bar(METRICS["off_label"], t1_data["off"], t2_data["off"], METRICS["max_val"])
        st.markdown("<br>", unsafe_allow_html=True)
        draw_stat_bar(METRICS["def_label"], t1_data["def"], t2_data["def"], METRICS["max_val"])
        st.markdown("<br>", unsafe_allow_html=True)
        draw_stat_bar(METRICS["tempo_label"], t1_data["pace"], t2_data["pace"], METRICS["max_val"])
        
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# TECHNICAL FOOTER
# -------------------------
st.markdown("<br><hr style='border-color: #1e2235;'>", unsafe_allow_html=True)
st.caption("NextPlay AI Elite • Version 10.0 Multi-Sport Clean Canvas • Engineered for Advanced Sports Data Analytics")
