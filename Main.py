import asyncio
from pyrogram import filters
from Call.Player.Calls import bot, call


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot is online!")


bot.run()
call.start()
