from pytube import YouTube
import os

#yt = YouTube(str(input("Enter the URL of the video you want to download: #\n>>")))

yt = YouTube(https://www.youtube.com/watch?v=RA4PqRDU4Hk)


#audio = yt.streams.filter(only_audio = True).first()

#yt.streams.filter(only_audio=True)

yt.streams.first().download()


# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'

# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
# os.rename(out_file, new_file)

# print(yt.title + " has been successfully downloaded in .mp3 format.")



