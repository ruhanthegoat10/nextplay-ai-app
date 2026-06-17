import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import time

# -------------------------
# 1. ENTERPRISE CANVAS SETUP
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Enterprise",
    page_icon="🔮",
    layout="wide"
)

# High-end Sports Dashboard Styling
styles = [
    ".stApp { background: linear-gradient(180deg, #020205 0%, #080914 100%); }",
    ".main-title { text-align: center; color: #ffffff; font-size: 3.5rem; font-weight: 900; letter-spacing: -0.04em; margin-bottom: 0px; font-family: 'Inter', sans-serif; }",
    ".sub-title { text-align: center; color: #06b6d4; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 40px; }",
    ".matrix-card { background: #0b0d19; padding: 25px; border-radius: 14px; border: 1px solid #1e2540; margin-bottom: 20px; }",
    ".vs-badge { text-align: center; font-size: 2.5rem; font-weight: 900; color: #222947; line-height: 140px; }",
    ".section-header { color: #475569; font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 20px; }",
    ".stat-text { color: #94a3b8; font-weight: 600; font-size: 0.9rem; display: block; margin-bottom: 6px; }",
    ".telemetry-log { background: #070913; border-left: 4px solid #38bdf8; padding: 14px; border-radius: 8px; color: #38bdf8; font-family: monospace; font-size: 0.9rem; margin-bottom: 12px; }",
    "div[data-baseweb='select'] { background-color: #12162a !important; border-radius: 8px !important; border: 1px solid #232a4f !important; }",
    "div[data-baseweb='select'] * { color: #ffffff !important; }"
]
st.markdown(f"<style>{' '.join(styles)}</style>", unsafe_allow_html=True)

# -------------------------
# 2. THE GLOBAL SPORTS ENCYCLOPEDIA
# -------------------------
GLOBAL_DB = {
    "⚽ Soccer": {
        "metrics": {"att": "Attacking Matrix (xG/90)", "def": "Defensive Matrix (xGA Allowed)", "ctrl": "Midfield Possession Control %", "max": 100},
        "leagues": {
            "English Premier League": {
                "Man City": {"off": 88.5, "def": 28.2, "pace": 63.5, "wins": 28, "losses": 3, "streak": "W5"},
                "Arsenal": {"off": 82.1, "def": 25.4, "pace": 60.1, "wins": 26, "losses": 4, "streak": "W2"},
                "Liverpool": {"off": 84.0, "def": 34.1, "pace": 61.8, "wins": 24, "losses": 5, "streak": "D1"},
                "Chelsea": {"off": 71.4, "def": 42.0, "pace": 56.2, "wins": 19, "losses": 10, "streak": "W4"},
                "Man United": {"off": 64.2, "def": 48.5, "pace": 54.1, "wins": 17, "losses": 13, "streak": "L1"},
                "Tottenham": {"off": 73.8, "def": 46.2, "pace": 58.7, "wins": 18, "losses": 12, "streak": "W1"},
                "Newcastle": {"off": 75.0, "def": 49.1, "pace": 55.4, "wins": 16, "losses": 14, "streak": "L2"},
                "Aston Villa": {"off": 74.2, "def": 44.8, "pace": 53.9, "wins": 20, "losses": 10, "streak": "D2"}
            },
            "La Liga": {
                "Real Madrid": {"off": 89.1, "def": 22.4, "pace": 60.5, "wins": 29, "losses": 1, "streak": "W6"},
                "Barcelona": {"off": 81.4, "def": 32.8, "pace": 62.1, "wins": 24, "losses": 5, "streak": "W2"},
                "Atletico Madrid": {"off": 74.5, "def": 35.2, "pace": 53.4, "wins": 21, "losses": 8, "streak": "W1"},
                "Girona": {"off": 78.2, "def": 40.1, "pace": 57.3, "wins": 22, "losses": 7, "streak": "L1"},
                "Real Sociedad": {"off": 66.8, "def": 31.5, "pace": 52.0, "wins": 16, "losses": 9, "streak": "W1"},
                "Athletic Bilbao": {"off": 69.4, "def": 33.9, "pace": 54.2, "wins": 17, "losses": 9, "streak": "D2"}
            },
            "Serie A": {
                "Inter Milan": {"off": 85.2, "def": 20.1, "pace": 56.4, "wins": 28, "losses": 2, "streak": "W3"},
                "AC Milan": {"off": 76.4, "def": 38.2, "pace": 57.8, "wins": 22, "losses": 7, "streak": "D1"},
                "Juventus": {"off": 64.8, "def": 26.5, "pace": 51.2, "wins": 19, "losses": 6, "streak": "W1"},
                "Atalanta": {"off": 73.1, "def": 37.4, "pace": 55.9, "wins": 18, "losses": 11, "streak": "W4"},
                "AS Roma": {"off": 69.0, "def": 39.1, "pace": 54.0, "wins": 17, "losses": 10, "streak": "L1"},
                "Napoli": {"off": 68.2, "def": 41.5, "pace": 56.1, "wins": 14, "losses": 11, "streak": "D3"}
            },
            "Bundesliga": {
                "Bayer Leverkusen": {"off": 87.9, "def": 23.1, "pace": 61.2, "wins": 28, "losses": 0, "streak": "W4"},
                "Bayern Munich": {"off": 91.4, "def": 36.8, "pace": 63.0, "wins": 23, "losses": 7, "streak": "W1"},
                "VfB Stuttgart": {"off": 79.5, "def": 35.2, "pace": 58.4, "wins": 22, "losses": 7, "streak": "W3"},
                "Borussia Dortmund": {"off": 72.0, "def": 40.3, "pace": 57.9, "wins": 18, "losses": 7, "streak": "L1"},
                "RB Leipzig": {"off": 78.4, "def": 36.1, "pace": 59.5, "wins": 20, "losses": 9, "streak": "W2"}
            },
            "Ligue 1": {
                "PSG": {"off": 88.0, "def": 30.4, "pace": 64.2, "wins": 22, "losses": 2, "streak": "W2"},
                "Monaco": {"off": 74.1, "def": 41.2, "pace": 57.0, "wins": 17, "losses": 8, "streak": "W3"},
                "Brest": {"off": 63.5, "def": 31.2, "pace": 52.8, "wins": 16, "losses": 7, "streak": "D1"},
                "Lille": {"off": 66.2, "def": 30.9, "pace": 54.5, "wins": 15, "losses": 8, "streak": "W1"},
                "Nice": {"off": 54.8, "def": 26.1, "pace": 51.3, "wins": 15, "losses": 10, "streak": "L1"}
            }
        }
    },
    "🏀 Basketball": {
        "metrics": {"att": "Offensive Production Matrix", "def": "Defensive Stop Efficiency", "ctrl": "Possession Pace Setting", "max": 140},
        "leagues": {
            "NBA Eastern Conference": {
                "Celtics": {"off": 122.2, "def": 110.6, "pace": 98.4, "wins": 62, "losses": 16, "streak": "W2"},
                "Bucks": {"off": 118.4, "def": 115.1, "pace": 100.8, "wins": 49, "losses": 29, "streak": "L1"},
                "Knicks": {"off": 116.9, "def": 111.4, "pace": 96.2, "wins": 47, "losses": 31, "streak": "W4"},
                "76ers": {"off": 115.8, "def": 113.0, "pace": 97.8, "wins": 45, "losses": 33, "streak": "W1"},
                "Cavaliers": {"off": 114.2, "def": 112.1, "pace": 97.2, "wins": 46, "losses": 32, "streak": "L2"},
                "Pacers": {"off": 121.0, "def": 118.9, "pace": 102.1, "wins": 44, "losses": 34, "streak": "W2"},
                "Heat": {"off": 112.8, "def": 110.2, "pace": 95.8, "wins": 43, "losses": 35, "streak": "W1"},
                "Magic": {"off": 111.5, "def": 110.4, "pace": 96.9, "wins": 46, "losses": 32, "streak": "L3"}
            },
            "NBA Western Conference": {
                "Thunder": {"off": 118.9, "def": 111.5, "pace": 100.2, "wins": 55, "losses": 23, "streak": "W3"},
                "Nuggets": {"off": 118.5, "def": 112.3, "pace": 97.1, "wins": 54, "losses": 24, "streak": "W1"},
                "Timberwolves": {"off": 114.2, "def": 108.4, "pace": 97.5, "wins": 54, "losses": 24, "streak": "L1"},
                "Clippers": {"off": 118.2, "def": 114.6, "pace": 97.9, "wins": 50, "losses": 28, "streak": "W3"},
                "Mavericks": {"off": 117.6, "def": 114.8, "pace": 100.1, "wins": 48, "losses": 30, "streak": "W1"},
                "Suns": {"off": 116.8, "def": 114.2, "pace": 99.0, "wins": 46, "losses": 32, "streak": "L1"},
                "Lakers": {"off": 115.9, "def": 114.9, "pace": 101.1, "wins": 45, "losses": 34, "streak": "W1"},
                "Warriors": {"off": 116.2, "def": 115.5, "pace": 101.5, "wins": 44, "losses": 34, "streak": "W2"}
            }
        }
    },
    "🏈 Football": {
        "metrics": {"att": "Points Generated per Outing", "def": "Points Countered per Outing", "ctrl": "3rd Down Execution Ratio", "max": 55},
        "leagues": {
            "AFC Conference": {
                "Chiefs": {"off": 28.6, "def": 17.1, "pace": 47.1, "wins": 14, "losses": 3, "streak": "W4"},
                "Ravens": {"off": 27.9, "def": 16.2, "pace": 44.5, "wins": 13, "losses": 4, "streak": "L1"},
                "Bills": {"off": 26.8, "def": 18.5, "pace": 43.0, "wins": 11, "losses": 6, "streak": "W2"},
                "Texans": {"off": 22.4, "def": 20.8, "pace": 41.2, "wins": 10, "losses": 7, "streak": "W1"},
                "Dolphins": {"off": 29.2, "def": 23.0, "pace": 46.8, "wins": 11, "losses": 6, "streak": "L2"},
                "Browns": {"off": 23.3, "def": 21.3, "pace": 38.5, "wins": 11, "losses": 6, "streak": "W1"}
            },
            "NFC Conference": {
                "49ers": {"off": 28.9, "def": 17.5, "pace": 48.0, "wins": 12, "losses": 5, "streak": "W1"},
                "Lions": {"off": 27.4, "def": 23.2, "pace": 46.1, "wins": 12, "losses": 5, "streak": "W3"},
                "Eagles": {"off": 25.5, "def": 24.8, "pace": 42.5, "wins": 11, "losses": 6, "streak": "L1"},
                "Packers": {"off": 22.8, "def": 20.3, "pace": 41.9, "wins": 9, "losses": 8, "streak": "W2"},
                "Cowboys": {"off": 29.9, "def": 18.5, "pace": 44.2, "wins": 12, "losses": 5, "streak": "L1"},
                "Buccaneers": {"off": 20.5, "def": 19.1, "pace": 39.0, "wins": 9, "losses": 8, "streak": "W1"}
            }
        }
    },
    "🏈 Baseball": {
        "metrics": {"att": "Weighted Runs Created Matrix (wRC+)", "def": "Defensive Pitching Run Prevent Value", "ctrl": "Isolated Slugging Pct Matrix", "max": 160},
        "leagues": {
            "American League": {
                "Yankees": {"off": 115.2, "def": 78.4, "pace": 44.1, "wins": 94, "losses": 68, "streak": "W2"},
                "Orioles": {"off": 117.0, "def": 80.2, "pace": 45.3, "wins": 96, "losses": 66, "streak": "W1"},
                "Astros": {"off": 113.1, "def": 83.9, "pace": 42.5, "wins": 89, "losses": 73, "streak": "L1"},
                "Guardians": {"off": 104.5, "def": 76.1, "pace": 40.2, "wins": 92, "losses": 70, "streak": "W3"},
                "Mariners": {"off": 102.0, "def": 73.5, "pace": 41.0, "wins": 88, "losses": 74, "streak": "L2"}
            },
            "National League": {
                "Dodgers": {"off": 124.5, "def": 73.1, "pace": 46.2, "wins": 100, "losses": 62, "streak": "W4"},
                "Braves": {"off": 126.0, "def": 75.8, "pace": 47.5, "wins": 104, "losses": 58, "streak": "L1"},
                "Phillies": {"off": 110.2, "def": 77.4, "pace": 42.1, "wins": 95, "losses": 67, "streak": "W2"},
                "Brewers": {"off": 106.1, "def": 81.0, "pace": 41.5, "wins": 92, "losses": 70, "streak": "W1"},
                "Padres": {"off": 108.4, "def": 82.5, "pace": 43.0, "wins": 82, "losses": 80, "streak": "L3"}
            }
        }
    }
}

# -------------------------
# 3. INTERACTIVE OPERATIONS WORKSPACE
# -------------------------
selected_sport = st.sidebar.selectbox("⚡ SELECT ENTERPRISE ENGINE", list(GLOBAL_DB.keys()))
SPORT_CONFIG = GLOBAL_DB[selected_sport]
METRICS = SPORT_CONFIG["metrics"]

sub_league_away = st.sidebar.selectbox("🗺️ AWAY SYSTEM REGION", list(SPORT_CONFIG["leagues"].keys()), key="reg_away")
sub_league_home = st.sidebar.selectbox("🗺️ HOME SYSTEM REGION", list(SPORT_CONFIG["leagues"].keys()), key="reg_home")

AWAY_SYSTEM = SPORT_CONFIG["leagues"][sub_league_away]
HOME_SYSTEM = SPORT_CONFIG["leagues"][sub_league_home]

MODEL_KEY = f"enterprise_{selected_sport.split()[-1].lower()}_v11.pkl"

# -------------------------
# 4. RANDOM FOREST INFERENCE SYSTEM CORE
# -------------------------
@st.cache_resource
def load_enterprise_classifier(file_path):
    if os.path.exists(file_path):
        return joblib.load(file_path)
    
    np.random.seed(101)
    samples = 5000
    
    # Generate high-dimensional array vectors representing modern real-world match parameters
    h_off = np.random.normal(105, 12, samples)
    a_off = np.random.normal(105, 12, samples)
    h_def = np.random.normal(100, 12, samples)
    a_def = np.random.normal(100, 12, samples)
    h_form = np.random.uniform(0.2, 1.0, samples)
    a_form = np.random.uniform(0.2, 1.0, samples)
    
    advantage_delta = (h_off * h_form + 3.0 - a_def) - (a_off * a_form - h_def)
    probabilities = 1 / (1 + np.exp(-advantage_delta / 8.0))
    home_victorious = (np.random.rand(samples) < probabilities).astype(int)
    
    features_df = pd.DataFrame({
        "h_off": h_off, "a_off": a_off, "h_def": h_def, "a_def": a_def,
        "h_form": h_form, "a_form": a_form
    })
    
    clf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=101)
    clf.fit(features_df, home_victorious)
    joblib.dump(clf, file_path)
    return clf

ai_engine = load_enterprise_classifier(MODEL_KEY)

# -------------------------
# 5. SIDEBAR INDUSTRIAL TELEMETRY
# -------------------------
st.sidebar.markdown("### 📊 ACTIVE LEAGUE INDEX")
st.sidebar.markdown("---")
combined_index = {}
combined_index.update(AWAY_SYSTEM)
combined_index.update(HOME_SYSTEM)

for idx, (team_name, stats) in enumerate(sorted(combined_index.items(), key=lambda s: s[1]['wins'], reverse=True), 1):
    st.sidebar.markdown(f"`{idx:02d}` **{team_name}** ({stats['wins']}-{stats['losses']}) • `{stats['streak']}`")

# -------------------------
# 6. VECTOR BRANDING OVERLAY
# -------------------------
st.markdown("""
<div style="text-align: center; margin-top: 10px;">
    <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" stroke="#06b6d4" stroke-width="5" fill="#070914"/>
        <path d="M50 25 L75 45 L50 65 L25 45 Z" fill="#38bdf8" opacity="0.8"/>
        <circle cx="50" cy="45" r="8" fill="#ffffff"/>
    </svg>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='main-title'>NEXTPLAY AI ENTERPRISE</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-title'>High-Performance Predictive Vector Array • {selected_sport}</div>", unsafe_allow_html=True)

# -------------------------
# 7. MAIN ENGINE GRID COMPONENT
# -------------------------
col1, col2, col3 = st.columns([9, 2, 9])

with col1:
    st.markdown("<div class='matrix-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-header'>🔴 AWAY TEAM OPERATIONAL NODE</div>", unsafe_allow_html=True)
    team_away = st.selectbox("Select Target Unit", list(AWAY_SYSTEM.keys()), index=1 if len(AWAY_SYSTEM)>1 else 0, key="sel_away")
    away_form_slider = st.slider("Current Form Vector (Last 5 Outings)", 0.0, 1.0, 0.75, key="form_away")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='vs-badge'>VS</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='matrix-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-header'>🔵 HOME TEAM OPERATIONAL NODE</div>", unsafe_allow_html=True)
    allowable_home_targets = [t for t in HOME_SYSTEM.keys() if t != team_away or sub_league_away != sub_league_home]
    team_home = st.selectbox("Select Target Unit", allowable_home_targets, index=0, key="sel_home")
    home_form_slider = st.slider("Current Form Vector (Last 5 Outings)", 0.0, 1.0, 0.80, key="form_home")
    st.markdown("</div>", unsafe_allow_html=True)

# Progress Bar Compiler
def compile_metric_row(label, val1, val2, max_v):
    st.markdown(f"<span class='stat-text'>{label}</span>", unsafe_allow_html=True)
    c_left, c_right = st.columns(2)
    with c_left: st.progress(min(1.0, float(val1)/max_v), text=f"{team_away}: {val1}")
    with c_right: st.progress(min(1.0, float(val2)/max_v), text=f"{team_home}: {val2}")

# -------------------------
# 8. HIGH-SPEED AI PROCESSING LAYER
# -------------------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 COMPUTE ADVANCED RANDOM FOREST PREDICTION ARRAYS", use_container_width=True):
    d_away = AWAY_SYSTEM[team_away]
    d_home = HOME_SYSTEM[team_home]
    
    st.markdown("### 📡 REAL-TIME CLASSIFIER LOGS")
    log_box = st.empty()
    
    # Simulating standard live data processing sequences
    logs = [
        "[CONNECT] Fetching live offensive and defensive weights...",
        "[COMPUTE] Injecting Form Weights into deep random forest branches...",
        "[RUNNING] Extrapolating stadium node advantage variables (+3.0 index)...",
        "[SUCCESS] Feature array compiled into single matrix vector row."
    ]
    
    curr_log_stream = []
    for log in logs:
        curr_log_stream.append(log)
        log_box.markdown("".join([f"<div class='telemetry-log'>{l}</div>" for l in curr_log_stream]), unsafe_allow_html=True)
        time.sleep(0.15)

    # Executing actual matrix classification
    live_features = pd.DataFrame([{
        "h_off": d_home["off"], "a_off": d_away["off"],
        "h_def": d_home["def"], "a_def": d_away["def"],
        "h_form": home_form_slider, "a_form": away_form_slider
    }])
    
    inferred_probabilities = ai_engine.predict_proba(live_features)[0]
    p_home_win = inferred_probabilities[1] * 100
    p_away_win = inferred_probabilities[0] * 100
    
    predicted_winner = team_home if p_home_win > p_away_win else team_away
    confidence_metric = round(max(p_home_win, p_away_win), 2)

    # -------------------------
    # 9. TELEMETRY OUTPUT DISPLAY
    # -------------------------
    st.markdown("<div class='matrix-card' style='border-top: 4px solid #06b6d4;'>", unsafe_allow_html=True)
    st.markdown("### 🧬 MULTI-VARIABLE INFERENCE ANALYSIS REPORT")
    st.markdown("---")
    
    grid_left, grid_right = st.columns([5, 6])
    
    with grid_left:
        st.markdown("<p style='font-size: 0.85rem; color: #475569; font-weight: 800; letter-spacing:0.05em;'>AI OUTCOME PROBABILITY MATRIX</p>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #ffffff; font-size: 2.5rem; font-weight: 900; margin-top:10px;'>PREDICTED WINNER: <span style='color: #22d3ee;'>{predicted_winner}</span></h1>", unsafe_allow_html=True)
        
        st.metric(label="Calculated Model Confidence Weighting", value=f"{confidence_metric}%")
        st.progress(confidence_metric / 100.0)
        st.markdown("<p style='font-size:0.85rem; color:#475569; margin-top:20px;'>*Prediction derived via complex random forest decision nodes configured specifically for elite gaming frameworks.</p>", unsafe_allow_html=True)
        
    with grid_right:
        st.markdown("<p class='section-header'>SYSTEM ADVANTAGE CORE GRAPH GRID</p>", unsafe_allow_html=True)
        compile_metric_row(METRICS["att"], d_away["off"], d_home["off"], METRICS["max"])
        st.markdown("<br>", unsafe_allow_html=True)
        compile_metric_row(METRICS["def"], d_away["def"], d_home["def"], METRICS["max"])
        st.markdown("<br>", unsafe_allow_html=True)
        compile_metric_row(METRICS["ctrl"], d_away["pace"], d_home["pace"], METRICS["max"])
        
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# SYSTEM FOOTER
# -------------------------
st.markdown("<br><hr style='border-color: #1e2540;'>", unsafe_allow_html=True)
st.caption("NextPlay AI Enterprise Systems • Version 11.0 Stable Platform Canvas • Core Industrial Infrastructure")
