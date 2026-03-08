import yt_dlp

def download_video(url):
    ydl_opts = {
        # 'bestvideo+bestaudio' dilei shobcheye bhalo quality pabe
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        # FFmpeg er location jodi path e na thake, tobe nicher line e path bole deya jay
        'merge_output_format': 'mp4', 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading... ektu somoy lagte pare.")
            ydl.download([url])
        print("\nDownload Complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Video Link: ")
    download_video(link)
