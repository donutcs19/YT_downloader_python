import yt_dlp

url = input("Enter Youtube URL : ")
path = input("Enter download folder (e.g. C:\DEV\Videos): ")

ydl_opts = {
    'format': 'bestvideo[height=1080]',
    'outtmpl': rf'{path}\%(title)s.%(ext)s',
    'merge_output_format': 'mp4',   
    # 'outtmpl': r'FULL PART\%(title)s.%(ext)s', 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
