import streamlit as st
import time
import random
from config import SOCIALIZATION_QUOTES
from logic import generate_daily_challenges
from storage import load_data, save_data, get_user_data
from ui import apply_theme, show_header, show_welcome, show_confidence_slider, show_stats_dashboard, show_challenge_card

# Config
st.set_page_config(page_title="Social XP Game 🎮", layout="wide", initial_sidebar_state="collapsed")

# Apply theme
apply_theme()

# Init session state
if "user_name" not in st.session_state:
    st.session_state.user_name = "Player"
if "confidence" not in st.session_state:
    st.session_state.confidence = None
if "challenges" not in st.session_state:
    st.session_state.challenges = []
if "loading" not in st.session_state:
    st.session_state.loading = False

# =====================
# UI
# =====================
show_header()
show_welcome(st.session_state.user_name)

# Confidence slider
confidence = show_confidence_slider()
st.session_state.confidence = confidence

# Generate button
if st.button("🎲 GENERATE CHALLENGES", use_container_width=True, key="gen_challenges"):
    st.session_state.loading = True
    st.session_state.challenges = []

# Loading screen
if st.session_state.loading:
    st.markdown("<div style='text-align: center; padding: 40px;'><div style='font-size: 24px; font-weight: 900; margin-bottom: 20px;'>✨ Creating Your Perfect Challenges...</div></div>", unsafe_allow_html=True)
    
    quote = random.choice(SOCIALIZATION_QUOTES)
    quote_placeholder = st.empty()
    timer_placeholder = st.empty()
    
    for i in range(5, 0, -1):
        with quote_placeholder.container():
            st.markdown(f"<div style='text-align: center; padding: 30px; background: rgba(100, 100, 150, 0.2); border-radius: 10px; border-left: 4px solid #06b6d4; margin: 20px 0;'><i style='color: #22d3ee; font-size: 18px;'>{quote}</i></div>", unsafe_allow_html=True)
        
        with timer_placeholder.container():
            st.markdown(f"<div style='text-align: center; font-size: 16px; color: #a855f7;'>⏱️ Generating in {i} seconds...</div>", unsafe_allow_html=True)
        
        time.sleep(1)
    
    quote_placeholder.empty()
    timer_placeholder.empty()
    
    st.session_state.challenges = generate_daily_challenges(confidence)
    st.session_state.loading = False
    st.rerun()

st.markdown("---")

# =====================
# CHALLENGES DISPLAY
# =====================
if st.session_state.challenges:
    st.markdown("#### 🎯 Your Challenges Today")
    
    def mark_complete(challenge):
        data = load_data()
        user_data = data.get(st.session_state.user_name, {"total_xp": 0, "completed": 0, "streak": 0, "avg_confidence": 0})
        user_data["total_xp"] = user_data.get("total_xp", 0) + challenge["xp"]
        user_data["completed"] = user_data.get("completed", 0) + 1
        user_data["streak"] = user_data.get("streak", 0) + 1
        data[st.session_state.user_name] = user_data
        save_data(data)
        st.success(f"🎉 +{challenge['xp']} XP!")
        st.rerun()
    
    for idx, challenge in enumerate(st.session_state.challenges):
        show_challenge_card(challenge, idx, mark_complete)
else:
    st.info("👈 Select your confidence level and click 'Generate Challenges' to get started!")

st.markdown("---")

# =====================
# STATS DASHBOARD - AT BOTTOM
# =====================
user_data = get_user_data(st.session_state.user_name)
show_stats_dashboard(user_data)