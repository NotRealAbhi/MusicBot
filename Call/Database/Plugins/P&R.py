"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import pause, resume


@Client.on_message(filters.command("pause") & filters.group)
async def pause_command(client: Client, message: Message):
    """Pauses the current song."""
    chat_id = message.chat.id
    result = await pause(chat_id)
    await message.reply(result)



@Client.on_message(filters.command("resume") & filters.group)
async def resume_command(client: Client, message: Message):
    """Resumes the paused song."""
    chat_id = message.chat.id
    result = await resume(chat_id)
    await message.reply(result)
