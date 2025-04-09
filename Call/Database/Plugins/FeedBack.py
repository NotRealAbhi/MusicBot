"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

from pyrogram import Client, filters
from pyrogram.types import Message

# Define the admin/owner ID for feedback collection
OWNER_ID = ""

@Client.on_message(filters.command("feedback") & filters.private)
async def feedback(client: Client, message: Message):
    """Collect user feedback and send it to the bot owner/admin."""
    try:
        # Asking the user for feedback
        await message.reply("💬 Please provide your feedback or issue:")
        
        # Wait for user response
        response = await client.listen(message.chat.id, timeout=60)  # Wait for 60 seconds
        
        # Get the feedback message from the user
        feedback_message = response.text
        
        # Send the feedback to the owner/admin
        await client.send_message(
            OWNER_ID,
            f"💬 **User Feedback**\n"
            f"**From:** {message.from_user.first_name} ({message.from_user.id})\n"
            f"**Feedback:**\n{feedback_message}"
        )
        
        # Let the user know their feedback was submitted
        await message.reply("Thank you for your feedback! It has been sent to the admin.")
    
    except Exception as e:
        await message.reply(f"Sorry, an error occurred: {e}")
      
