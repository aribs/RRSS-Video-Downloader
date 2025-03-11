# YouTube Video Downloader

A simple Python script to download YouTube videos using `yt-dlp` and `ffmpeg`. This script allows you to download videos in the best available quality by passing the video URL as a command-line argument.

## 📌 Requirements
- Python 3.x
- `yt-dlp` (for downloading YouTube videos)
- `ffmpeg` (for merging video and audio)

## 🚀 Installation

### 1️⃣ Install `yt-dlp`
Run the following command to install `yt-dlp`:
```bash
pip install yt-dlp
```

### 2️⃣ Install `ffmpeg`

#### 🐧 Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install ffmpeg -y
```

#### 🍏 macOS (via Homebrew)
```bash
brew install ffmpeg
```

#### 🖥️ Windows
1. Download `ffmpeg` from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the contents and move the folder to `C:\ffmpeg\`.
3. Add `C:\ffmpeg\bin\` to the **system PATH**:
   - Open *Environment Variables*.
   - Edit the `Path` variable and add `C:\ffmpeg\bin\`.
   - Save and restart your terminal.
4. Verify the installation:
   ```bash
   ffmpeg -version
   ```

## 📝 Usage
Run the script with the YouTube video URL as an argument:
```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

## 🛠 Features
✅ Downloads videos in the highest quality available.  
✅ Saves the video with its original title.  
✅ Automatically merges video and audio (if required).  

## 📜 License
This project is open-source and free to use.

---
🚀 Enjoy downloading your favorite YouTube videos!
