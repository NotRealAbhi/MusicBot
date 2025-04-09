"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import change_volume, mute, unmute
from Call.Lang import get_string
from Call.Database.DB import db, USE_JSON


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("volume") & filters.group)
async def set_volume(client: Client, message: Message):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    if len(message.command) < 2 or not message.command[1].isdigit():
        return await message.reply("🔊 Usage:\n<code>/volume 100</code> (0-200)")

    volume = int(message.command[1])
    if volume < 0 or volume > 200:
        return await message.reply("⚠️ Volume must be between 0 and 200")

    response = await change_volume(message.chat.id, volume)
    await message.reply(response)
