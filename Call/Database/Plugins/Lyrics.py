"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Lang import get_string
import aiohttp


@Client.on_message(filters.command("lyrics") & filters.group)
async def fetch_lyrics(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("🎶 Usage:\n<code>/lyrics Artist - Title</code>\nExample:\n<code>/lyrics Imagine Dragons - Believer</code>")

    query = " ".join(message.command[1:])

    if " - " not in query:
        return await message.reply("❌ Please format like: <code>Artist - Title</code>")

    artist, title = query.split(" - ", 1)
    msg = await message.reply("🔍 Fetching lyrics...")

    try:
        url = f"https://api.lyrics.ovh/v1/{artist.strip()}/{title.strip()}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    lyrics = data.get("lyrics")

                    if not lyrics:
                        return await msg.edit("❌ No lyrics found.")

                    if len(lyrics) > 4000:
                        lyrics = lyrics[:4000] + "\n...\n\n(Lyrics truncated)"

                    await msg.edit(
                        f"🎤 <b>{artist.strip()} - {title.strip()}</b>\n\n<code>{lyrics}</code>"
                    )
                else:
                    await msg.edit("❌ Could not find lyrics for that song.")
    except Exception as e:
        await msg.edit(f"❌ Error:\n<code>{e}</code>")
      
