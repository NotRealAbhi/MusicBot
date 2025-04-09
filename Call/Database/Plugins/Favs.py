"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from Call.Player.Core import call
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import os

# File path to store user favorites
FAVS_FILE = "favs.json"

# Load favorites data from the JSON file
def load_favorites():
    if os.path.exists(FAVS_FILE):
        with open(FAVS_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

# Save favorites data to the JSON file
def save_favorites(favs):
    with open(FAVS_FILE, "w") as file:
        json.dump(favs, file, indent=4)

# Handle user's favorites
favs_data = load_favorites()

@Client.on_message(filters.command("fav") & filters.private)
async def add_favorite(client: Client, message):
    """Add a song to the user's favorites."""
    song_url = message.text.split(" ", 1)
    
    if len(song_url) < 2:
        await message.reply("Please provide the song URL to add to favorites.")
        return
    
    song_url = song_url[1].strip()
    user_id = message.from_user.id

    if user_id not in favs_data:
        favs_data[user_id] = []

    if song_url not in favs_data[user_id]:
        favs_data[user_id].append(song_url)
        save_favorites(favs_data)
        await message.reply(f"Song added to your favorites: {song_url}")
    else:
        await message.reply("This song is already in your favorites.")

@Client.on_message(filters.command("myfavs") & filters.private)
async def list_favorites(client: Client, message):
    """List all songs in the user's favorites."""
    user_id = message.from_user.id

    if user_id in favs_data and favs_data[user_id]:
        favorites = "\n".join(favs_data[user_id])
        await message.reply(f"Your favorite songs:\n{favorites}")
    else:
        await message.reply("You don't have any favorite songs yet.")

@Client.on_message(filters.command("playfav") & filters.private)
async def play_favorite(client: Client, message):
    """Play a song from the user's favorites."""
    song_url = message.text.split(" ", 1)
    
    if len(song_url) < 2:
        await message.reply("Please provide the song URL to play from your favorites.")
        return
    
    song_url = song_url[1].strip()
    user_id = message.from_user.id

    if user_id in favs_data and song_url in favs_data[user_id]:
        chat_id = message.chat.id
        await call.play(chat_id, song_url)
        await message.reply(f"Now playing your favorite song: {song_url}")
    else:
        await message.reply("This song is not in your favorites. Use /fav <song_url> to add it.")
    
@Client.on_message(filters.command("removefav") & filters.private)
async def remove_favorite(client: Client, message):
    """Remove a song from the user's favorites."""
    song_url = message.text.split(" ", 1)
    
    if len(song_url) < 2:
        await message.reply("Please provide the song URL to remove from favorites.")
        return
    
    song_url = song_url[1].strip()
    user_id = message.from_user.id

    if user_id in favs_data and song_url in favs_data[user_id]:
        favs_data[user_id].remove(song_url)
        save_favorites(favs_data)
        await message.reply(f"Song removed from your favorites: {song_url}")
    else:
        await message.reply("This song is not in your favorites.")
      
