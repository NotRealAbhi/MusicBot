"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import get_now_playing


@Client.on_message(filters.command("now") & filters.group)
async def nowplaying(client: Client, message: Message):
    """Displays the current song and seek bar."""
    response = await get_now_playing()
    await message.reply(response)
  
