from pytube import YouTube
from sys import argv

if len(argv) < 2:
    print("Usage: python ytDownload.py <YouTube URL>")
    exit(1)

link = argv[1]

try:
    yt = YouTube(link)
    print("Title:", yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download('/Users/udaykiran/Downloads/yt')
    print("Download completed!")
except Exception as e:
    print("An error occurred:", e)
