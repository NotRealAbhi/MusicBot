"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from Call.Lang import get_string
from Call.Database.DB import db, USE_JSON
from Call.Config import SUDO_USERS

AVAILABLE_LANGS = {
    "en": "English 🇺🇸",
    "hi": "हिंदी 🇮🇳"
}


def set_user_lang(user_id, lang_code):
    if USE_JSON:
        db["users"][str(user_id)]["lang"] = lang_code
    else:
        db["users"].update_one({"_id": user_id}, {"$set": {"lang": lang_code}}, upsert=True)


def get_user_lang(user_id):
    if USE_JSON:
        return db["users"].get(str(user_id), {}).get("lang", "en")
    else:
        user = db["users"].find_one({"_id": user_id})
        return user["lang"] if user and "lang" in user else "en"


@Client.on_message(filters.command(["setlang", "language"]) & filters.private)
async def set_language(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)

    if len(args) == 1:
        lang_text = "\n".join([f"<b>{code}</b> - {name}" for code, name in AVAILABLE_LANGS.items()])
        return await message.reply(
            f"🌐 <b>Available Languages:</b>\n{lang_text}\n\nUse <code>/setlang en</code> to set your language."
        )

    lang_code = args[1].strip().lower()

    if lang_code not in AVAILABLE_LANGS:
        return await message.reply("❌ Invalid language code. Try again with a valid one.")

    set_user_lang(user_id, lang_code)
    lang_name = AVAILABLE_LANGS[lang_code]
    await message.reply(f"✅ Language set to <b>{lang_name}</b>.")


@Client.on_message(filters.command("mystats"))
async def mystats_handler(client: Client, message: Message):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    welcome = get_string(lang, "start")
    await message.reply(welcome)
  
