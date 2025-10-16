# ui.py - Clean design based on wireframe

import streamlit as st
from config import CHALLENGE_INSTRUCTIONS

def apply_theme():
    """Apply clean, minimal theme"""
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        }
        
        [data-testid="stMainBlockContainer"] {
            max-width: 500px;
            margin: 0 auto;
            padding: 24px 16px;
        }
        
        /* Typography */
        body, p, span, div, label, input {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .main-title {
            font-size: 32px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 32px;
        }
        
        .question {
            font-size: 20px;
            font-weight: 500;
            color: #e0e0e0;
            text-align: center;
            margin-bottom: 24px;
        }
        
        /* Slider styling */
        .stSlider {
            padding: 20px 0;
        }
        
        /* Button */
        .stButton > button {
            width: 100%;
            background: #ffffff !important;
            color: #1a1a2e !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 14px !important;
            font-size: 16px !important;
            margin: 24px 0 !important;
            transition: all 0.2s !important;
        }
        
        .stButton > button:hover {
            background: #e0e0e0 !important;
            transform: translateY(-2px) !important;
        }
        
        /* Quote box */
        .quote-box {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            margin: 24px 0;
            font-style: italic;
            color: #e0e0e0;
            font-size: 14px;
            line-height: 1.6;
        }
        
        /* Challenge card */
        .challenge-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 24px;
            margin: 24px 0;
            min-height: 300px;
        }
        
        .challenge-title {
            font-size: 22px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .challenge-text {
            font-size: 18px;
            font-weight: 500;
            color: #ffffff;
            text-align: center;
            margin: 20px 0;
        }
        
        .difficulty-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin: 16px 0;
            font-size: 14px;
            color: #e0e0e0;
        }
        
        .challenge-description {
            font-size: 14px;
            color: #b0b0b0;
            line-height: 1.6;
            margin-top: 16px;
            text-align: center;
        }
        
        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 24px;
        }
        
        .nav-button {
            background: none;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            padding: 12px 20px;
            color: #ffffff;
            font-size: 24px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .nav-button:hover {
            border-color: rgba(255, 255, 255, 0.6);
            background: rgba(255, 255, 255, 0.05);
        }
        
        /* Report card */
        .report-title {
            font-size: 24px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin: 40px 0 24px 0;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 40px;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 24px 16px;
            text-align: center;
            aspect-ratio: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .stat-value {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 8px;
        }
        
        .stat-label {
            font-size: 13px;
            color: #b0b0b0;
            line-height: 1.4;
        }
        
        /* Desktop responsive */
        @media (min-width: 768px) {
            [data-testid="stMainBlockContainer"] {
                max-width: 600px;
                padding: 40px 24px;
            }
            
            .main-title {
                font-size: 40px;
            }
            
            .question {
                font-size: 24px;
            }
            
            .challenge-card {
                min-height: 350px;
                padding: 32px;
            }
            
            .stat-value {
                font-size: 56px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def show_welcome(username):
    """Show welcome message"""
    st.markdown(f'<div class="main-title">Welcome back {username}</div>', unsafe_allow_html=True)

def show_question():
    """Show feeling question"""
    st.markdown('<div class="question">How are you feeling today?</div>', unsafe_allow_html=True)

def show_slider():
    """Show confidence slider"""
    confidence = st.slider("", min_value=1, max_value=10, value=5, label_visibility="collapsed")
    return confidence

def show_generate_button():
    """Show generate button"""
    return st.button("Generate challenges for today", use_container_width=True)

def show_quote(quote):
    """Show inspirational quote"""
    st.markdown(f'<div class="quote-box">{quote}</div>', unsafe_allow_html=True)

def show_challenge_card(challenge, current_idx, total_challenges, on_prev, on_next, on_complete):
    """Show single challenge card with navigation"""
    difficulty_stars = "⭐" * min(5, max(1, {"easy": 1, "medium": 2, "hard": 3, "superhard": 4}.get(challenge['difficulty'], 1)))
    
    st.markdown(f"""
        <div class="challenge-card">
            <div class="challenge-title">Challenge #{current_idx + 1}</div>
            <div class="challenge-text">{challenge['text']}</div>
            <div class="difficulty-row">
                <span>Difficulty - {difficulty_stars}</span>
            </div>
            <div class="challenge-description">
                <strong>Description:</strong> {CHALLENGE_INSTRUCTIONS[challenge['difficulty']]}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation and complete buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if current_idx > 0:
            if st.button("←", key=f"prev_{current_idx}"):
                on_prev()
    
    with col2:
        if st.button("Complete", key=f"complete_{current_idx}", use_container_width=True):
            on_complete(challenge)
    
    with col3:
        if current_idx < total_challenges - 1:
            if st.button("→", key=f"next_{current_idx}"):
                on_next()

def show_loading(quote, seconds):
    """Show loading state"""
    st.markdown(f"""
        <div style="text-align: center; padding: 40px 0;">
            <div style="font-size: 20px; font-weight: 600; color: #ffffff; margin-bottom: 20px;">
                Generating your challenges...
            </div>
            <div class="quote-box">{quote}</div>
            <div style="font-size: 14px; color: #b0b0b0; margin-top: 16px;">
                {seconds} seconds remaining...
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_report_card(successful, rejections, avg_confidence, streak):
    """Show report card with 2x2 grid"""
    st.markdown('<div class="report-title">Your Report Card</div>', unsafe_allow_html=True)
    
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
                <div class="stat-value">{avg_confidence}</div>
                <div class="stat-label">Average<br/>confidence for<br/>the week</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{streak}</div>
                <div class="stat-label">Days streak<br/>maintained</div>
            </div>
        </div>
    """, unsafe_allow_html=True)