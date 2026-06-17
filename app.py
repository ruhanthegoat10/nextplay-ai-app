import streamlit as st
# -----------------------
# PAGE SETUP
# -----------------------
st.set_page_config(
    page_title="NextPlay AI",
    page_icon="🏆",
    layout="wide"
)
# -----------------------
# STYLE
# -----------------------
st.markdown("""
<style>
.stApp {
    background-color: #0B1426;
}
.big-title {
    color: white;
    text-align: center;
    font-size: 3rem;
}
.card {
    background-color: #111C3A;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)
# -----------------------
# HEADER
# -----------------------
st.markdown(
    "<h1 class='big-title'>🏆 NextPlay AI</h1>",
    unsafe_allow_html=True
)
st.write("AI-powered sports prediction platform")
# -----------------------
# SPORT SELECTOR
# -----------------------
sport = st.selectbox(
    "Choose Sport",
    ["🏀 NBA", "🏈 NFL", "⚽ Soccer", "⚾ MLB"]
)
# -----------------------
# TEAM INPUTS
# -----------------------
team1 = st.text_input("Team 1 Name")
team2 = st.text_input("Team 2 Name")
team1_score = st.number_input(
    "Team 1 Rating",
    min_value=0.0,
    max_value=200.0,
    value=100.0
)
team2_score = st.number_input(
    "Team 2 Rating",
    min_value=0.0,
    max_value=200.0,
    value=100.0
)
home_team = st.selectbox(
    "Home Team",
    ["Team 1", "Team 2"]
)
# -----------------------
# PREDICTION
# -----------------------
if st.button("Predict Winner"):
    t1 = team1_score
    t2 = team2_score
    if home_team == "Team 1":
        t1 += 3
    else:
        t2 += 3
    difference = abs(t1 - t2)
    if difference >= 20:
        confidence = "Very High"
    elif difference >= 10:
        confidence = "High"
    elif difference >= 5:
        confidence = "Medium"
    else:
        confidence = "Low"
    if t1 > t2:
        winner = team1 if team1 else "Team 1"
        percent = min(95, 50 + difference)
    elif t2 > t1:
        winner = team2 if team2 else "Team 2"
        percent = min(95, 50 + difference)
    else:
        winner = "Tie"
        percent = 50
    st.success(f"🏆 Predicted Winner: {winner}")
    st.metric(
        "Win Probability",
        f"{percent}%"
    )
    st.info(f"Confidence: {confidence}")
# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.caption("NextPlay AI V1")
