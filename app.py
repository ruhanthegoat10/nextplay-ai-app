import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

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
    "Celtics": {"off": 120.8, "def": 110.6, "pace": 98.4, "wins": 54, "losses": 18, "streak": "W4"},
    "Nuggets": {"off": 118.5, "def": 112.3, "pace": 97.1, "wins": 51, "losses": 21, "streak": "W1"},
    "Bucks": {"off": 117.9, "def": 115.1, "pace": 100.8, "wins": 48, "losses": 24, "streak": "L1"},
    "Mavericks": {"off": 117.2, "def": 114.8, "pace": 100.1, "wins": 46, "losses": 26, "streak": "W3"},
    "Warriors": {"off": 116.2, "def": 115.5, "pace": 101.5, "wins": 42, "losses": 30, "streak": "W2"},
    "Knicks": {"off": 116.0, "def": 111.4, "pace": 96.2, "wins": 45, "losses": 27, "streak": "W5"},
    "Lakers": {"off": 115.4, "def": 112.1, "pace": 100.2, "wins": 43, "losses": 29, "streak": "L2"},
    "Suns": {"off": 114.8, "def": 114.2, "pace": 99.0, "wins": 41, "losses": 31, "streak": "W1"},
    "Timberwolves": {"off": 113.5, "def": 108.4, "pace": 97.5, "wins": 50, "losses": 22, "streak": "L1"},
    "Heat": {"off": 112.1, "def": 110.2, "pace": 95.8, "wins": 39, "losses": 33, "streak": "L3"}
}

MODEL_PATH = "nextplay_model.pkl"

# -------------------------
# 3. ON-THE-FLY MACHINE LEARNING TRAINING ENGINE
# -------------------------
@st.cache_resource
def get_trained_model():
    """Checks for an existing model, trains a real Random Forest if missing."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    
    # Generate synthetic historical game rows to train our AI model
    np.random.seed(42)
    num_games = 5000
    
    # Generate random features mirroring realistic basketball profiles
    home_off = np.random.normal(116, 4, num_games)
    away_off = np.random.normal(116, 4, num_games)
    home_def = np.random.normal(113, 4, num_games)
    away_def = np.random.normal(113, 4, num_games)
    home_rest = np.random.choice([-3.0, 0.0, 2.0], size=num_games, p=[0.2, 0.6, 0.2])
    away_rest = np.random.choice([-3.0, 0.0, 2.0], size=num_games, p=[0.2, 0.6, 0.2])
    
    # Base calculation formula to decide historical win outcomes
    # Home court gives a +2.5 baseline boost to home offense
    score_delta = (home_off + home_rest + 2.5 - away_def) - (away_off + away_rest - home_def)
    
    # Convert score delta to probability, then generate binary 1 (Win) or 0 (Loss) labels
    prob = 1 / (1 + np.exp(-score_delta / 5.0))
    home_won = (np.random.rand(num_games) < prob).astype(int)
    
    # Store clean tracking frame
    df = pd.DataFrame({
        "home_off": home_off, "away_off": away_off,
        "home_def": home_def, "away_def": away_def,
        "home_rest": home_rest, "away_rest": away_rest,
        "home_won": home_won
    })
    
    # Extract features and targets
    X = df[["home_off", "away_off", "home_def", "away_def", "home_rest", "away_rest"]]
    y = df["home_won"]
    
    # Train actual production-level Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42)
    clf.fit(X, y)
    
    # Save training weights locally
    joblib.dump(clf, MODEL_PATH)
    return clf

# Initialize / load model automatically
ai_classifier = get_trained_model()

# -------------------------
# 4. SIDEBAR LEAGUE STANDINGS
# -------------------------
st.sidebar.markdown("## 📊 League Leaderboard")
st.sidebar.markdown("Current NBA Power Rankings & Streaks")

sorted_teams = sorted(TEAM_DATA.items(), key=lambda x: x[1]["wins"], reverse=True)

for idx, (name, data) in enumerate(sorted_teams, 1):
    st.sidebar.markdown(f"**{idx}. {name}** ({data['wins']}-{data['losses']}) • `{data['streak']}`")

# -------------------------
# 5. APP HEADER
# -------------------------
st.markdown("<div class='main-title'>⚡ NEXTPLAY AI PRO</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Predictive Random Forest Machine Learning Dashboard</div>", unsafe_allow_html=True)

# -------------------------
# 6. MATCHUP BUILDER UI
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
# 8. LIVE MACHINE LEARNING INFERENCE
# -------------------------
if st.button("🔮 RUN MACHINE LEARNING INFERENCE ENGINE", use_container_width=True):
    t1_data = TEAM_DATA[team1]
    t2_data = TEAM_DATA[team2]
    
    # Map rest selections to numeric variables identical to our training dataset structure
    rest_map = {"Tired (B2B)": -3.0, "Normal": 0.0, "Fresh (3+ Days)": 2.0}
    
    # Format current feature matrix row for inference input:
    # Order: [home_off, away_off, home_def, away_def, home_rest, away_rest]
    matchup_features = pd.DataFrame([{
        "home_off": t2_data["off"],
        "away_off": t1_data["off"],
        "home_def": t2_data["def"],
        "away_def": t1_data["def"],
        "home_rest": rest_map[t2_rest],
        "away_rest": rest_map[t1_rest]
    }])
    
    # Compute true predictive probability using our trained model weights
    # predict_proba returns array format: [[prob_away_win, prob_home_win]]
    probabilities = ai_classifier.predict_proba(matchup_features)[0]
    t2_win_prob = probabilities[1] * 100
    t1_win_prob = probabilities[0] * 100
    
    # Calculate scorecasts based on calculated efficiency weighting
    base_pace = (t1_data["pace"] + t2_data["pace"]) / 2
    t2_projected_score = round(((t2_data["off"] + rest_map[t2_rest] + 2.5) / 100) * base_pace)
    t1_projected_score = round(((t1_data["off"] + rest_map[t1_rest]) / 100) * base_pace)
    
    # Prevent unrealistic ties
    if t2_projected_score == t1_projected_score:
        if t2_win_prob > t1_win_prob:
            t2_projected_score += 2
        else:
            t1_projected_score += 2

    # Formatting winners based on model output thresholds
    if t1_win_prob > t2_win_prob:
        winner, win_prob, final_string = team1, round(t1_win_prob, 1), f"{team1} {t1_projected_score}, {team2} {t2_projected_score}"
    else:
        winner, win_prob, final_string = team2, round(t2_win_prob, 1), f"{team2} {t2_projected_score}, {team1} {t1_projected_score}"

    st.markdown("---")
    st.markdown("### 🧬 Machine Learning Analysis Outputs")
    
    out_left, out_right = st.columns([5, 6])
    
    with out_left:
        st.markdown("<div class='dashboard-card' style='text-align: center; border-left: 6px solid #38bdf8;'>", unsafe_allow_html=True)
        st.markdown("<p class='card-header'>RANDOM FOREST PROBABILITY DELTA</p>", unsafe_allow_html=True)
        st.markdown(f"<h2>Projected Winner: <span style='color:#38bdf8;'>{winner}</span></h2>", unsafe_allow_html=True)
        
        st.metric(label="Model Win Confidence Metric", value=f"{win_prob}%")
        st.progress(win_prob / 100)
        
        st.markdown(f"<p style='font-size:1.1rem; margin-top:20px; color:#e2e8f0;'>AI Scorecast Line: <b>{final_string}</b></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with out_right:
        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
        st.markdown("<p class='card-header'>📊 Roster Attribute Comparisons</p>", unsafe_allow_html=True)
        
        draw_stat_bar("Offensive Efficiency Profile (Points/100 Possessions)", t1_data["off"], t2_data["off"])
        draw_stat_bar("Defensive Floor Rating (Lower = Better Defense)", t1_data["def"], t2_data["def"])
        draw_stat_bar("Team Baseline Game Tempo (Pace)", t1_data["pace"], t2_data["pace"])
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom AI Analysis Summary
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<p class='card-header'>🤖 NextPlay Deep Scouting Summary</p>", unsafe_allow_html=True)
    
    fatigue_alert = "Noticeable schedule fatigue imbalance detected." if t1_rest != t2_rest else "Both rosters enter on equivalent rest intervals."
    
    st.markdown(f"""
    * **Algorithm Method:** Executed live multi-node feature vector calculations inside a trained **Random Forest Classifier**.
    * **Conditioning Matrix:** {fatigue_alert} The model calculated an adjusted standard game speed environment of **{base_pace} possessions**.
    * **Decision Tree Pathway:** The primary reason **{winner}** holds the edge is how the model's decision pathways weighted their efficiency threshold against opponent fatigue modifiers.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("NextPlay AI Elite • Version 6.0 Machine Learning Edition • Built for Next-Gen Sports Analytics")

