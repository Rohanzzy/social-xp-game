# ui.py - Game-like funky design

import streamlit as st
from config import CHALLENGE_INSTRUCTIONS

def apply_theme():
    """Apply funky game-like theme"""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            animation: gradientShift 8s ease infinite;
            background-size: 200% 200%;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        [data-testid="stMainBlockContainer"] {
            max-width: 500px;
            margin: 0 auto;
            padding: 40px 16px 24px 16px;
        }
        
        /* Welcome title with glow */
        .main-title {
            font-size: 32px;
            font-weight: 900;
            color: #ffffff;
            text-align: center;
            margin-bottom: 32px;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.5),
                         0 0 40px rgba(255, 105, 180, 0.3);
            animation: pulse 2s ease-in-out infinite;
            line-height: 1.3;
            padding: 0 16px;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        .question {
            font-size: 22px;
            font-weight: 600;
            color: #ffffff;
            text-align: center;
            margin-bottom: 32px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        /* Custom slider styling - hide value label */
        .stSlider {
            padding: 24px 0;
        }
        
        .stSlider > div > div > div > div {
            background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #1dd1a1);
        }
        
        .stSlider > div > div > div > div > div {
            background: white;
            border: 4px solid #667eea;
            width: 32px !important;
            height: 32px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        /* Hide the default slider value */
        .stSlider > div > div > div > div[data-baseweb="slider"] > div > div {
            display: none !important;
        }
        
        .slider-emoji-row {
            display: flex;
            justify-content: space-between;
            margin-top: 12px;
            font-size: 20px;
        }
        
        /* Generate button */
        .stButton > button {
            width: 100%;
            background: #ffffff !important;
            color: #667eea !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 16px !important;
            padding: 18px !important;
            font-size: 18px !important;
            margin: 32px 0 !important;
            transition: all 0.3s !important;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            background: #f0f0f0 !important;
            transform: translateY(-4px) !important;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Quote box */
        .quote-box {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            margin: 32px 0;
            font-style: italic;
            color: #ffffff;
            font-size: 15px;
            line-height: 1.8;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }
        
        /* Pokemon/Sports card style */
        .challenge-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: 4px solid #ffd700;
            border-radius: 20px;
            padding: 28px 28px 120px 28px;
            margin: 32px 0;
            min-height: 320px;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4),
                        inset 0 0 60px rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: transform 0.3s;
        }
        
        .challenge-card:hover {
            transform: scale(1.02);
        }
        
        .challenge-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                45deg,
                transparent,
                rgba(255, 255, 255, 0.1),
                transparent
            );
            animation: shine 3s infinite;
        }
        
        @keyframes shine {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .challenge-title {
            font-size: 26px;
            font-weight: 900;
            color: #ffd700;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .challenge-text {
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin: 24px 0;
            line-height: 1.5;
            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        }
        
        .difficulty-badge {
            display: inline-block;
            background: rgba(255, 215, 0, 0.2);
            border: 2px solid #ffd700;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 700;
            color: #ffd700;
            margin: 16px 0;
        }
        
        .challenge-description {
            font-size: 14px;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.7;
            margin-top: 20px;
            text-align: center;
            background: rgba(0, 0, 0, 0.2);
            padding: 16px;
            border-radius: 12px;
        }
        
        /* Navigation arrows */
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 24px;
            gap: 12px;
        }
        
        .nav-button {
            background: rgba(255, 255, 255, 0.2) !important;
            border: 3px solid rgba(255, 255, 255, 0.5) !important;
            border-radius: 12px !important;
            padding: 12px 20px !important;
            color: #ffffff !important;
            font-size: 24px !important;
            font-weight: 900 !important;
            transition: all 0.3s !important;
            min-width: 60px !important;
        }
        
        .nav-button:hover {
            background: rgba(255, 255, 255, 0.4) !important;
            border-color: #ffffff !important;
            transform: scale(1.1) !important;
        }
        
        /* Loading screen */
        .loading-container {
            text-align: center;
            padding: 48px 20px;
        }
        
        .loading-title {
            font-size: 24px;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 24px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            animation: bounce 1s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .loading-spinner {
            font-size: 48px;
            animation: spin 2s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Report card */
        .report-title {
            font-size: 28px;
            font-weight: 900;
            color: #ffffff;
            text-align: center;
            margin: 48px 0 32px 0;
            text-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 48px;
        }
        
        @media (max-width: 600px) {
            .stats-grid {
                grid-template-columns: 1fr;
                gap: 16px;
                max-width: 280px;
                margin: 0 auto 48px auto;
            }
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 20px;
            padding: 24px 16px;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: all 0.3s;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            min-height: 160px;
        }
        
        @media (min-width: 601px) {
            .stat-card {
                aspect-ratio: 1;
            }
        }
        
        .stat-card:hover {
            transform: translateY(-8px);
            border-color: #ffd700;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
        }
        
        .stat-value {
            font-size: 52px;
            font-weight: 900;
            color: #ffd700;
            margin-bottom: 8px;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }
        
        .stat-label {
            font-size: 13px;
            color: #ffffff;
            line-height: 1.4;
            font-weight: 600;
        }
        
        /* Desktop responsive */
        @media (min-width: 768px) {
            [data-testid="stMainBlockContainer"] {
                max-width: 600px;
                padding: 40px 24px;
            }
            
            .main-title {
                font-size: 46px;
            }
            
            .question {
                font-size: 26px;
            }
            
            .challenge-card {
                min-height: 380px;
                padding: 36px;
            }
            
            .challenge-title {
                font-size: 30px;
            }
            
            .challenge-text {
                font-size: 22px;
            }
            
            .stat-value {
                font-size: 60px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def get_first_name(full_name):
    """Extract first name from username"""
    return full_name.split()[0] if full_name else "Player"

def show_welcome(username):
    """Show welcome with first name only - centered"""
    first_name = get_first_name(username)
    st.markdown(f'<div class="main-title">Welcome back {first_name}!</div>', unsafe_allow_html=True)

def show_question():
    """Show feeling question"""
    st.markdown('<div class="question">How are you feeling today?</div>', unsafe_allow_html=True)

def show_slider():
    """Show enhanced slider with emojis"""
    confidence = st.slider("", min_value=1, max_value=10, value=5, label_visibility="collapsed")
    
    # Emoji indicators
    st.markdown("""
        <div class="slider-emoji-row">
            <span>😰</span>
            <span>😐</span>
            <span>😊</span>
            <span>😄</span>
            <span>🔥</span>
        </div>
    """, unsafe_allow_html=True)
    
    return confidence

def show_generate_button():
    """Show generate button with contrast"""
    return st.button("🎲 Generate Challenges For Today", use_container_width=True)

def show_quote(quote):
    """Show inspirational quote"""
    st.markdown(f'<div class="quote-box">"{quote}"</div>', unsafe_allow_html=True)

def show_challenge_card(challenge, current_idx, total_challenges, on_prev, on_next, on_complete):
    """Show Pokemon/Sports card style challenge with internal navigation"""
    difficulty_stars = "⭐" * min(5, max(1, {"easy": 1, "medium": 2, "hard": 3, "superhard": 4, "challenge": 4, "boss": 5, "creative": 2}.get(challenge['difficulty'], 1)))
    
    st.markdown(f"""
        <div class="challenge-card">
            <div class="challenge-title">Challenge #{current_idx + 1}</div>
            <div class="challenge-text">{challenge['text']}</div>
            <div style="text-align: center;">
                <span class="difficulty-badge">Difficulty: {difficulty_stars}</span>
            </div>
            <div class="challenge-description">
                <strong>💡 How to do it:</strong><br/>
                {CHALLENGE_INSTRUCTIONS.get(challenge['difficulty'], 'Be confident and authentic!')}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation with arrows on both sides and complete in middle
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        # Left arrow - loop to last challenge
        if st.button("←", key=f"prev_{current_idx}", help="Previous challenge"):
            on_prev()
    
    with col2:
        if st.button("✅ Complete Challenge", key=f"complete_{current_idx}", use_container_width=True):
            on_complete(challenge)
    
    with col3:
        # Right arrow - loop to first challenge
        if st.button("→", key=f"next_{current_idx}", help="Next challenge"):
            on_next()

def show_loading(quote, seconds):
    """Show loading with animation"""
    st.markdown(f"""
        <div class="loading-container">
            <div class="loading-spinner">🎮</div>
            <div class="loading-title">Creating Your Perfect Challenges...</div>
            <div class="quote-box">"{quote}"</div>
            <div style="font-size: 16px; color: #ffffff; margin-top: 20px; font-weight: 600;">
                ⏱️ {seconds} seconds...
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_report_card(successful, rejections, avg_confidence, streak):
    """Show gamified report card"""
    st.markdown('<div class="report-title">🏆 Your Report Card 🏆</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{successful}</div>
                <div class="stat-label">Successful<br/>interactions for<br/>the week</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{rejections}</div>
                <div class="stat-label">Rejections for<br/>the week</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{avg_confidence if avg_confidence else "0"}</div>
                <div class="stat-label">Average<br/>confidence for<br/>the week</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{streak}</div>
                <div class="stat-label">Days streak<br/>maintained</div>
            </div>
        </div>
    """, unsafe_allow_html=True)