from mutagen.easyid3 import EasyID3
from yt_dlp import YoutubeDL
from .config import YDL_OPTIONS

import os

def add_metadata(file_path, title, artist, album):
    """Add metadata to the MP3 file."""
    try:
        audio = EasyID3(file_path)
    except Exception:
        audio = EasyID3()
    audio['title'] = title
    audio['artist'] = artist
    audio['album'] = album
    audio.save()

def download_audio(video_url, metadata):
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.download([video_url])
        
        filename = metadata['title'] + ".mp3"  
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        add_metadata(file_path, metadata['title'], metadata['artist'], metadata['album'])
        print(f"Download and metadata addition completed: {file_path}")
    except Exception as e:
        print(f"An error occurred while downloading: {e}")
