from downloader.downloader import download_audio
from downloader.utils import is_valid_url


def handle_download(url: str):
    try:
        if is_valid_url(url):
            download_audio(url)
            print("Download successful!")
        else:
            print("Invalid URL. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_menu():
    print("Welcome to the Music Downloader!")
    print("Options:")
    print("1. Single Download")
    print("Type 'exit' to quit.")


def main():
    display_menu()
    
    while True:
        choice = input("Enter your choice: ").strip()
        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        elif choice == '1':
            url = input("Enter a YouTube URL: ").strip()
            handle_download(url)
        else:
            print("Invalid choice. Please enter 1.")


if __name__ == "__main__":
    main()
