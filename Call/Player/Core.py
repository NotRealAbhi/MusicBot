"""
Telegram @NotRealAbhi
Copyright ©️ 2025
"""

from .Calls import call
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality

# Example audio URL for testing
sample_audio = "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"

current_song = None
current_position = 0

async def stream_audio(chat_id, file_path):
    global current_song, current_position
    try:
        current_song = file_path  # Set the current song
        current_position = 0  # Reset position when a new song starts
        await call.play(
            chat_id,
            MediaStream(
                media_path=file_path,
                audio_parameters=AudioQuality.HIGH,
                video_flags=MediaStream.Flags.IGNORE
            )
        )
        return True, None
    except Exception as e:
        return False, f"Error: <code>{e}</code>"

async def get_now_playing():
    """Returns the current song title and a seek bar"""
    global current_song, current_position
    if not current_song:
        return "No song is playing right now."
    
    # Simple ASCII seek bar (replace with actual time data for accurate progress)
    total_duration = 300  # Example song length in seconds (5 minutes)
    seek_bar = "🔘" * (current_position // 10) + "🟩" * ((total_duration - current_position) // 10)
    song_title = current_song if current_song else "Unknown Song"
    
    # Update the position (simulating it for now)
    current_position += 1
    if current_position > total_duration:
        current_position = 0  # Reset after song ends

    return f"🎶 Now Playing: <code>{song_title}</code>\n{seek_bar}\n⏰ {current_position}/{total_duration} seconds"


async def play_video(chat_id: int, video_url: str = sample_audio, quality: str = "SD_480p"):
    """Play a video stream with audio in VC."""
    try:
        quality_mapping = {
            "uhd_4k": VideoQuality.UHD_4K,
            "qhd_2k": VideoQuality.QHD_2K,
            "fhd_1080p": VideoQuality.FHD_1080p,
            "hd_720p": VideoQuality.HD_720p,
            "sd_480p": VideoQuality.SD_480p,
            "sd_360p": VideoQuality.SD_360p,
        }
        video_quality = quality_mapping.get(quality.lower(), VideoQuality.SD_480p)

        await call.play(
            chat_id,
            MediaStream(
                media_path=video_url,
                audio_parameters=AudioQuality.HIGH,
                video_parameters=video_quality
            )
        )
        return True, "📹 Video started"
    except Exception as e:
        return False, f"❌ Error: <code>{e}</code>"


async def pause(chat_id: int):
    try:
        await call.pause(chat_id)
        return "⏸️ Paused"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"


async def resume(chat_id: int):
    try:
        await call.resume(chat_id)
        return "▶️ Resumed"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"


async def mute(chat_id: int):
    try:
        await call.mute(chat_id)
        return "🔇 Muted"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"


async def unmute(chat_id: int):
    try:
        await call.unmute(chat_id)
        return "🔊 Unmuted"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"


async def change_volume(chat_id: int, volume: int = 100):
    try:
        await call.change_volume(chat_id, volume)
        return f"🔊 Volume set to {volume}%"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"


async def stop(chat_id: int):
    try:
        await call.leave_call(chat_id)
        return "🛑 Stopped and left VC"
    except Exception as e:
        return f"❌ Error: <code>{e}</code>"
      
