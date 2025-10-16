# storage.py - Handle user data persistence

import json
from pathlib import Path
import datetime

SAVE_PATH = Path.home() / ".social_xp_game.json"

def load_data():
    """Load all user data from JSON file"""
    if SAVE_PATH.exists():
        try:
            return json.loads(SAVE_PATH.read_text())
        except:
            return {}
    return {}

def save_data(data):
    """Save all user data to JSON file"""
    SAVE_PATH.write_text(json.dumps(data, indent=2))

def get_today():
    """Get today's date as ISO string"""
    return datetime.date.today().isoformat()

def get_user_data(username):
    """Get specific user's data"""
    data = load_data()
    return data.get(username, {
        "total_xp": 0,
        "completed": 0,
        "rejections": 0,
        "streak": 0,
        "avg_confidence": 0,
        "successful": 0
    })

def update_user_data(username, **kwargs):
    """Update user data with given fields"""
    data = load_data()
    user_data = data.get(username, {
        "total_xp": 0,
        "completed": 0,
        "streak": 0,
        "avg_confidence": 0
    })
    
    user_data.update(kwargs)
    data[username] = user_data
    save_data(data)