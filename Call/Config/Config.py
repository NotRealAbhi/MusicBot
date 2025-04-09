import os

# Bot Configuration
API_ID = int(os.getenv("API_ID", 25024171))  # Your API ID from Telegram
API_HASH = os.getenv("API_HASH", "7e709c0f5a2b8ed7d5f90a48219cffd3")  # Your API Hash from Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "7513601323:AAHe3cZhJDwVXW_1w_DYQR7-hCfeSilQ6Ic")  # Your Bot Token from @BotFather

# Bot Owner and Sudo Users
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  # Your Telegram ID as the bot owner
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "123456789,987654321").split(',')))  # List of IDs for Sudo Users (comma-separated)

# MongoDB Configuration (if used)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/music_bot_db")  # MongoDB URI for database
MONGO_DB = os.getenv("MONGO_DB", "music_bot_db")  # MongoDB database name

# Music Player Configuration
DEFAULT_VOLUME = int(os.getenv("DEFAULT_VOLUME", "70"))  # Default volume level
MAX_QUEUE_SIZE = int(os.getenv("MAX_QUEUE_SIZE", "100"))  # Maximum number of songs in the queue

# Voice Chat Settings
MAX_PLAYLIST_LENGTH = int(os.getenv("MAX_PLAYLIST_LENGTH", "50"))  # Max number of songs to play from a playlist

# Language Configuration
DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")  # Default language for bot messages
LANGUAGE_FILE = os.getenv("LANGUAGE_FILE", "Lang/en.json")  # Path to language file

# Logging and Debugging
DEBUG = bool(os.getenv("DEBUG", True))  # Enable or disable debugging mode

# Misc Settings
ANTI_SPAM = bool(os.getenv("ANTI_SPAM", True))  # Enable or disable anti-spam protection

