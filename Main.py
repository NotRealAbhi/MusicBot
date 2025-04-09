import asyncio
from pyrogram.errors import BadMsgNotification
from Call.Player.Calls import bot, call

async def start_bot():
    try:
        print("Bot is starting...")
        await bot.start()
        print("Bot started successfully.")
        await call.start()
        print("PyTgCalls initialized.")
    except BadMsgNotification as e:
        print(f"Error: {e}")
        print("Bad message notification, likely due to a time sync issue. Please sync the bot time.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Exiting...")
        await bot.stop()

async def on_shutdown():
    print("Bot is shutting down...")
    await call.stop()
    await bot.stop()
    print("Bot stopped.")

async def main():
    try:
        await start_bot()
        await bot.idle()  # Keeps the bot running until manually stopped
    except KeyboardInterrupt:
        await on_shutdown()

if __name__ == "__main__":
    asyncio.run(main())
