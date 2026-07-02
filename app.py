import streamlit as st
import datetime

# -------------------------
# 1. APEX BRANDING & SUITE ARCHITECTURE
# -------------------------
st.set_page_config(
    page_title="APEX AI | Media Syndication Engine",
    page_icon="👑",
    layout="wide"
)

# Custom enterprise CSS to style cards similarly to modern news feeds
st.markdown("""
<style>
    .stApp { background: #020205; }
    .main-title { 
        text-align: center; color: #ffffff; font-size: 3.2rem; 
        font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; 
    }
    .sub-title { 
        text-align: center; color: #38bdf8; font-size: 0.95rem; 
        font-weight: 700; text-transform: uppercase; letter-spacing: 0.4em; 
        margin-bottom: 30px; 
    }
    .feed-container { max-width: 1100px; margin: 0 auto; }
    .news-card {
        background: #0b0f19;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .source-tag {
        color: #38bdf8;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    .headline-text {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 800;
        margin: 5px 0 10px 0;
        line-height: 1.3;
    }
    .timestamp {
        color: #64748b;
        font-size: 0.85rem;
    }
    .summary-text {
        color: #cbd5e1;
        font-size: 1rem;
        line-height: 1.6;
        margin-top: 10px;
    }
    .metric-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize data list inside session state to simulate incoming updates
if "news_feed" not in st.session_state:
    st.session_state.news_feed = [
        {
            "source": "APEX INTELLIGENCE WIRE",
            "headline": "Transfer Arbitrage Flagged: South American Wing Markets Face Imminent Undervaluation Realignment",
            "time": "10 minutes ago",
            "metrics": "SCOUTING PROFILE",
            "summary": "Data pipelines indicate high-intensity pressing profiles across regional leagues are yielding significant market inefficiencies. Portfolios showing defensive recovery margins above the 90th percentile are currently trading below baseline enterprise thresholds."
        },
        {
            "source": "B2B AGENT SYNDICATION",
            "headline": "Midfield Distribution Index: High-Pressure Progression Metrics Stabilize Across Elite Assets",
            "time": "45 minutes ago",
            "metrics": "TACTICAL ANALYTICS",
            "summary": "Automated regression modeling confirms target profiles handling ball progression with >91% accuracy under intense defensive closures are seeing severe premium escalation ahead of domestic contract cycles."
        }
    ]

# -------------------------
# 2. BRANDING HEADER
# -------------------------
st.markdown("<div class='main-title'>APEX AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Institutional Talent Discovery & Automated Media Syndication Engine</div>", unsafe_allow_html=True)

# -------------------------
# 3. INTERACTIVE CONTROL DASHBOARD
# -------------------------
st.markdown("<div class='feed-container'>", unsafe_allow_html=True)

# Front-office pipeline generation controls
with st.expander("🛠️ APEX INTEL DISTRIBUTION CONTROL", expanded=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        target_param = st.text_input("Pipeline Parameters", placeholder="e.g., Left Winger, South America, Under-22, High Pressing", label_visibility="collapsed")
    with col2:
        generate_btn = st.button("⚡ GENERATE NEWS BLOCKS", use_container_width=True)

# Inject newly engineered articles on parameter command
if generate_btn and target_param:
    new_article = {
        "source": "APEX REAL-TIME SYNCHRONIZER",
        "headline": f"Data Update: Structural Analysis Matrix Mapping Completed for '{target_param}'",
        "time": "Just now",
        "metrics": "DYNAMIC ASSET",
        "summary": f"Apex automation engines have compiled deep analytical profiles matching your strict criteria for '{target_param}'. Roster efficiency indicators and marketing wire press copies have been automatically calculated and pushed to syndication channels."
    }
    # Add new article to the top of the feed to mirror real news flows
    st.session_state.news_feed.insert(0, new_article)

# -------------------------
# 4. DISPLAY SYNDICATED FEEDS
# -------------------------
st.markdown("### 📰 LIVE DISCOVERY & NEWS SYNDICATION FLOW")

for article in st.session_state.news_feed:
    st.markdown(f"""
    <div class='news-card'>
        <span class='source-tag'>{article['source']}</span>
        <div class='headline-text'>{article['headline']}</div>
        <div>
            <span class='metric-badge'>{article['metrics']}</span>
            <span class='timestamp'>🕒 {article['time']}</span>
        </div>
        <div class='summary-text'>{article['summary']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
