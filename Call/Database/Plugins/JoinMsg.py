"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import send_welcome_message  # Assuming we have this method in Core

@Client.on_message(filters.new_chat_members)
async def welcome_new_user(client: Client, message: Message):
    """Sends a custom welcome message when a user joins the voice chat."""
    if message.chat.type != "private":
        new_member = message.new_chat_members[0]
        chat_id = message.chat.id

        # Get the custom join message (can be saved in DB or config)
        join_message = "Welcome to the Voice Chat, {first_name}! 🎧"

        # Send the custom join message
        formatted_message = join_message.format(first_name=new_member.first_name)
        await send_welcome_message(chat_id, formatted_message)
      
