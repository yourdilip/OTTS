from bot.config import PREMIUM_LIMIT

# A simple dictionary to manage premium users and their limits
premium_users = {}

def add_premium(user_id, videos, days):
    premium_users[user_id] = {'videos': videos, 'days': days}

def remove_premium(user_id):
    if user_id in premium_users:
        del premium_users[user_id]

def check_premium_status():
    return premium_users

def get_stats():
    return {"total_users": len(premium_users)}
  
