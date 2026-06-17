import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="NextPlay AI",
    page_icon="🏆",
    layout="wide"
)

# -------------------------
# STYLING
# -------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#020617,#0f172a,#1e3a8a);
}

.main-title {
    text-align:center;
    color:white;
    font-size:4rem;
    font-weight:800;
}

.sub-title {
    text-align:center;
    color:#cbd5e1;
    font-size:1.2rem;
    margin-bottom:30px;
}

.result-card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.15);
}

.ai-box {
    background:#0f172a;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #3b82f6;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    "<div class='main-title'>🏆 NextPlay AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Sports Predictions Powered by AI</div>",
    unsafe_allow_html=True
)

# -------------------------
# TEAM DATABASE
# -------------------------
teams = {
    "Lakers": 92,
    "Celtics": 96,
    "Warriors": 90,
    "Nuggets": 94,
    "Suns": 89,
    "Knicks": 91,
    "Bucks": 93,
    "Heat": 88,
    "Mavericks": 90,
    "Timberwolves": 92
}

# -------------------------
# TEAM SELECTION
# -------------------------
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Team 1",
        list(teams.keys())
    )

with col2:
    team2 = st.selectbox(
        "Team 2",
        list(teams.keys()),
        index=1
    )

# -------------------------
# TEAM RATINGS
# -------------------------
team1_rating = teams[team1]
team2_rating = teams[team2]

st.write("### Team Strength")

col3, col4 = st.columns(2)

with col3:
    st.metric(team1, team1_rating)

with col4:
    st.metric(team2, team2_rating)

home_team = st.selectbox(
    "Home Team",
    [team1, team2]
)

# -------------------------
# PREDICT BUTTON
# -------------------------
if st.button("🚀 Run AI Prediction"):

    t1 = team1_rating
    t2 = team2_rating

    if home_team == team1:
        t1 += 3
    else:
        t2 += 3

    difference = abs(t1 - t2)

    if t1 > t2:
        winner = team1
        probability = min(95, 50 + difference)
    else:
        winner = team2
        probability = min(95, 50 + difference)

    confidence = probability / 100

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(f"🏆 Predicted Winner: {winner}")

    st.progress(confidence)

    st.metric(
        "Win Probability",
        f"{probability}%"
    )

    # AI ANALYSIS
    st.markdown("### 🤖 NextPlay AI Analysis")

    analysis = f"""
    {winner} enters this matchup with a stronger overall rating.

    Home court advantage was included in the prediction.

    Rating Difference: {difference}

    Projected Win Probability: {probability}%

    Confidence increases as the rating gap widens.
    """

    st.info(analysis)

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.caption("NextPlay AI V3")
