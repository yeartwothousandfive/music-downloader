import os
from yt_dlp import YoutubeDL
from .config import YDL_OPTIONS

def download_audio(video_url):
    """Download a single song."""
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.download([video_url])
        print(f"Download completed for: {video_url}")
    except Exception as e:
        print(f"An error occurred while downloading: {e}")
