import streamlit as st
import time
import random
from config import SOCIALIZATION_QUOTES
from logic import generate_daily_challenges
from storage import load_data, save_data, get_user_data
from ui import (
    apply_theme, show_sticky_header, show_welcome_section, 
    show_confidence_slider, show_generate_button, show_loading_screen,
    show_challenges_header, show_challenge_card, show_empty_state,
    show_stats_dashboard
)

# Config
st.set_page_config(
    page_title="Social XP Game 🎮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply theme
apply_theme()

# Init session state
if "user_name" not in st.session_state:
    st.session_state.user_name = "Player"
if "confidence" not in st.session_state:
    st.session_state.confidence = 5
if "challenges" not in st.session_state:
    st.session_state.challenges = []
if "loading" not in st.session_state:
    st.session_state.loading = False

# Load user data for header
user_data = get_user_data(st.session_state.user_name)

# =====================
# STICKY HEADER
# =====================
show_sticky_header(
    user_data.get("total_xp", 0),
    user_data.get("completed", 0),
    user_data.get("streak", 0)
)

# =====================
# WELCOME SECTION
# =====================
show_welcome_section(st.session_state.user_name)

# =====================
# CONFIDENCE SLIDER
# =====================
confidence = show_confidence_slider()
st.session_state.confidence = confidence

# =====================
# GENERATE BUTTON
# =====================
if show_generate_button():
    st.session_state.loading = True
    st.session_state.challenges = []

# =====================
# LOADING STATE
# =====================
if st.session_state.loading:
    quote = random.choice(SOCIALIZATION_QUOTES)
    for i in range(5, 0, -1):
        show_loading_screen(quote, i)
        time.sleep(1)
    
    st.session_state.challenges = generate_daily_challenges(confidence)
    st.session_state.loading = False
    st.rerun()

# =====================
# CHALLENGES DISPLAY
# =====================
if st.session_state.challenges:
    show_challenges_header()
    
    def mark_complete(challenge):
        data = load_data()
        user_data = data.get(st.session_state.user_name, {
            "total_xp": 0,
            "completed": 0,
            "streak": 0,
            "avg_confidence": 0
        })
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
    show_empty_state()

# =====================
# STATS DASHBOARD (BOTTOM)
# =====================
user_data = get_user_data(st.session_state.user_name)
show_stats_dashboard(user_data)