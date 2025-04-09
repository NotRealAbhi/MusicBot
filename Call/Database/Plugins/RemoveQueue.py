"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Queue import get_queue, remove_from_queue
from Call.Database.DB import db, USE_JSON
from Call.Lang import get_string


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command("remove") & filters.group)
async def remove_song(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    queue = get_queue(chat_id)
    if not queue:
        return await message.reply(get_string(lang, "no_queue"))

    args = message.command
    if len(args) < 2 or not args[1].isdigit():
        return await message.reply("❌ Please specify a position to remove: <code>/remove 2</code>")

    pos = int(args[1]) - 1
    if pos < 1 or pos >= len(queue):
        return await message.reply("❌ Invalid position. Cannot remove current playing or out of range.")

    removed = remove_from_queue(chat_id, pos)
    if removed:
        await message.reply(f"✅ Removed <b>{removed['title']}</b> from queue.")
    else:
        await message.reply("❌ Failed to remove from queue.")
