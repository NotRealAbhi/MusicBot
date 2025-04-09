"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Queue import get_queue
from Call.Player.Core import stream_audio, stop
from Call.Database.DB import db, USE_JSON
from Call.Lang import get_string
from Call.Player.Core import skip_song


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("skip") & filters.group)
async def skip(client: Client, message: Message):
    """Skips the currently playing song."""
    chat_id = message.chat.id
    result = await skip_song(chat_id)
    await message.reply(result)

      
