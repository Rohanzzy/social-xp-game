# ui.py - Mobile app-style UI/UX

import streamlit as st
from config import CONFIDENCE_LABELS, CHALLENGE_INSTRUCTIONS

def apply_theme():
    """Apply global Streamlit theme and styling"""
    st.markdown("""
        <style>
        * {
            margin: 0;
            padding: 0;
        }
        
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2d1b69 100%);
        }
        
        [data-testid="stMainBlockContainer"] {
            max-width: 600px;
            margin: 0 auto;
            padding: 0;
        }
        
        body, p, span, div, label {
            color: #e0e0e0 !important;
        }
        
        /* Sticky Header */
        .sticky-header {
            position: sticky;
            top: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 2px solid #06b6d4;
            padding: 12px 16px;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header-brand {
            font-size: 18px;
            font-weight: 900;
            background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .header-stats {
            display: flex;
            gap: 16px;
            font-size: 12px;
            font-weight: 700;
        }
        
        /* Main Content */
        .content-wrapper {
            padding: 16px;
        }
        
        .section {
            margin-bottom: 20px;
        }
        
        .section-title {
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 12px;
        }
        
        .welcome-text {
            font-size: 24px;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 8px;
        }
        
        .welcome-subtext {
            font-size: 14px;
            color: #a0a0a0;
            margin-bottom: 16px;
        }
        
        /* Slider */
        .slider-container {
            background: rgba(100, 100, 150, 0.15);
            padding: 20px;
            border-radius: 12px;
            border: 2px solid #06b6d4;
        }
        
        .slider-label {
            font-size: 14px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 12px;
        }
        
        .slider-value {
            font-size: 32px;
            font-weight: 900;
            text-align: center;
            color: #22d3ee;
            margin: 12px 0;
        }
        
        .slider-feedback {
            font-size: 16px;
            font-weight: 600;
            text-align: center;
            color: #a0d8a0;
            background: rgba(100, 150, 100, 0.2);
            padding: 12px;
            border-radius: 8px;
            margin-top: 12px;
        }
        
        /* Button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%) !important;
            color: white !important;
            font-weight: 900 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 14px !important;
            font-size: 16px !important;
            transition: all 0.3s !important;
        }
        
        .stButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.5) !important;
        }
        
        /* Challenge Cards */
        .challenge-card {
            background: rgba(100, 100, 150, 0.2);
            padding: 16px;
            border-radius: 10px;
            border-left: 4px solid #06b6d4;
            margin: 12px 0;
        }
        
        .challenge-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .challenge-difficulty {
            font-weight: 900;
            color: #22d3ee;
            font-size: 12px;
        }
        
        .challenge-xp {
            background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
        }
        
        .challenge-text {
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            margin: 12px 0;
            line-height: 1.4;
        }
        
        .challenge-instructions {
            font-size: 12px;
            color: #a0d8a0;
            background: rgba(100, 150, 100, 0.2);
            padding: 10px;
            border-radius: 6px;
            border-left: 3px solid #22c55e;
            margin-top: 10px;
        }
        
        /* Loading Screen */
        .loading-container {
            text-align: center;
            padding: 40px 20px;
        }
        
        .loading-title {
            font-size: 22px;
            font-weight: 900;
            color: #22d3ee;
            margin-bottom: 20px;
        }
        
        .loading-quote {
            background: rgba(100, 100, 150, 0.2);
            border-left: 4px solid #06b6d4;
            padding: 20px;
            border-radius: 10px;
            color: #22d3ee;
            font-style: italic;
            font-size: 14px;
            margin: 20px 0;
            line-height: 1.5;
        }
        
        .loading-timer {
            font-size: 16px;
            color: #a855f7;
            margin-top: 16px;
            font-weight: 600;
        }
        
        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        
        .stat-card {
            padding: 18px;
            border-radius: 10px;
            border: 2px solid;
            text-align: center;
        }
        
        .stat-label {
            font-size: 11px;
            color: #ffffff;
            margin-bottom: 8px;
            font-weight: 600;
        }
        
        .stat-value {
            font-size: 28px;
            font-weight: 900;
        }
        
        /* Info Box */
        .info-box {
            background: rgba(59, 130, 246, 0.15);
            border-left: 4px solid #3b82f6;
            padding: 16px;
            border-radius: 8px;
            color: #ffffff;
            margin: 20px 0;
        }
        
        @media (max-width: 600px) {
            [data-testid="stMainBlockContainer"] {
                padding: 0;
            }
            
            .content-wrapper {
                padding: 12px;
            }
            
            .section {
                margin-bottom: 16px;
            }
            
            .welcome-text {
                font-size: 20px;
            }
            
            .slider-value {
                font-size: 28px;
            }
            
            .stButton > button {
                font-size: 14px;
                padding: 12px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def show_sticky_header(xp, completed, streak):
    """Display sticky header with quick stats"""
    st.markdown(f"""
        <div class="sticky-header">
            <div class="header-brand">🎮 SOCIAL XP</div>
            <div class="header-stats">
                <span>⚡{xp}</span>
                <span>🏆{completed}</span>
                <span>🔥{streak}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_welcome_section(username):
    """Display welcome message"""
    st.markdown(f"""
        <div class="content-wrapper">
            <div class="section">
                <div class="welcome-text">Hey {username}! 🚀</div>
                <div class="welcome-subtext">How's your vibe today?</div>
            </div>
    """, unsafe_allow_html=True)

def show_confidence_slider():
    """Display confidence slider"""
    st.markdown("""
        <div class="slider-container">
            <div class="slider-label">Confidence Level:</div>
    """, unsafe_allow_html=True)
    
    confidence = st.slider("", min_value=1, max_value=10, value=5, label_visibility="collapsed")
    
    st.markdown(f"""
            <div class="slider-value">{confidence}/10</div>
            <div class="slider-feedback">{CONFIDENCE_LABELS[confidence]}</div>
        </div>
        <div class="section"></div>
    """, unsafe_allow_html=True)
    
    return confidence

def show_generate_button():
    """Display generate challenges button"""
    if st.button("GENERATE CHALLENGES", use_container_width=True, key="gen_btn"):
        return True
    return False

def show_loading_screen(quote, timer):
    """Display loading screen"""
    st.markdown(f"""
        <div class="loading-container">
            <div class="loading-title">✨ Creating Your Perfect Challenges...</div>
            <div class="loading-quote">"{quote}"</div>
            <div class="loading-timer">⏱️ Generating in {timer} seconds...</div>
        </div>
    """, unsafe_allow_html=True)

def show_challenges_header():
    """Display challenges section header"""
    st.markdown("""
        <div class="section">
            <div class="section-title">🎯 Your Challenges</div>
        </div>
    """, unsafe_allow_html=True)

def show_challenge_card(challenge, idx, on_complete):
    """Display single challenge card"""
    difficulty_icons = {
        "easy": "🟢",
        "medium": "🔵",
        "hard": "🟠",
        "superhard": "🔴"
    }
    
    st.markdown(f"""
        <div class="challenge-card">
            <div class="challenge-header">
                <span class="challenge-difficulty">{difficulty_icons[challenge['difficulty']]} {challenge['difficulty'].upper()}</span>
                <span class="challenge-xp">+{challenge['xp']} XP</span>
            </div>
            <div class="challenge-text">{challenge['text']}</div>
            <div class="challenge-instructions">
                <strong>💡 How:</strong> {CHALLENGE_INSTRUCTIONS[challenge['difficulty']]}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"✅ Complete", key=f"complete_{idx}", use_container_width=True):
        on_complete(challenge)

def show_empty_state():
    """Display empty state message"""
    st.markdown("""
        <div class="info-box">
            👈 Select your confidence level and click 'Generate Challenges' to get started!
        </div>
    """, unsafe_allow_html=True)

def show_stats_dashboard(user_data):
    """Display stats dashboard at bottom"""
    st.markdown("""
        <div class="section">
            <div class="section-title">📊 Your Stats</div>
            <div class="stats-grid">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
                <div class="stat-card" style="background: rgba(34, 197, 94, 0.2); border-color: #22c55e;">
                    <div class="stat-label">⚡ XP</div>
                    <div class="stat-value" style="color: #22c55e;">{user_data.get("total_xp", 0)}</div>
                </div>
                <div class="stat-card" style="background: rgba(59, 130, 246, 0.2); border-color: #3b82f6;">
                    <div class="stat-label">🏆 COMPLETED</div>
                    <div class="stat-value" style="color: #3b82f6;">{user_data.get("completed", 0)}</div>
                </div>
                <div class="stat-card" style="background: rgba(239, 68, 68, 0.2); border-color: #ef4444;">
                    <div class="stat-label">🔥 STREAK</div>
                    <div class="stat-value" style="color: #ef4444;">{user_data.get("streak", 0)}</div>
                </div>
    """, unsafe_allow_html=True)
    
    avg_conf = user_data.get("avg_confidence", 0)
    st.markdown(f"""
                <div class="stat-card" style="background: rgba(168, 85, 247, 0.2); border-color: #a855f7;">
                    <div class="stat-label">💪 AVG</div>
                    <div class="stat-value" style="color: #a855f7;">{f"{avg_conf}/10" if avg_conf else "N/A"}</div>
                </div>
            </div>
        </div>
        </div>
    """, unsafe_allow_html=True)