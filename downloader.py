import yt_dlp
import sys

def download_youtube(url):
    try:
        options = {
            'outtmpl': "%(title)s.%(ext)s",  # Save in the current folder with the original title
            'format': 'bestvideo+bestaudio/best',  # Best available quality
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("Download completed successfully.")
    except Exception as e:
        print(f"Error downloading the video: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <VIDEO_URL>")
        sys.exit(1)

    url = sys.argv[1]
    download_youtube(url)
