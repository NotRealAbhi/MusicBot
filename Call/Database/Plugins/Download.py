"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pyrogram.errors import PeerIdInvalid
from Call.Player.Core import download_media

@Client.on_message(filters.command("download") & filters.group)
async def download_audio(client: Client, message: Message):
    """Downloads the currently playing song/audio."""
    chat_id = message.chat.id

    try:
        # Check if there is a media stream currently playing
        if not download_media.get(chat_id):
            await message.reply("❌ No media is currently playing.")
            return

        # Get the media file
        media_file = download_media.get(chat_id)

        # Provide the file download link or file
        await client.send_document(
            chat_id,
            media_file,
            caption="Here is your requested audio file. 🎶",
        )

        await message.reply("⏳ Downloading your audio... Please wait.")
    except PeerIdInvalid:
        await message.reply("❌ Invalid chat. Ensure the bot is in the correct chat.")
    except Exception as e:
        await message.reply(f"Error: <code>{e}</code>")

async def download_media(chat_id, file_path):
    """Handles the download of the media file."""
    try:
        # Assume the media is downloaded and stored locally
        file_name = os.path.basename(file_path)
        
        # Download the file (this is just a placeholder, implement according to your needs)
        # Actual download process should be done here.
        
        # Returning the file name for demonstration purposes.
        return file_path
    except Exception as e:
        print(f"Error downloading media: {e}")
        return None
      
