"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
import json
import os

# Define the stats file path
STATS_FILE = "bot_stats.json"

# Load statistics from file
def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return {
        "total_users": 0,
        "total_plays": 0,
        "total_time_spent": 0,  # in seconds
    }

# Save statistics to file
def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)

# Update total users count
def update_user_count():
    stats = load_stats()
    stats["total_users"] += 1
    save_stats(stats)

# Update total plays count
def update_total_plays():
    stats = load_stats()
    stats["total_plays"] += 1
    save_stats(stats)

# Update total time spent in VC
def update_total_time_spent(seconds):
    stats = load_stats()
    stats["total_time_spent"] += seconds
    save_stats(stats)

@Client.on_message(filters.command("stats") & filters.group)
async def stats(client: Client, message: Message):
    """Displays the bot usage statistics."""
    stats = load_stats()
    
    total_users = stats.get("total_users", 0)
    total_plays = stats.get("total_plays", 0)
    total_time_spent = stats.get("total_time_spent", 0)
    
    # Format total time spent in hours, minutes, and seconds
    hours, remainder = divmod(total_time_spent, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    formatted_time = f"{hours}h {minutes}m {seconds}s"
    
    # Send the statistics to the user
    await message.reply(
        f"📊 **Bot Statistics**\n"
        f"**Total Users**: {total_users}\n"
        f"**Total Plays**: {total_plays}\n"
        f"**Total Time Spent in VC**: {formatted_time}\n"
        f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

@Client.on_message(filters.command("newuser") & filters.private)
async def new_user(client: Client, message: Message):
    """Updates the user count when a new user interacts with the bot."""
    update_user_count()
    await message.reply("👤 New user count updated!")

@Client.on_message(filters.command("play") & filters.private)
async def play_song(client: Client, message: Message):
    """Updates the play count and time spent in VC when a song is played."""
    update_total_plays()
    update_total_time_spent(180)  # Example: Assume the song lasts 3 minutes (180 seconds)
    await message.reply("🎶 Song is playing...")

@Client.on_message(filters.command("endvc") & filters.private)
async def end_vc(client: Client, message: Message):
    """Updates the total time spent in VC when the session ends."""
    update_total_time_spent(120)  # Example: Assume the VC session lasted 2 minutes (120 seconds)
    await message.reply("🔴 Voice chat ended. Time spent updated.")
  
