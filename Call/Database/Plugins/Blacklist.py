"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import os

# File path to store blacklist data
BLACKLIST_FILE = "blacklist.json"

# Load blacklist data from the JSON file
def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as file:
            return json.load(file)
    else:
        return {"users": [], "chats": []}

# Save blacklist data to the JSON file
def save_blacklist(blacklist):
    with open(BLACKLIST_FILE, "w") as file:
        json.dump(blacklist, file, indent=4)

# Handle the blacklist data
blacklist_data = load_blacklist()

@Client.on_message(filters.command("blacklist") & filters.private)
async def blacklist_user(client: Client, message):
    """Blacklist a user or chat."""
    if message.from_user.id != 123456789:  # Check for authorized users (e.g., admin)
        await message.reply("You are not authorized to use this command.")
        return
    
    # Extract user or chat info
    command_parts = message.text.split(" ", 1)
    
    if len(command_parts) < 2:
        await message.reply("Please provide a user ID or chat ID to blacklist.")
        return
    
    target_id = command_parts[1].strip()
    
    if target_id.isdigit():
        target_id = int(target_id)
        
        if target_id not in blacklist_data["users"]:
            blacklist_data["users"].append(target_id)
            save_blacklist(blacklist_data)
            await message.reply(f"User {target_id} has been blacklisted.")
        else:
            await message.reply(f"User {target_id} is already blacklisted.")
    else:
        await message.reply("Invalid user or chat ID. Please provide a valid ID.")

@Client.on_message(filters.command("unblacklist") & filters.private)
async def unblacklist_user(client: Client, message):
    """Unblacklist a user or chat."""
    if message.from_user.id != 123456789:  # Check for authorized users (e.g., admin)
        await message.reply("You are not authorized to use this command.")
        return
    
    # Extract user or chat info
    command_parts = message.text.split(" ", 1)
    
    if len(command_parts) < 2:
        await message.reply("Please provide a user ID or chat ID to unblacklist.")
        return
    
    target_id = command_parts[1].strip()
    
    if target_id.isdigit():
        target_id = int(target_id)
        
        if target_id in blacklist_data["users"]:
            blacklist_data["users"].remove(target_id)
            save_blacklist(blacklist_data)
            await message.reply(f"User {target_id} has been removed from the blacklist.")
        else:
            await message.reply(f"User {target_id} is not in the blacklist.")
    else:
        await message.reply("Invalid user or chat ID. Please provide a valid ID.")

@Client.on_message(filters.command("checkblacklist") & filters.private)
async def check_blacklist(client: Client, message):
    """Check if a user is blacklisted."""
    user_id = message.from_user.id

    if user_id in blacklist_data["users"]:
        await message.reply(f"User {user_id} is blacklisted.")
    else:
        await message.reply(f"User {user_id} is not blacklisted.")

@Client.on_message(filters.command("checkchatblacklist") & filters.group)
async def check_chat_blacklist(client: Client, message):
    """Check if a chat is blacklisted."""
    chat_id = message.chat.id

    if chat_id in blacklist_data["chats"]:
        await message.reply(f"This chat is blacklisted.")
    else:
        await message.reply(f"This chat is not blacklisted.")

@Client.on_message(filters.command("blacklistchat") & filters.private)
async def blacklist_chat(client: Client, message):
    """Blacklist a chat."""
    if message.from_user.id != 123456789:  # Check for authorized users (e.g., admin)
        await message.reply("You are not authorized to use this command.")
        return
    
    # Extract chat ID
    command_parts = message.text.split(" ", 1)
    
    if len(command_parts) < 2:
        await message.reply("Please provide a chat ID to blacklist.")
        return
    
    chat_id = command_parts[1].strip()
    
    if chat_id.isdigit():
        chat_id = int(chat_id)
        
        if chat_id not in blacklist_data["chats"]:
            blacklist_data["chats"].append(chat_id)
            save_blacklist(blacklist_data)
            await message.reply(f"Chat {chat_id} has been blacklisted.")
        else:
            await message.reply(f"Chat {chat_id} is already blacklisted.")
    else:
        await message.reply("Invalid chat ID. Please provide a valid ID.")

@Client.on_message(filters.command("unblacklistchat") & filters.private)
async def unblacklist_chat(client: Client, message):
    """Unblacklist a chat."""
    if message.from_user.id != 123456789:  # Check for authorized users (e.g., admin)
        await message.reply("You are not authorized to use this command.")
        return
    
    # Extract chat ID
    command_parts = message.text.split(" ", 1)
    
    if len(command_parts) < 2:
        await message.reply("Please provide a chat ID to unblacklist.")
        return
    
    chat_id = command_parts[1].strip()
    
    if chat_id.isdigit():
        chat_id = int(chat_id)
        
        if chat_id in blacklist_data["chats"]:
            blacklist_data["chats"].remove(chat_id)
            save_blacklist(blacklist_data)
            await message.reply(f"Chat {chat_id} has been removed from the blacklist.")
        else:
            await message.reply(f"Chat {chat_id} is not in the blacklist.")
    else:
        await message.reply("Invalid chat ID. Please provide a valid ID.")
        
