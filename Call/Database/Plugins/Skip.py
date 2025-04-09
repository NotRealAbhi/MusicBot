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


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("skip") & filters.group)
async def skip_song(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    queue = get_queue(chat_id)
    if not queue:
        return await message.reply(get_string(lang, "no_queue"))

    queue.pop(0)

    if queue:
        next_song = queue[0]
        success, error = await stream_audio(chat_id, next_song["path"])
        if not success:
            return await message.reply(error)
        await message.reply(get_string(lang, "play_success").format(title=next_song["title"]))
    else:
        await stop(chat_id)
        await message.reply("🛑 Queue ended.")
      
