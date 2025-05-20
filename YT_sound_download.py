import yt_dlp

url = input("Enter Youtube URL : ")

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'merge_output_format': 'mp3',   
    # 'outtmpl': r'FULL PART\%(title)s.%(ext)s', 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
