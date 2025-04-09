"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters

# Sample data for top 10 songs
top_songs = [
    {"rank": 1, "title": "Song 1", "artist": "Artist 1"},
    {"rank": 2, "title": "Song 2", "artist": "Artist 2"},
    {"rank": 3, "title": "Song 3", "artist": "Artist 3"},
    {"rank": 4, "title": "Song 4", "artist": "Artist 4"},
    {"rank": 5, "title": "Song 5", "artist": "Artist 5"},
    {"rank": 6, "title": "Song 6", "artist": "Artist 6"},
    {"rank": 7, "title": "Song 7", "artist": "Artist 7"},
    {"rank": 8, "title": "Song 8", "artist": "Artist 8"},
    {"rank": 9, "title": "Song 9", "artist": "Artist 9"},
    {"rank": 10, "title": "Song 10", "artist": "Artist 10"},
]

@Client.on_message(filters.command("top10"))
async def top_10(client: Client, message):
    """Display the top 10 songs."""
    response = "Top 10 Songs:\n"
    for song in top_songs:
        response += f"{song['rank']}. {song['title']} by {song['artist']}\n"

    await message.reply(response)

@Client.on_message(filters.command("mytop"))
async def my_top(client: Client, message):
    """Display user's top songs (using an example list)."""
    user_id = message.from_user.id
    # You can customize this with actual user data
    user_songs = top_songs[:5]  # For example, top 5 songs for the user

    response = f"Your Top Songs:\n"
    for song in user_songs:
        response += f"{song['rank']}. {song['title']} by {song['artist']}\n"

    await message.reply(response)
  
