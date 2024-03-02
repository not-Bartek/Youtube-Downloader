from pytube import YouTube
from sys import argv

link = argv[1]
path = "/Users/Bartek/Downloads"
yt = YouTube(https://www.youtube.com/shorts/vfvLtTzRXuk)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(path)