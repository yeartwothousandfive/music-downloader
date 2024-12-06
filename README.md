# Music Downloader

This project allows you to download music from YouTube and Spotify. You can either download individual tracks from YouTube or bulk download a playlist from Spotify, using YouTube as the source.

### Features:
- **Download Single Track**: Input a YouTube URL to download a single track.
- **Bulk Download from Spotify**: Input a Spotify playlist URL to download all tracks in the playlist.
- **Add Metadata**: The downloaded MP3 files are tagged with song metadata (title, artist, album).

### Requirements:
Make sure to install the dependencies:

```bash
pip install -r requirements.txt
```

### Libraries Used:
- `yt-dlp` - For downloading videos from YouTube.
- `mutagen` - For adding metadata to MP3 files.
- `spotipy` - For accessing Spotify data.

## License
This project is open-source and licensed under the MIT License.
