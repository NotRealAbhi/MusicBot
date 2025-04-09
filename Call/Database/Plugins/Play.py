"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL
from Call.Config import SUDO_USERS
from Call.Player.Core import stream_audio
from Call.Lang import get_string
from Call.Database.DB import db, USE_JSON


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


YDL_OPTS = {
    "format": "bestaudio[ext=m4a]/bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": True,
    "no_warnings": True,
    "noplaylist": True,
    "geo_bypass": True,
}


def download_audio(query):
    with YoutubeDL(YDL_OPTS) as ydl:
        info = ydl.extract_info(query, download=True)
        return {
            "title": info.get("title"),
            "url": info.get("webpage_url"),
            "path": ydl.prepare_filename(info)
        }


@Client.on_message(filters.command("play") & filters.group)
async def play_song(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    lang = get_user_lang(user_id)

    if len(message.command) < 2:
        return await message.reply(get_string(lang, "no_results"))

    query = " ".join(message.command[1:])
    msg = await message.reply("🔎 Searching & downloading...")

    try:
        info = await asyncio.to_thread(download_audio, query)
    except Exception as e:
        return await msg.edit(f"❌ Error:\n<code>{e}</code>")

    success, error = await stream_audio(chat_id, info["path"])

    if not success:
        return await msg.edit(error)

    await msg.edit(
        get_string(lang, "play_success").format(title=info["title"])
    )
  
