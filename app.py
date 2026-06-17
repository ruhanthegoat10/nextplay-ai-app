import streamlit as st
st.set_page_config(
    page_title="NextPlay AI",
    page_icon="🏆",
    layout="wide"
)
# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #020617 0%,
        #0f172a 35%,
        #1e3a8a 100%
    );
    color: white;
}
.main-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.12);
}
.title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: white;
}
.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}
.ai-box {
    background: rgba(59,130,246,0.15);
    border-left: 4px solid #3b82f6;
    padding: 15px;
    border-radius: 12px;
    margin-top: 15px;
}
.metric-label {
    color: #cbd5e1;
}
</style>
""", unsafe_allow_html=True)
# -------------------------
# HEADER
# -------------------------
st.markdown(
    "<div class='title'>🏆 NextPlay AI</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>Sports Predictions Powered by AI</div>",
    unsafe_allow_html=True
)
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
# -------------------------
# SPORT
# -------------------------
sport = st.selectbox(
    "Choose Sport",
    [
        "🏀 NBA",
        "🏈 NFL",
        "⚽ Soccer",
        "⚾ MLB"
    ]
)
# -------------------------
# TEAMS
# -------------------------
col1, col2 = st.columns(2)
with col1:
    team1 = st.text_input("Team 1")
with col2:
    team2 = st.text_input("Team 2")
# -------------------------
# RATINGS
# -------------------------
col3, col4 = st.columns(2)
with col3:
    team1_rating = st.slider(
        "Team 1 Strength",
        0,
        100,
        85
    )
with col4:
    team2_rating = st.slider(
        "Team 2 Strength",
        0,
        100,
        85
    )
home_team = st.selectbox(
    "Home Team",
    [
        "Team 1",
        "Team 2"
    ]
)
# -------------------------
# PREDICTION
# -------------------------
if st.button("🚀 Run AI Prediction"):
    score1 = team1_rating
    score2 = team2_rating
    if home_team == "Team 1":
        score1 += 3
    else:
        score2 += 3
    diff = abs(score1 - score2)
    if score1 > score2:
        winner = team1 if team1 else "Team 1"
    elif score2 > score1:
        winner = team2 if team2 else "Team 2"
    else:
        winner = "Tie"
    probability = min(
        95,
        50 + diff * 2
    )
    st.success(f"🏆 Predicted Winner: {winner}")
    st.progress(probability / 100)
    st.metric(
        "Win Probability",
        f"{probability}%"
    )
    if diff >= 15:
        confidence = "Very High"
    elif diff >= 8:
        confidence = "High"
    elif diff >= 4:
        confidence = "Medium"
    else:
        confidence = "Low"
    st.info(f"Confidence: {confidence}")
    st.markdown(
        f"""
        <div class="ai-box">
        <h4>🤖 NextPlay AI Analysis</h4>
        <p>
        {winner} is favored due to stronger team metrics
        and home advantage adjustments.
        Current confidence level: <b>{confidence}</b>.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("NextPlay AI • V2 Startup Edition")
