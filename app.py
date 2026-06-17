import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import random

# -------------------------
# 1. PREMIUM ULTRADARK DESIGN CONFIG
# -------------------------
st.set_page_config(
    page_title="NextPlay AI Elite",
    page_icon="⚡",
    layout="wide"
)

# Custom Front-Office CSS Overhaul
st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(180deg, #05050a 0%, #0a0b10 100%); 
    }
    .main-title { 
        text-align: center; 
        color: #ffffff; 
        font-size: 3.2rem; 
        font-weight: 900; 
        letter-spacing: -0.03em; 
        margin-bottom: 5px;
        font-family: 'Inter', sans-serif;
    }
    .sub-title { 
        text-align: center; 
        color: #38bdf8; 
        font-size: 1.05rem; 
        font-weight: 600; 
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 30px; 
    }
    .dashboard-card { 
        background: #0f111a; 
        padding: 22px; 
        border-radius: 12px; 
        border: 1px solid #1e2235; 
        margin-bottom: 15px; 
    }
    .vs-container { 
        text-align: center; 
        font-size: 2.2rem; 
        font-weight: 900; 
        color: #334155; 
        line-height: 120px;
    }
    .card-header { 
        color: #64748b; 
        font-size: 0.85rem; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.08em; 
        margin-bottom: 15px; 
    }
    .stat-label { 
        color: #94a3b8; 
        font-weight: 600; 
        font-size: 0.9rem;
        display: block;
        margin-bottom: 4px;
    }
    .live-ticker {
        background: #161b2e;
        border-left: 4px solid #10b981;
        padding: 12px;
        border-radius: 6px;
        color: #10b981;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.95rem;
        margin-bottom: 1
