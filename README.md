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
   - 1. ##**Windows:**
   - Download FFmpeg from the official site: [FFmpeg Download Page](https://ffmpeg.org/download.html).
   - Extract the ZIP file to a directory (e.g., `C:\ffmpeg`).
   - Add the `bin` folder to your system's PATH:
     1. Open the Start menu, search for "Environment Variables," and open it.
     2. Under "System Variables," select `Path` and click "Edit."
     3. Click "New" and add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
     4. Click "OK" to save changes.

   - 2. ##**Linux:**
   - Install FFmpeg using your package manager:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```

   - 3. ##**MacOS:**
   - Install FFmpeg using Homebrew:
     ```bash
     brew install ffmpeg
     ```

4. **Verify Installation:**
   - Open a terminal or command prompt and type:
     ```bash
     ffmpeg -version
     ```
   - If the version information is displayed, FFmpeg is installed correctly.

---

5. Run the application:
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
