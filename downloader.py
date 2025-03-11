import yt_dlp
import sys

def download_youtube(url):
    """Download YouTube video in the best available quality."""
    try:
        options = {
            'outtmpl': "%(title)s.%(ext)s",  # Save in the current folder with the original title
            'format': 'bestvideo+bestaudio/best',  # Best available quality
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("YouTube video downloaded successfully.")
    except Exception as e:
        print(f"Error downloading YouTube video: {e}")

def download_tiktok(url):
    """Download TikTok video without watermark."""
    try:
        options = {
            'outtmpl': "%(title)s.%(ext)s",  # Save in the current folder with the original title
            'format': 'best',  # Best available quality
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("TikTok video downloaded successfully.")
    except Exception as e:
        print(f"Error downloading TikTok video: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <VIDEO_URL>")
        sys.exit(1)

    url = sys.argv[1]

    if "youtube.com" in url or "youtu.be" in url:
        download_youtube(url)
    elif "tiktok.com" in url:
        download_tiktok(url)
    else:
        print("Unsupported URL. Only YouTube and TikTok links are supported.")
