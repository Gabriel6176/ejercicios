from pytube import YouTube
import os

APP_PATH = os.getcwd()


# Ask user for the YouTube video URL
#url = input("Enter the YouTube video URL: ")

# Create a YouTube object from the URL
#yt = YouTube(url)
yt = YouTube("https://www.youtube.com/watch?v=HTAyAwtTDn0")

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
output_path = APP_PATH + "\\"

filename = "audio.mp3"

audio_stream.download(output_path=output_path, filename=filename)

#                 audio_stream.download(filename=filename)

#                  print(f"Audio downloaded to {output_path}/{filename}")


