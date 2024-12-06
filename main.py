from downloader.downloader import download_audio, bulk_download
from downloader.utils import is_valid_url
from downloader.spotify_utils import get_playlist_id

def main():
    print("Welcome to the Music Downloader!")
    print("Options: \n1. Single Download\n2. Bulk Download (Spotify Playlist)")
    while True:
        choice = input("Enter your choice (or type 'exit' to quit): ").strip()
        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        if choice == '1':
            url = input("Enter a YouTube URL: ")
            if is_valid_url(url):
                download_audio(url)
            else:
                print("Invalid URL. Please try again.")
        elif choice == '2':
            playlist_url = input("Enter a Spotify playlist URL: ")
            playlist_id = get_playlist_id(playlist_url) 
            if playlist_id:
                bulk_download(playlist_id)
            else:
                print("Invalid Spotify playlist URL. Please try again.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
