
from downloader.downloader import download_audio
from downloader.utils import is_valid_url

def main():
    print("Welcome to the Music Downloader!")
    while True:
        url = input("Enter a YouTube video URL (or type 'exit' to quit): ").strip()
        if url.lower() == 'exit':
            print("Goodbye!")
            break
        if is_valid_url(url):
            download_audio(url)
        else:
            print("Invalid URL. Please try again.")

if __name__ == "__main__":
    main()
