import streamlit as st
import requests

# -------------------------
# 1. APEX CORPORATE UI STYLE
# -------------------------
st.set_page_config(
    page_title="APEX AI | Media Syndication Engine",
    page_icon="👑",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background: #020205; }
    .main-title { 
        text-align: center; color: #ffffff; font-size: 3.2rem; 
        font-weight: 900; letter-spacing: -0.05em; margin-bottom: 5px; 
        font-family: 'Inter', sans-serif;
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
        padding: 24px;
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
        font-size: 1.5rem;
        font-weight: 800;
        margin: 5px 0 12px 0;
        line-height: 1.3;
    }
    .timestamp {
        color: #64748b;
        font-size: 0.85rem;
    }
    .summary-text {
        color: #cbd5e1;
        font-size: 1.05rem;
        line-height: 1.65;
        margin-top: 12px;
        white-space: pre-wrap;
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

if "news_feed" not in st.session_state:
    st.session_state.news_feed = [
        {
            "source": "APEX CONTROL",
            "headline": "System Initialization Complete",
            "metrics": "CORE SYSTEM",
            "time": "Online",
            "summary": "Type your target parameters below (e.g., 'left winger under 23 from Brazil'). The live APEX generative brain will read your input, execute real-time textual inference, and deliver a fully custom scouting analysis combined with a syndicated news wire block."
        }
    ]

# -------------------------
# 2. BRANDING HEADER
# -------------------------
st.markdown("<div class='main-title'>APEX AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Institutional Talent Discovery & Automated Media Syndication Engine</div>", unsafe_allow_html=True)

st.markdown("<div class='feed-container'>", unsafe_allow_html=True)

# -------------------------
# 3. INTERACTIVE CONTROL DASHBOARD
# -------------------------
with st.expander("🛠️ APEX INTEL DISTRIBUTION CONTROL", expanded=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        target_param = st.text_input("Pipeline Parameters", placeholder="e.g., Left winger, under 26, Spanish...", label_visibility="collapsed")
    with col2:
        generate_btn = st.button("⚡ GENERATE NEWS BLOCKS", use_container_width=True)

# -------------------------
# 4. BULLETPROOF MULTI-ROUTE LLM PIPELINE
# -------------------------
def generate_true_ai_news(prompt):
    system_instruction = (
        "You are APEX AI, a multi-billion dollar enterprise sports intelligence suite. "
        "The user will give you a sports player search parameter. You must generate a highly professional response containing two things:\n"
        "1. AN OVERVIEW HEADLINE: A premium, sensational sports journalism headline.\n"
        "2. ASSET ANALYTICS & PRESS WIRE: A detailed breakdown of a realistic matching prospect (include full name, age, customized metrics like passing accuracy or pressing speed), and a professional news wire narrative copy summarizing their market impact.\n"
        "Do not copy the user's prompt word-for-word. Create entirely dynamic, high-end original content."
    )
    
    # Route A: Primary stable endpoint
    try:
        url = "https://text.pollinations.ai/"
        payload = {
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": f"Generate a recruitment profile and news release for: {prompt}"}
            ],
            "model": "openai"
        }
        res = requests.post(url, json=payload, timeout=12)
        if res.status_code == 200 and res.text:
            output = res.text.strip()
            headline = f"APEX INTEL: Strategic Realignment for '{prompt}'"
            lines = output.split('\n')
            for line in lines:
                if "headline" in line.lower() or line.startswith("#"):
                    headline = line.replace("Headline:", "").replace("**Headline:**", "").replace("#", "").strip()
                    output = output.replace(line, "").strip()
                    break
            return headline, output
    except:
        pass  # Roll over to Route B seamlessly if Route A experiences a glitch

    # Route B: Public AI cluster backup endpoint
    try:
        url_b = f"https://text.pollinations.ai/prompt/Create%20a%20detailed%20sports%20scouting%20report%20and%20media%20article%20for%20{prompt.replace(' ', '%20')}"
        res_b = requests.get(url_b, timeout=12)
        if res_b.status_code == 200 and res_b.text:
            return f"APEX BREAKING PORTFOLIO: Market Shift on {prompt}", res_b.text.strip()
    except Exception as e:
        return "APEX LINK LAYOVER", f"All live inference clusters are handling high enterprise volumes. Please try pushing your parameters through the pipeline again. Reason: {str(e)}"

if generate_btn and target_param:
    with st.spinner("Apex Core is executing live model compilation..."):
        ai_headline, ai_body = generate_true_ai_news(target_param)
        
    new_article = {
        "source": "APEX INTELLIGENCE CORE",
        "headline": ai_headline,
        "metrics": "DYNAMIC LIVE ASSET",
        "time": "Just now",
        "summary": ai_body
    }
    st.session_state.news_feed.insert(0, new_article)

# -------------------------
# 5. RENDER THE GENERATED FEED
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
