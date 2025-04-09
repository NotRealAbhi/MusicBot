"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import unmute
from Call.Lang import get_string
from Call.Database.DB import db, USE_JSON


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("unmute") & filters.group)
async def unmute_command(client: Client, message: Message):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    response = await unmute(message.chat.id)
    await message.reply(response)
  
