"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Player.Core import stream_audio  # Import stream_audio function
from Call.Lang import get_string


@Client.on_message(filters.command("live") & filters.group)
async def play_radio(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("📻 Usage:\n<code>/radio [stream-url]</code>")

    radio_url = message.command[1]
    chat_id = message.chat.id
    msg = await message.reply("🔄 Connecting to voice chat...")

    success, error = await stream_audio(chat_id, radio_url)
    if success:
        await msg.edit(f"✅ Streaming started!\n📻 <code>{radio_url}</code>")
    else:
        await msg.edit(f"❌ Failed to stream:\n{error}")
      
