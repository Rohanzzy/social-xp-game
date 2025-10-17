import streamlit as st
import time
import random
from config import SOCIALIZATION_QUOTES
from logic import generate_daily_challenges
from storage import load_data, save_data, get_user_data, update_user_data
from ui import apply_theme
from ui import show_welcome
from ui import show_question
from ui import show_slider
from ui import show_generate_button
from ui import show_quote
from ui import show_challenge_card
from ui import show_loading
from ui import show_report_card

# Page config
st.set_page_config(
    page_title="Social XP",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply theme
apply_theme()

# Initialize session state
if "user_name" not in st.session_state:
    st.session_state.user_name = "Rohan"
if "confidence" not in st.session_state:
    st.session_state.confidence = 5
if "challenges" not in st.session_state:
    st.session_state.challenges = []
if "current_challenge_idx" not in st.session_state:
    st.session_state.current_challenge_idx = 0
if "loading" not in st.session_state:
    st.session_state.loading = False
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(SOCIALIZATION_QUOTES)

# Load user data
user_data = get_user_data(st.session_state.user_name)

# Welcome
show_welcome(st.session_state.user_name)

# Question
show_question()

# Slider
confidence = show_slider()
st.session_state.confidence = confidence

# Generate button
if show_generate_button():
    st.session_state.loading = True
    st.session_state.challenges = []
    st.session_state.current_challenge_idx = 0
    st.session_state.quote = random.choice(SOCIALIZATION_QUOTES)

# Loading state
if st.session_state.loading:
    for i in range(5, 0, -1):
        show_loading(st.session_state.quote, i)
        time.sleep(1)
    
    st.session_state.challenges = generate_daily_challenges(confidence)
    st.session_state.loading = False
    st.rerun()

# Quote (only show during loading, not after)
if not st.session_state.challenges and not st.session_state.loading:
    show_quote(st.session_state.quote)

# Challenge display
if st.session_state.challenges:
    current_idx = st.session_state.current_challenge_idx
    challenge = st.session_state.challenges[current_idx]
    
    def go_prev():
        if st.session_state.current_challenge_idx > 0:
            st.session_state.current_challenge_idx -= 1
            st.rerun()
    
    def go_next():
        if st.session_state.current_challenge_idx < len(st.session_state.challenges) - 1:
            st.session_state.current_challenge_idx += 1
            st.rerun()
    
    def mark_complete(challenge):
        data = load_data()
        user_data = data.get(st.session_state.user_name, {
            "total_xp": 0,
            "completed": 0,
            "rejections": 0,
            "streak": 0,
            "avg_confidence": 0,
            "successful": 0
        })
        
        user_data["total_xp"] = user_data.get("total_xp", 0) + challenge["xp"]
        user_data["completed"] = user_data.get("completed", 0) + 1
        user_data["successful"] = user_data.get("successful", 0) + 1
        user_data["streak"] = user_data.get("streak", 0) + 1
        
        # Update average confidence
        total_completions = user_data["completed"]
        old_avg = user_data.get("avg_confidence", 0)
        user_data["avg_confidence"] = round(
            ((old_avg * (total_completions - 1)) + st.session_state.confidence) / total_completions,
            1
        )
        
        data[st.session_state.user_name] = user_data
        save_data(data)
        
        st.success(f"✅ Challenge completed! +{challenge['xp']} XP")
        time.sleep(1)
        st.rerun()
    
    show_challenge_card(
        challenge,
        current_idx,
        len(st.session_state.challenges),
        go_prev,
        go_next,
        mark_complete
    )

# Report card
user_data = get_user_data(st.session_state.user_name)
show_report_card(
    user_data.get("successful", 0),
    user_data.get("rejections", 0),
    user_data.get("avg_confidence", 0),
    user_data.get("streak", 0)
)