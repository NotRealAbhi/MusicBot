"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio

# Automatically leave empty voice chats
VOICE_CHAT_TIMEOUT = 60  # Time to wait before leaving the empty voice chat (in seconds)

@Client.on_message(filters.voice_chat_started)
async def on_voice_chat_started(client: Client, message):
    """Join a voice chat when it starts."""
    try:
        await client.join_voice_chat(message.chat.id)
    except UserAlreadyParticipant:
        pass  # If already in the voice chat, do nothing


@Client.on_message(filters.voice_chat_ended)
async def on_voice_chat_ended(client: Client, message):
    """Leave the voice chat when it ends."""
    await client.leave_voice_chat(message.chat.id)


@Client.on_message(filters.voice_chat_participant_left)
async def on_participant_left(client: Client, message):
    """Check if the VC is empty and leave after a timeout."""
    chat_id = message.chat.id
    
    # Check the number of participants in the voice chat
    members = await client.get_chat_members(chat_id, filter="administrators")
    
    if len(members) == 1:  # Only admin is left
        await asyncio.sleep(VOICE_CHAT_TIMEOUT)  # Wait for a while before checking again
        updated_members = await client.get_chat_members(chat_id, filter="administrators")
        
        if len(updated_members) == 1:  # Still only admin
            await client.leave_voice_chat(chat_id)
            print(f"Left the voice chat in {chat_id} due to inactivity.")


@Client.on_message(filters.voice_chat_participant_joined)
async def on_participant_joined(client: Client, message):
    """Keep track of participants joining and reset the timer if necessary."""
    chat_id = message.chat.id
    
    # Reset timeout if the participant count goes above 1
    members = await client.get_chat_members(chat_id, filter="administrators")
    
    if len(members) > 1:  # There are more than 1 participant
        print(f"Bot will stay in the voice chat {chat_id} because there are {len(members)} participants.")
