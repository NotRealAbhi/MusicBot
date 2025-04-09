"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Database.DB import db, USE_JSON
from Call.Lang import get_string

from Call.Player.Queue import get_queue


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("queue") & filters.group)
async def show_queue(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    queue = get_queue(chat_id)
    if not queue:
        return await message.reply(get_string(lang, "no_queue"))

    text = f"🎶 <b>Current Queue:</b>\n"
    for idx, track in enumerate(queue, start=1):
        text += f"<b>{idx}.</b> {track['title']}\n"

    await message.reply(text)
  
