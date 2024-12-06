import os

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(DOWNLOADS_FOLDER, '%(title)s.%(ext)s'),  # Saves file with video title as filename
    'quiet': False,                  # Set to True to suppress logs
}
