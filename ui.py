# ui.py - All UI and styling components

import streamlit as st
from config import CONFIDENCE_LABELS, CHALLENGE_INSTRUCTIONS

def apply_theme():
    """Apply global Streamlit theme and styling"""
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2d1b69 100%);
        }
        [data-testid="stMainBlockContainer"] {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1.5rem;
        }
        body {
            color: #e0e0e0;
        }
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%);
            color: white;
            font-weight: 900;
            border: none;
            border-radius: 10px;
            padding: 12px;
            transition: all 0.3s;
            font-size: 16px;
        }
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
        }
        @media (max-width: 768px) {
            [data-testid="stMainBlockContainer"] {
                max-width: 100%;
                padding: 1rem;
            }
            .stButton > button {
                font-size: 14px;
                padding: 10px;
            }
        }
        @media (max-width: 480px) {
            [data-testid="stMainBlockContainer"] {
                padding: 0.75rem;
            }
            .stButton > button {
                font-size: 12px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def show_header():
    """Display app header"""
    st.markdown("<div style='font-size: 36px; font-weight: 900; background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 4px;'>🎮 SOCIAL XP</div>", unsafe_allow_html=True)
    st.markdown("<div style='color: #22d3ee; font-size: 12px; font-weight: 900; letter-spacing: 1px; margin-bottom: 12px;'>LEVEL UP YOUR SOCIAL CONFIDENCE</div>", unsafe_allow_html=True)
    st.markdown("---")

def show_welcome(username):
    """Display welcome section"""
    st.markdown(f"<div style='font-size: 24px; font-weight: 900; margin: 8px 0;'>Hey <span style='background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{username}</span>, how's it going? 🚀</div>", unsafe_allow_html=True)
    st.write("Ready to build some social confidence today?")
    st.markdown("---")

def show_confidence_slider():
    """Display confidence slider and return value"""
    st.markdown("#### 🎯 How confident are you feeling today?")
    confidence = st.slider("Pick a number:", min_value=1, max_value=10, value=5, label_visibility="collapsed")
    
    st.markdown(f"<div style='text-align: center; font-size: 16px; color: #22d3ee; margin: 8px 0;'><strong>{confidence}/10</strong> — {CONFIDENCE_LABELS[confidence]}</div>", unsafe_allow_html=True)
    
    return confidence

def show_stat_card(label, value, color_code):
    """Display a single stat card"""
    st.markdown(f"""
        <div style='background: rgba({color_code}, 0.2); padding: 18px; border-radius: 10px; border: 2px solid rgb({color_code}); text-align: center;'>
            <div style='font-size: 12px; color: #a0a0a0; margin-bottom: 8px; font-weight: 600;'>{label}</div>
            <div style='font-size: 28px; font-weight: 900;'>{value}</div>
        </div>
    """, unsafe_allow_html=True)

def show_stats_dashboard(user_data):
    """Display stats dashboard with 4 stats"""
    st.markdown("<div style='font-size: 20px; font-weight: 900; margin: 16px 0;'>📊 Your Stats</div>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        show_stat_card("⚡ XP", user_data.get("total_xp", 0), "34, 197, 94")
    with col2:
        show_stat_card("🏆 DONE", user_data.get("completed", 0), "59, 130, 246")
    with col3:
        show_stat_card("🔥 STREAK", user_data.get("streak", 0), "239, 68, 68")
    with col4:
        avg_conf = user_data.get("avg_confidence", 0)
        show_stat_card("💪 AVG", f"{avg_conf}/10" if avg_conf else "N/A", "168, 85, 247")

def show_challenge_card(challenge, idx, on_complete):
    """Display a single challenge card"""
    difficulty_colors = {
        "easy": "🟢",
        "medium": "🔵",
        "hard": "🟠",
        "superhard": "🔴"
    }
    
    st.markdown(f"""
        <div style='background: rgba(100, 100, 150, 0.2); padding: 20px; border-radius: 10px; border-left: 4px solid #06b6d4; margin: 15px 0;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                <div style='font-weight: 900; color: #22d3ee;'>{difficulty_colors[challenge['difficulty']]} {challenge['difficulty'].upper()}</div>
                <div style='background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;'>+{challenge['xp']} XP</div>
            </div>
            <div style='font-size: 18px; font-weight: 600; margin: 15px 0; color: #ffffff;'>{challenge['text']}</div>
            <div style='font-size: 13px; color: #a0d8a0; background: rgba(100, 150, 100, 0.2); padding: 12px; border-radius: 6px; border-left: 3px solid #22c55e; margin-top: 10px;'>
                <strong>💡 How to do it:</strong> {CHALLENGE_INSTRUCTIONS[challenge['difficulty']]}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"✅ Mark Complete", key=f"complete_{idx}", use_container_width=True):
        on_complete(challenge)