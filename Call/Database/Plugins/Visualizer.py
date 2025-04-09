"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

import asyncio
import sys
from typing import Optional
from time import time

# Visualization function
def visualize_audio(audio_data: str) -> str:
    """Generate a simple ASCII visualization of the audio."""
    bars = "█" * int(audio_data)
    return f"[{bars:<20}]"

async def send_visualizer(chat_id, audio_data: Optional[str] = "10"):
    """Send an ASCII-based visualizer to the voice chat."""
    try:
        while True:
            # Create the visualizer and update the progress
            visualization = visualize_audio(audio_data)
            await chat_id.send_message(visualization)  # Use chat_id to send the visualizer as message
            await asyncio.sleep(1)  # Update every second

    except Exception as e:
        print(f"Error in sending visualizer: {e}")

async def stop_visualizer(chat_id):
    """Stop sending the visualizer."""
    try:
        # Stop the visualizer updates by clearing the output
        await chat_id.send_message("🛑 Stopped visualizer.")
    except Exception as e:
        print(f"Error in stopping visualizer: {e}")


