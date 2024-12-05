
from yt_dlp import YoutubeDL
from .config import YDL_OPTIONS

def download_audio(video_url):
    """Download audio from the given YouTube URL."""
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred while downloading: {e}")
