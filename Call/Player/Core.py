"""
Telegram @NotRealAbhi
Copyright ©️ 2025
"""

from Player.Calls import call
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality

# Example audio URL for testing
sample_audio = "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"


async def play_audio(chat_id: int, audio_url: str = sample_audio):
    """Play an audio stream in VC."""
    try:
        await call.play(
            chat_id,
            MediaStream(
                media_path=audio_url,
                audio_parameters=AudioQuality.STUDIO,
                video_flags=MediaStream.Flags.IGNORE
            )
        )
        return True, "🎶 Audio started"
    except Exception as e:
        return False, f"❌ Error: <code>{e}</code>"


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
      
