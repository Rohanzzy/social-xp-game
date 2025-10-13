# logic.py - Game logic and calculations

import random
from config import CHALLENGES_DB, XP_BY_DIFFICULTY

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
    """Generate 5 challenges based on confidence level"""
    distribution = get_challenges_by_confidence(confidence)
    challenges = []
    
    for difficulty, count in distribution.items():
        pool = CHALLENGES_DB[difficulty]
        selected = random.sample(pool, min(count, len(pool)))
        for challenge_text in selected:
            challenges.append({
                "text": challenge_text,
                "difficulty": difficulty,
                "xp": XP_BY_DIFFICULTY[difficulty]
            })
    
    return challenges

def calc_level(xp):
    """Calculate user level from total XP (100 XP per level)"""
    return 1 + (xp // 100)