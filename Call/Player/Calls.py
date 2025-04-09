"""
Telegram @NotRealAbhi
Copyright ©️ 2025
"""

from pytgcalls import PyTgCalls, filters
from pytgcalls.types.stream import StreamEnded
from pytgcalls.types import Update
from pyrogram import Client
from Call.Config import API_ID, API_HASH, BOT_TOKEN

# ✅ Initialize bot client
bot = Client(
    name="MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,  # Optional: auto-load Plugins/
)

# ✅ Initialize PyTgCalls for bot
call = PyTgCalls(bot)

# ✅ Handling stream end event
@call.on_update(filters.stream_end())
async def on_stream_end_handler(client: PyTgCalls, update: Update):
    chat_id = update.chat_id
    try:
        # Attempting to leave the call after stream ends
        await call.leave_call(chat_id)
        print(f"❌ Stream ended, left VC in {chat_id}")
    except Exception as e:
        # Catching any errors while trying to leave the call
        print(f"⚠️ Error leaving VC after stream end in {chat_id}: {e}")
