import asyncio
from Call.Player.Calls import bot, call


@bot.on_message(filters.command("start"))
 async def start(client, message):
     await message.reply("Bot is online!")


async def start_bot():
    try:
        await bot.start()  # Start the bot
        print("✅ Bot started successfully!")
    except Exception as e:
        print(f"⚠️ Error starting the bot: {e}")

    # Running the PyTgCalls bot in a loop
    await call.start()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())


