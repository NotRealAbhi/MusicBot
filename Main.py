import asyncio
from Call.Player.Calls import bot, call

async def main():
    await bot.start()
    await call.start()
    print("✅ Music Bot and VC Engine started!")

    await idle()  # Keeps the bot running

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
