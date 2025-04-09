"""
Telegram @NotRealAbhi
Copyright ©️ 2025
"""

from pytgcalls.types import MediaStream, AudioQuality
from .Calls import call

# Predefined FFmpeg filter parameters
FILTERS = {
    "bass": "bass=g=10,dynaudnorm=f=150",
    "nightcore": "asetrate=44100*1.25,aresample=44100,atempo=1.1",
    "vaporwave": "asetrate=44100*0.8,aresample=44100,atempo=1.1",
    "echo": "aecho=0.8:0.9:1000:0.3",
    "surround": "surround",
    "reverse": "areverse",
}


async def apply_filter(chat_id: int, file_path: str, filter_name: str):
    """
    Apply an audio filter and play.
    :param chat_id: VC chat ID
    :param file_path: Original audio path or URL
    :param filter_name: One of bass, nightcore, etc.
    """
    try:
        filter_cmd = FILTERS.get(filter_name)
        if not filter_cmd:
            return False, "❌ Invalid filter name."

        ffmpeg_path = f"audio-filter:{file_path}|af={filter_cmd}"
        await call.play(
            chat_id,
            MediaStream(
                media_path=ffmpeg_path,
                audio_parameters=AudioQuality.HIGH,
                video_flags=MediaStream.Flags.IGNORE,
            ),
        )
        return True, f"✅ Applied filter: {filter_name.capitalize()}"
    except Exception as e:
        return False, f"❌ Error: <code>{e}</code>"


async def remove_filter(chat_id: int, file_path: str):
    """
    Play original audio without filters.
    """
    try:
        await call.play(
            chat_id,
            MediaStream(
                media_path=file_path,
                audio_parameters=AudioQuality.HIGH,
                video_flags=MediaStream.Flags.IGNORE,
            ),
        )
        return True, "✅ Removed all filters"
    except Exception as e:
        return False, f"❌ Error: <code>{e}</code>"
      
