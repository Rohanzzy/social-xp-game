import streamlit as st
from pathlib import Path
import json
import random
import datetime
import time
from typing import List, Dict

# Page config
st.set_page_config(page_title="Social XP Game 🎮", layout="wide", initial_sidebar_state="collapsed")

# CSS Styling
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2d1b69 100%);
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
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Data & Config
# -------------------------
SAVE_PATH = Path.home() / ".social_xp_game.json"

SOCIALIZATION_QUOTES = [
    '"Every conversation is a chance to change someone\'s day." - Anonymous',
    '"Connection is the antidote to isolation." - Brené Brown',
    '"The greatest gift you can give is your presence." - Oprah',
    '"Real human connection is at the heart of everything." - Brian Chesky',
    '"We\'re hardwired to connect with other people." - Daniel Goleman',
    '"You can\'t stay in your corner waiting for others to come to you." - Winnie the Pooh',
    '"Social connection is as vital as any physical activity." - Research',
    '"The best way to find yourself is in service to others." - Gandhi',
]

CONFIDENCE_LABELS = {
    1: "😰 Not ready - maybe tomorrow",
    2: "😔 Bit nervous - small steps only",
    3: "😐 Neutral - let's ease in",
    4: "🙂 Getting there - some social time",
    5: "😊 Decent - can do easy stuff",
    6: "🤔 Ready - let's try medium challenges",
    7: "😄 Confident - bring it on",
    8: "🔥 Very confident - I got this",
    9: "💪 Super confident - challenge me",
    10: "🚀 Unstoppable - I can talk to ANYONE"
}

CHALLENGE_INSTRUCTIONS = {
    "easy": "Approach with a simple, friendly greeting. Smile and be genuine. Keep it brief and light.",
    "medium": "Start a real conversation. Ask follow-up questions and actually listen. Be curious and authentic.",
    "hard": "Go deeper. Exchange contact info if appropriate. Be vulnerable and show genuine interest.",
    "superhard": "Push your limits. Lead the interaction. Be confident and inspiring. Make it memorable."
}

CHALLENGES_DB = {
    "easy": [
        "Smile at 5 strangers.", "Compliment someone's shoes.", "Ask someone what time it is.",
        "Say 'Have a good day' to a cashier.", "Ask for directions even if you know the way.",
        "Tell a friend they look great today.", "Hold eye contact with someone for 3 seconds and smile.",
        "Ask someone's name and remember it.", "Ask someone about their weekend plans.",
        "Ask someone how their day's going — and actually listen.", "Compliment someone's hairstyle.",
        "Ask a waiter/waitress for their food recommendation.", "Say 'You have a good vibe' to someone.",
        "Ask a stranger where they're from.", "Introduce yourself to someone in your gym/café.",
        "Wave or say hi to a neighbor.", "Start small talk in a queue.",
        "Ask a coworker/classmate for a small favor.", "Hold the door open for someone and make eye contact.",
        "Ask someone what music they're listening to.", "Compliment someone's smile.",
        "Ask a stranger their favorite food.", "Say thank you with a smile.", "Compliment someone's jewelry.",
        "Ask someone's opinion on the weather.", "Make eye contact and nod to someone.",
        "Ask someone where they get their energy.", "Compliment someone's handwriting.",
        "Ask if they know a good place to eat nearby.", "Tell someone you like their positive energy.",
        "Ask about their pet.", "Compliment their color choice.", "Ask 'What made you smile today?'",
        "Say 'You seem really cool' to someone.", "Ask if they've been somewhere cool recently.",
        "Compliment someone's phone case.", "Ask their go-to comfort food.", "Tell someone they have nice eyes.",
        "Ask a stranger their favorite music.", "Smile genuinely at someone.",
        "Ask 'What's something good that happened to you?'", "Compliment someone's laugh.",
        "Ask a stranger for an opinion.", "Tell someone they're having a good day.",
        "Ask what hobby they're passionate about.", "Compliment a visible tattoo.",
        "Ask 'What's your favorite season?'", "Tell someone they have a friendly face.",
        "Ask what they love about their job.", "Compliment their effort or hard work.",
    ],
    "medium": [
        "Ask someone's opinion on something like 'Which coffee is better?'",
        "Start a funny conversation about the weather.",
        "Ask someone about their outfit and where they got it.",
        "Ask a stranger to take your photo.",
        "Ask for help choosing between two things in a store.",
        "Ask a stranger about their tattoo or accessory.",
        "Give a genuine compliment to someone of the opposite gender.",
        "Ask someone what their dream job is.",
        "Ask what motivates them.",
        "Ask a stranger if they believe in luck.",
        "Ask for a restaurant recommendation.",
        "Start a random conversation on the elevator.",
        "Ask someone about their favorite childhood cartoon.",
        "Ask about their favorite phone app.",
        "Compliment someone's confidence.",
        "Ask someone's opinion on a trending topic.",
        "Ask if they prefer cats or dogs and debate playfully.",
        "Ask someone to teach you a handshake.",
        "Make someone laugh intentionally.",
        "Ask a stranger what book they're reading.",
        "Ask what skill they wish they had.",
        "Start a conversation about a TV show or movie.",
        "Ask what country they'd love to visit.",
        "Compliment someone on their work or project.",
        "Ask about their biggest achievement.",
        "Start a conversation about a popular podcast.",
        "Ask what makes them feel alive.",
        "Compliment their communication skills.",
        "Ask what they're grateful for today.",
        "Start a conversation about travel experiences.",
        "Ask about their favorite childhood memory.",
        "Compliment their creativity.",
        "Ask what they'd do on a perfect day.",
        "Start a conversation about learning something new.",
        "Ask what inspires them the most.",
        "Compliment them on handling a tough situation.",
        "Ask what their hidden talent is.",
        "Start a conversation about dreams or goals.",
        "Ask what makes them unique.",
        "Compliment their perspective or wisdom.",
        "Ask what adventure they're planning.",
        "Start a conversation about personal growth.",
        "Ask what legacy they want to leave.",
        "Compliment their patience or kindness.",
        "Ask what they're excited about.",
        "Start a conversation about a shared interest.",
        "Ask what success means to them.",
        "Compliment their authenticity.",
        "Ask what they do to stay motivated.",
        "Start a conversation about meaningful life lessons.",
    ],
    "hard": [
        "Ask someone to high-five you.", "Ask a stranger to dance for 30 seconds.",
        "Challenge someone to rock-paper-scissors.", "Ask for their phone number or Instagram.",
        "Ask someone out for coffee or juice.", "Ask a random person for fashion advice.",
        "Ask someone to rate your outfit from 1-10.", "Ask what they'd do if they won ₹1 crore.",
        "Compliment someone in a creative/funny way.", "Ask if you can take a selfie together.",
        "Offer to buy a stranger coffee.", "Ask about their biggest dream.",
        "Tell someone 'You seem like someone I'd get along with.'", "Ask a stranger what makes them happy.",
        "Ask if you can join their group for 5 minutes.", "Give compliments to 10 people.",
        "Ask someone to recommend a movie or song.", "Ask a group a fun question.",
        "Ask a stranger to describe their perfect day.", "Tell someone 'You look like someone who does interesting things.'",
        "Start a philosophical debate.", "Ask someone to be your accountability partner.",
        "Challenge someone to trivia.", "Ask for career advice.", "Invite someone for a meal.",
        "Ask someone to mentor you.", "Start a project idea with a stranger.",
        "Ask someone to be part of a fun challenge.", "Pitch an idea and ask for feedback.",
        "Ask about their biggest life lesson.", "Invite someone to an event.",
        "Ask someone to teach you their craft.", "Propose starting a group together.",
        "Ask about overcoming their fear.", "Invite a stranger on an adventure.",
        "Ask someone to collaborate on something creative.", "Challenge someone to step out of their comfort zone.",
        "Ask what superpower they'd choose.", "Invite someone to join your social mission.",
        "Ask someone to share their most vulnerable moment.", "Start a conversation about life purpose.",
        "Ask someone to help with a personal goal.", "Invite someone to a networking event.",
        "Ask what advice they'd give their younger self.", "Challenge someone to try something new.",
        "Ask about their most transformative experience.", "Invite someone to start a habit with you.",
        "Ask someone to share their success story.", "Start a conversation about mental health.",
        "Ask if they'd be open to being friends.",
    ],
    "superhard": [
        "Ask for a 10% discount on something.", "Ask to borrow a stranger's phone for a call.",
        "Ask someone to play a public game with you.", "Ask for directions to a nonexistent place (then laugh).",
        "Ask someone to teach you a TikTok dance.", "Ask to record a positive message for your challenge.",
        "Give 3 compliments in a row.", "Ask someone to sing with you.", "Ask for fist bumps from 5 strangers.",
        "Tell someone about your social confidence game.", "Lead a mini group activity.",
        "Ask someone to freestyle dance with you.", "Do a 15-second funny public challenge.",
        "Ask a stranger for life advice.", "Start a 'Would you rather?' game with 3 people.",
        "Ask someone to tell you something secret.", "Join a group conversation naturally.",
        "Ask a group to vote on something.", "Ask someone to be your podcast guest.",
        "Ask someone to give you a random dare.", "Start a spontaneous street performance.",
        "Ask 5 strangers to share their life motto.", "Lead someone through a personal growth exercise.",
        "Ask someone to be part of a social experiment.", "Organize an impromptu group activity.",
        "Ask someone to share their biggest fear.", "Start a conversation about life purpose with a group.",
        "Ask 10 people for advice on a decision.", "Lead a group challenge.",
        "Ask someone to help inspire others.", "Start a social movement.",
        "Ask a group to participate in kindness.", "Organize a group discussion.",
        "Ask someone to mentor you publicly.", "Start a community building activity.",
        "Ask people to share transformation stories.", "Lead a workshop.",
        "Ask people to contribute to a creative project.", "Start a support circle.",
        "Ask a group to help someone in need.", "Organize a flash mob.",
        "Ask people to participate in a cause.", "Lead a group exercise.",
        "Ask a group to create something together.", "Start a mentorship circle.",
        "Ask people to celebrate wins together.", "Lead a group on an adventure.",
    ],
}

XP_BY_DIFFICULTY = {"easy": 5, "medium": 10, "hard": 20, "superhard": 35}

# -------------------------
# Helpers
# -------------------------
def load_data():
    if SAVE_PATH.exists():
        try:
            return json.loads(SAVE_PATH.read_text())
        except:
            return {}
    return {}

def save_data(data):
    SAVE_PATH.write_text(json.dumps(data, indent=2))

def get_today():
    return datetime.date.today().isoformat()

def calc_level(xp):
    return 1 + (xp // 100)

def get_challenges_by_confidence(confidence):
    """Return challenge distribution based on confidence level (1-10)"""
    if confidence <= 3:
        return {"easy": 4, "medium": 1, "hard": 0, "superhard": 0}
    elif confidence <= 5:
        return {"easy": 2, "medium": 2, "hard": 1, "superhard": 0}
    elif confidence <= 7:
        return {"easy": 1, "medium": 2, "hard": 2, "superhard": 0}
    else:
        return {"easy": 0, "medium": 1, "hard": 3, "superhard": 1}

def generate_daily_challenges(confidence):
    """Generate 5 challenges based on confidence"""
    distribution = get_challenges_by_confidence(confidence)
    challenges = []
    
    for difficulty, count in distribution.items():
        pool = CHALLENGES_DB[difficulty]
        selected = random.sample(pool, min(count, len(pool)))
        for challenge_text in selected:
            challenges.append({"text": challenge_text, "difficulty": difficulty, "xp": XP_BY_DIFFICULTY[difficulty]})
    
    return challenges

# -------------------------
# Session State Init
# -------------------------
if "user_name" not in st.session_state:
    st.session_state.user_name = "Player"
if "confidence" not in st.session_state:
    st.session_state.confidence = None
if "challenges" not in st.session_state:
    st.session_state.challenges = []
if "loading" not in st.session_state:
    st.session_state.loading = False

# -------------------------
# Main UI
# -------------------------
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<div style='font-size: 48px; font-weight: 900; background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🎮 SOCIAL XP</div>", unsafe_allow_html=True)
    st.markdown("<div style='color: #22d3ee; font-size: 14px; font-weight: 900; letter-spacing: 2px;'>LEVEL UP YOUR SOCIAL CONFIDENCE</div>", unsafe_allow_html=True)

st.markdown("---")

# =====================
# WELCOME & CONFIDENCE SECTION
# =====================
st.markdown("<div style='font-size: 32px; font-weight: 900;'>Hey <span style='background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{}</span>, how's it going? 🚀</div>".format(st.session_state.user_name), unsafe_allow_html=True)
st.write("Ready to build some social confidence today?")

st.markdown("---")

# Confidence slider
st.markdown("#### 🎯 How confident are you feeling today?")
confidence = st.slider("Pick a number:", min_value=1, max_value=10, value=5, label_visibility="collapsed")

# Show confidence label with big font
st.markdown(f"""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%); border-radius: 15px; border: 3px solid #06b6d4; margin: 20px 0;'>
        <div style='font-size: 64px; font-weight: 900; background: linear-gradient(90deg, #06b6d4 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 15px;'>{confidence}/10</div>
        <div style='color: #22d3ee; font-size: 22px; font-weight: 700;'>{CONFIDENCE_LABELS[confidence]}</div>
    </div>
""", unsafe_allow_html=True)

st.session_state.confidence = confidence

# Generate challenges button
if st.button("🎲 GENERATE CHALLENGES", use_container_width=True, key="gen_challenges"):
    st.session_state.loading = True
    st.session_state.challenges = []

# Loading screen with quotes
if st.session_state.loading:
    with st.container():
        st.markdown("<div style='text-align: center; padding: 40px;'><div style='font-size: 24px; font-weight: 900; margin-bottom: 20px;'>✨ Creating Your Perfect Challenges...</div></div>", unsafe_allow_html=True)
        
        # Show one quote for 5 seconds
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
        
        # Generate challenges
        st.session_state.challenges = generate_daily_challenges(confidence)
        st.session_state.loading = False
        st.rerun()

st.markdown("---")

# =====================
# STATS SECTION
# =====================
st.markdown("<div style='font-size: 28px; font-weight: 900; margin: 30px 0 20px 0;'>📊 Your Stats</div>", unsafe_allow_html=True)

data = load_data()
user_data = data.get(st.session_state.user_name, {"total_xp": 0, "completed": 0, "streak": 0, "avg_confidence": 0})

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
with stat_col1:
    st.markdown(f"""
        <div style='background: rgba(34, 197, 94, 0.2); padding: 25px; border-radius: 12px; border: 2px solid #22c55e; text-align: center;'>
            <div style='font-size: 14px; color: #a0a0a0; margin-bottom: 10px; font-weight: 600;'>⚡ TOTAL XP</div>
            <div style='font-size: 40px; font-weight: 900; color: #22c55e;'>{user_data.get("total_xp", 0)}</div>
        </div>
    """, unsafe_allow_html=True)
with stat_col2:
    st.markdown(f"""
        <div style='background: rgba(59, 130, 246, 0.2); padding: 25px; border-radius: 12px; border: 2px solid #3b82f6; text-align: center;'>
            <div style='font-size: 14px; color: #a0a0a0; margin-bottom: 10px; font-weight: 600;'>🏆 COMPLETED</div>
            <div style='font-size: 40px; font-weight: 900; color: #3b82f6;'>{user_data.get("completed", 0)}</div>
        </div>
    """, unsafe_allow_html=True)
with stat_col3:
    st.markdown(f"""
        <div style='background: rgba(239, 68, 68, 0.2); padding: 25px; border-radius: 12px; border: 2px solid #ef4444; text-align: center;'>
            <div style='font-size: 14px; color: #a0a0a0; margin-bottom: 10px; font-weight: 600;'>🔥 STREAK</div>
            <div style='font-size: 40px; font-weight: 900; color: #ef4444;'>{user_data.get("streak", 0)}</div>
        </div>
    """, unsafe_allow_html=True)
with stat_col4:
    avg_conf = user_data.get("avg_confidence", 0)
    st.markdown(f"""
        <div style='background: rgba(168, 85, 247, 0.2); padding: 25px; border-radius: 12px; border: 2px solid #a855f7; text-align: center;'>
            <div style='font-size: 14px; color: #a0a0a0; margin-bottom: 10px; font-weight: 600;'>💪 AVG CONFIDENCE</div>
            <div style='font-size: 40px; font-weight: 900; color: #a855f7;'>{f"{avg_conf}/10" if avg_conf else "N/A"}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =====================
# CHALLENGES DISPLAY
# =====================
if st.session_state.challenges:
    st.markdown("#### 🎯 Your Challenges Today")
    
    for idx, challenge in enumerate(st.session_state.challenges):
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
            # Update data
            data = load_data()
            user_data = data.get(st.session_state.user_name, {"total_xp": 0, "completed": 0, "streak": 0})
            user_data["total_xp"] = user_data.get("total_xp", 0) + challenge["xp"]
            user_data["completed"] = user_data.get("completed", 0) + 1
            user_data["streak"] = user_data.get("streak", 0) + 1
            data[st.session_state.user_name] = user_data
            save_data(data)
            st.success(f"🎉 +{challenge['xp']} XP!")
            st.rerun()

else:
    st.info("👈 Select your confidence level and click 'Generate Challenges' to get started!")
