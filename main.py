from downloader.downloader import download_audio, bulk_download
from downloader.utils import is_valid_url
from downloader.welcome import colorful_welcome

def main():
    colorful_welcome()
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
            bulk_download(playlist_url)
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
