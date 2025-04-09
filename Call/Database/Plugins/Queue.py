"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import show_queue


@Client.on_message(filters.command("queue") & filters.group)
async def queue(client: Client, message: Message):
    """Displays the current song queue."""
    result = await show_queue()
    await message.reply(result)
    
