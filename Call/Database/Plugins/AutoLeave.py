"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pytgcalls import PyTgCalls
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Initialize PyTgCalls
call = PyTgCalls(Client("music_bot"))

# This function will automatically leave a VC when no one is left in it
async def check_empty_vc():
    """Checks if the voice chat is empty, and leaves if true."""
    while True:
        await asyncio.sleep(10)  # Check every 10 seconds
        for chat_id in call.active_calls:
            # Check if there are no participants in the voice chat
            participants = await call.get_participants(chat_id)
            if len(participants) == 0:
                await call.leave_call(chat_id)
                print(f"Bot left the voice chat {chat_id} as it was empty.")

# Start the background task to check for empty voice chats
async def start_auto_leave():
    """Starts the auto-leave background task."""
    await check_empty_vc()

@Client.on_message(filters.command("joinvc") & filters.group)
async def join_vc(client: Client, message: Message):
    """Joins a voice chat."""
    chat_id = message.chat.id
    # Here, you can add your VC joining logic
    await call.join_call(chat_id)
    await message.reply("🎧 Joined the voice chat!")

@Client.on_message(filters.command("leavevc") & filters.group)
async def leave_vc(client: Client, message: Message):
    """Leaves a voice chat."""
    chat_id = message.chat.id
    await call.leave_call(chat_id)
    await message.reply("👋 Left the voice chat!")

# Start the background task when the bot is initialized
@Client.on_ready
async def on_ready(client: Client):
    """Starts the auto leave check when the bot is ready."""
    await start_auto_leave()


