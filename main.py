from downloader.downloader import download_audio
from downloader.utils import is_valid_url

def main():
    print("Welcome to the Music Downloader!")
    print("Options: \n1. Single Download")
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
        else:
            print("Invalid choice. Please enter 1.")

if __name__ == "__main__":
    main()
