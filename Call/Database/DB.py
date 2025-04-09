"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

import os
import json
from pymongo import MongoClient
from Call.Config import MONGO_URL

USE_JSON = False
json_path = "database.json"
db = {}

# Load from JSON if MongoDB not configured
if not MONGO_URL:
    USE_JSON = True
    if os.path.exists(json_path):
        with open(json_path) as f:
            db = json.load(f)
    else:
        db = {"users": {}, "chats": {}, "favorites": {}}
else:
    client = MongoClient(MONGO_URL)
    db = client["MusicBot"]


# Mongo Example Access:
def get_user_stats(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {"plays": 0})
    else:
        return db["users"].find_one({"_id": user_id}) or {"plays": 0}


def save_user_stats(user_id, data):
    if USE_JSON:
        db["users"][str(user_id)] = data
        with open(json_path, "w") as f:
            json.dump(db, f, indent=2)
    else:
        db["users"].update_one({"_id": user_id}, {"$set": data}, upsert=True)


def get_favorites(user_id):
    if USE_JSON:
        return db["favorites"].get(str(user_id), [])
    else:
        user = db["favorites"].find_one({"_id": user_id})
        return user["tracks"] if user else []


def add_favorite(user_id, track):
    if USE_JSON:
        favs = db["favorites"].get(str(user_id), [])
        favs.append(track)
        db["favorites"][str(user_id)] = favs
        with open(json_path, "w") as f:
            json.dump(db, f, indent=2)
    else:
        db["favorites"].update_one(
            {"_id": user_id}, {"$push": {"tracks": track}}, upsert=True
        )
      
