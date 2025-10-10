import streamlit as st
from pathlib import Path
import json, random, datetime
from typing import List, Dict

# -------------------------
# Config / Data
# -------------------------
SAVE_PATH = Path.home() / ".social_xp_streamlit.json"

# XP by difficulty
XP_BY_DIFFICULTY = {
    "easy": 5,
    "medium": 10,
    "hard": 20,
    "challenge": 25,
    "boss": 35,
    "creative": 8,
}

# Full 100 challenges (id: (description, difficulty))
CHALLENGES = {
1: ("Smile at 5 strangers.", "easy"),
2: ("Compliment someone's shoes.", "easy"),
3: ("Ask someone what time it is.", "easy"),
4: ("Say 'Have a good day' to a cashier.", "easy"),
5: ("Ask for directions even if you know the way.", "easy"),
6: ("Tell a friend they look great today.", "easy"),
7: ("Hold eye contact with someone for 3 seconds and smile.", "easy"),
8: ("Ask someone's name and remember it.", "easy"),
9: ("Ask someone about their weekend plans.", "easy"),
10: ("Ask someone how their day's going — and actually listen.", "easy"),
11: ("Compliment someone's hairstyle.", "easy"),
12: ("Ask a waiter/waitress for their food recommendation.", "easy"),
13: ("Say 'You have a good vibe' to someone.", "easy"),
14: ("Ask a stranger where they're from.", "easy"),
15: ("Introduce yourself to someone in your gym/café.", "easy"),
16: ("Wave or say hi to a neighbor.", "easy"),
17: ("Start small talk in a queue.", "easy"),
18: ("Ask a coworker/classmate for a small favor.", "easy"),
19: ("Hold the door open for someone and make eye contact.", "easy"),
20: ("Ask someone what music they're listening to.", "easy"),
21: ("Ask someone's opinion on something ('Which coffee's better?').", "medium"),
22: ("Start a convo about the weather — make it funny.", "medium"),
23: ("Ask someone about their outfit ('That's cool — where'd you get it?').", "medium"),
24: ("Ask a stranger to take your photo.", "medium"),
25: ("Ask for help choosing between two things in a store.", "medium"),
26: ("Ask a stranger about a tattoo or accessory they have.", "medium"),
27: ("Give a genuine compliment to someone of the opposite gender.", "medium"),
28: ("Ask someone what their dream job is.", "medium"),
29: ("Ask a classmate/coworker what motivates them.", "medium"),
30: ("Ask a stranger if they believe in luck.", "medium"),
31: ("Ask someone for a restaurant recommendation.", "medium"),
32: ("Start a random convo on the elevator.", "medium"),
33: ("Ask someone what their favorite childhood cartoon was.", "medium"),
34: ("Ask someone what phone app they can't live without.", "medium"),
35: ("Compliment someone's confidence.", "medium"),
36: ("Ask someone's opinion on a trending topic.", "medium"),
37: ("Ask someone if they prefer cats or dogs — and debate playfully.", "medium"),
38: ("Ask someone to teach you a handshake.", "medium"),
39: ("Make someone laugh intentionally.", "medium"),
40: ("Ask a stranger what book they're reading.", "medium"),
41: ("Ask someone to high-five you.", "hard"),
42: ("Ask a stranger to dance for 30 seconds.", "hard"),
43: ("Challenge someone to a quick game (rock-paper-scissors, Uno, etc.).", "hard"),
44: ("Ask someone for their phone number or Instagram.", "hard"),
45: ("Ask someone out for coffee or juice.", "hard"),
46: ("Ask a random person for fashion advice.", "hard"),
47: ("Ask someone to rate your outfit from 1–10.", "hard"),
48: ("Ask someone what they'd do if they won ₹1 crore.", "hard"),
49: ("Compliment someone in a creative/funny way.", "hard"),
50: ("Ask someone if you can take a selfie together.", "hard"),
51: ("Offer to buy a stranger coffee.", "hard"),
52: ("Ask someone what their biggest dream is.", "hard"),
53: ("Tell someone, 'You seem like someone I'd get along with.'", "hard"),
54: ("Ask a stranger what makes them happy.", "hard"),
55: ("Ask someone if you can join their group for 5 minutes.", "hard"),
56: ("Do a mini social experiment — like giving compliments to 10 people.", "hard"),
57: ("Ask someone to recommend a movie or song.", "hard"),
58: ("Ask a group of people a fun question ('What's your spirit animal?').", "hard"),
59: ("Ask a stranger to describe their perfect day.", "hard"),
60: ("Tell someone, 'You look like someone who does interesting things.'", "hard"),
61: ("Ask for a 10% discount on something random.", "challenge"),
62: ("Ask a stranger to borrow their phone for a quick call (then explain it's a social challenge).", "challenge"),
63: ("Ask someone if they want to play a quick public game (UNO, chess, etc.).", "challenge"),
64: ("Ask for directions to a place that doesn't exist (then laugh about it).", "challenge"),
65: ("Ask someone to teach you a TikTok dance.", "challenge"),
66: ("Ask someone if you can record a 10-second 'positive message' for your challenge.", "challenge"),
67: ("Give out 3 compliments in a row without expecting a reply.", "challenge"),
68: ("Ask someone to sing one line of their favorite song with you.", "challenge"),
69: ("Ask for a fist bump from 5 strangers.", "challenge"),
70: ("Tell someone you're doing a 'social confidence game' and ask them to join one mini challenge.", "challenge"),
71: ("Lead a mini group activity (like a fun question circle).", "boss"),
72: ("Ask someone to freestyle dance with you for 15 seconds.", "boss"),
73: ("Do a 15-second funny public challenge (sing, dance, joke).", "boss"),
74: ("Ask a stranger for life advice.", "boss"),
75: ("Start a 'Would you rather?' convo with 3 people.", "boss"),
76: ("Ask someone to tell you something they've never told anyone.", "boss"),
77: ("Join a group convo mid-way (naturally, not awkwardly).", "boss"),
78: ("Ask a group to vote on something you're wearing or buying.", "boss"),
79: ("Ask someone to be your 1-minute podcast guest.", "boss"),
80: ("Ask someone to give you a random dare (as long as it's safe).", "boss"),
81: ("Ask someone to teach you one word in their language.", "creative"),
82: ("Ask someone to pose for a random photo idea.", "creative"),
83: ("Give a compliment in rhyme form.", "creative"),
84: ("Ask someone what superpower they'd want.", "creative"),
85: ("Start a fake 'street interview' for fun.", "creative"),
86: ("Ask someone their life motto.", "creative"),
87: ("Ask someone to join you for a quick dance reel.", "creative"),
88: ("Ask someone to teach you their favorite slang word.", "creative"),
89: ("Ask someone to guess your job or hobby.", "creative"),
90: ("Ask a stranger to rate your handshake.", "creative"),
91: ("Compliment someone's energy instead of looks.", "creative"),
92: ("Ask someone if they'd rather live in space or underwater.", "creative"),
93: ("Ask someone if they'd trade lives with anyone.", "creative"),
94: ("Ask someone what they'd tell their younger self.", "creative"),
95: ("Ask someone what their favorite smell is (weird = good).", "creative"),
96: ("Ask someone to draw something random for you.", "creative"),
97: ("Ask someone to tell you a joke.", "creative"),
98: ("Ask someone what song defines their life right now.", "creative"),
99: ("Ask someone to join you in saying something positive out loud.", "creative"),
100: ("Give a stranger a sincere compliment and walk away.", "creative"),
}

# -------------------------
# Helpers: storage & logic
# -------------------------
def load_data():
    if SAVE_PATH.exists():
        try:
            return json.loads(SAVE_PATH.read_text())
        except Exception:
            return {}
    return {}

def save_data(data):
    SAVE_PATH.write_text(json.dumps(data, indent=2))

def get_today_str():
    return datetime.date.today().isoformat()

def calc_level(total_xp: int) -> int:
    return 1 + total_xp // 100

def deterministic_daily_picks(seed_str: str, n: int = 5) -> List[int]:
    keys = sorted(list(CHALLENGES.keys()))
    rnd = random.Random(seed_str)
    picks = rnd.sample(keys, k=min(n, len(keys)))
    return picks

# -------------------------
# Page Config & Styling
# -------------------------
st.set_page_config(page_title="Social XP Game 🎮", page_icon="🎲", layout="centered")

st.markdown("""
    <style>
    /* Dark theme text fixes */
    body {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Challenge card styling */
    .challenge-card {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 16px;
        margin: 10px 0;
        color: #ffffff;
    }
    
    .challenge-title {
        font-size: 16px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 8px;
    }
    
    .challenge-meta {
        font-size: 12px;
        color: #a0a0a0;
    }
    
    .big-title {
        font-size: 34px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    /* Better button styling */
    .stButton > button {
        width: 100%;
        background-color: #1f6feb;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 8px 16px;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #388bfd;
    }
    
    .stMetric {
        background-color: #1a1a1a;
        padding: 10px;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Main App
# -------------------------
st.markdown("<div class='big-title'>🎮 Social XP — Game Mode</div>", unsafe_allow_html=True)
st.write("Pick daily challenges, complete them, gain XP, and level up. Make social practice fun!")

# Sidebar controls
with st.sidebar:
    st.header("Player")
    if "nickname" not in st.session_state:
        st.session_state["nickname"] = "Player"
    
    nickname = st.text_input("Nickname (local)", value=st.session_state["nickname"], max_chars=22)
    if not nickname:
        nickname = "Player"
    st.session_state["nickname"] = nickname

    st.markdown("---")
    
    if st.button("🎲 Draw today's 5 challenges", use_container_width=True):
        today = get_today_str()
        seed = nickname + "_" + today
        picks = deterministic_daily_picks(seed, n=5)
        
        data = load_data()
        ud = data.get(nickname, {"total_xp": 0, "completed": [], "last_played": None, "streak": 0})
        ud["last_picks"] = {"date": today, "picks": picks}
        data[nickname] = ud
        save_data(data)
        st.success("✅ Today's challenges drawn!")
        st.rerun()

    st.markdown("---")
    st.markdown("**Reset progress**")
    confirm = st.text_input("Type RESET to confirm", value="", key="reset_input")
    if st.button("Reset progress now", use_container_width=True):
        if confirm.strip().upper() == "RESET":
            data = load_data()
            if nickname in data:
                data.pop(nickname, None)
                save_data(data)
            st.success("✅ Progress reset. Refreshing...")
            st.rerun()
        else:
            st.error("Type RESET in the box above to confirm.")

# Load user data
data = load_data()
user_data = data.get(nickname, {"total_xp": 0, "completed": [], "last_played": None, "streak": 0})

# Display metrics
col1, col2, col3 = st.columns([1.2, 1, 1])
with col1:
    st.metric("Level", f"{calc_level(user_data['total_xp'])} ⭐")
with col2:
    st.metric("XP", f"{user_data['total_xp']} XP")
with col3:
    st.metric("Streak", f"{user_data.get('streak', 0)} days 🔥")

level = calc_level(user_data["total_xp"])
xp_into_level = user_data["total_xp"] - (level - 1) * 100
xp_next = 100
st.write(f"Progress to next level: **{xp_into_level}/{xp_next} XP**")
st.progress(min(1.0, xp_into_level / xp_next))

st.markdown("---")

# Today's challenges
today = get_today_str()
last_picks_info = user_data.get("last_picks", {})

if last_picks_info.get("date") != today:
    # Generate new picks for today
    seed = nickname + "_" + today
    picks = deterministic_daily_picks(seed, n=5)
    user_data["last_picks"] = {"date": today, "picks": picks}
    data[nickname] = user_data
    save_data(data)
else:
    picks = last_picks_info.get("picks", [])

st.markdown("### 🎯 Today's Challenges")
completed_today_ids = {c["id"] for c in user_data.get("completed", []) if c["date"] == today}

for cid in picks:
    desc, diff = CHALLENGES.get(cid, ("(missing)", "easy"))
    xp = XP_BY_DIFFICULTY.get(diff, 5)
    
    # Display challenge card
    st.markdown(f"""
        <div class='challenge-card'>
            <div class='challenge-title'>#{cid} — {desc}</div>
            <div class='challenge-meta'>{diff.upper()} • {xp} XP</div>
        </div>
    """, unsafe_allow_html=True)
    
    if cid in completed_today_ids:
        st.success(f"✅ Completed today (+{xp} XP)")
    else:
        if st.button(f"Complete #{cid} (+{xp} XP)", key=f"complete_{cid}"):
            already = any((c["id"] == cid and c["date"] == today) for c in user_data.get("completed", []))
            if not already:
                user_data["total_xp"] = user_data.get("total_xp", 0) + xp
                user_data.setdefault("completed", []).append({"id": cid, "date": today, "xp": xp, "desc": desc})
                
                # Update streak
                last = user_data.get("last_played")
                if last:
                    try:
                        last_date = datetime.date.fromisoformat(last)
                    except Exception:
                        last_date = None
                else:
                    last_date = None
                
                if last_date == datetime.date.today() - datetime.timedelta(days=1):
                    user_data["streak"] = user_data.get("streak", 0) + 1
                elif last_date == datetime.date.today():
                    pass
                else:
                    user_data["streak"] = 1
                
                user_data["last_played"] = today
                data[nickname] = user_data
                save_data(data)
                st.success(f"🎉 +{xp} XP earned!")
                st.rerun()
            else:
                st.info("Already recorded today.")

st.markdown("---")
st.markdown("### 📜 Recent completions")
recent = user_data.get("completed", [])[-10:]
if recent:
    for c in reversed(recent):
        st.write(f"• **#{c['id']}** on {c['date']} → **+{c['xp']} XP** — {c.get('desc', '')}")
else:
    st.write("_No completions yet. Try today's challenges!_")

st.markdown("---")
st.markdown("### 🏆 Local leaderboard (this machine)")
if data:
    leaderboard = []
    for name, ud in data.items():
        leaderboard.append((name, ud.get("total_xp", 0), ud.get("streak", 0)))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    for i, (name, xp, streak_) in enumerate(leaderboard[:10], start=1):
        st.write(f"{i}. **{name}** — {xp} XP | streak: {streak_} 🔥")
else:
    st.write("_No players yet._")

st.markdown("---")
st.info("💡 Tip: Use a nickname to keep local progress. For production, consider using Google Sheets or Supabase for per-user persistence.")
