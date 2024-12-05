
# Music Downloader

A simple music downloader using Python and `yt-dlp`.

## Features
- Download audio from YouTube videos as MP3.
- Automatically extracts and converts audio using FFmpeg.

## Requirements
- Python 3.6+
- FFmpeg installed on your system ([download here](https://ffmpeg.org/)).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yeartwothousandfive/music-downloader.git
   cd music-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg (if not already installed):
   - **Windows**: Download from [FFmpeg Official Site](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your PATH.
   - **Linux**: Install with:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **MacOS**: Install with:
     ```bash
     brew install ffmpeg
     ```

   Verify installation with:
   ```bash
   ffmpeg -version
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Troubleshooting
- **Error**: `Postprocessing: ffprobe and ffmpeg not found.`
  - Ensure FFmpeg is installed and added to your system's PATH.
  - Alternatively, specify the FFmpeg location when running the script:
    ```bash
    yt-dlp --ffmpeg-location /path/to/ffmpeg
    ```

## Dependencies
- `yt-dlp`: For downloading and extracting audio from YouTube videos.
- `FFmpeg`: For audio conversion.

## License
This project is open-source and licensed under the MIT License.
