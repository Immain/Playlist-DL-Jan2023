#     ____                  __         ____        __           _____            __
#    / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
#   / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
#  / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  )
# /_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/
#                                                                 /____/
# Written By: Immain
# Date Created: 1/31/2023
# Version: 1.0.0
# Description: Downloads playlists from youtube and saves it as a mp4 file with the thumbnail as a jpg file in the same directory as the script. 

import pafy, re, wget, string, random, os, ffmpeg, pytube

url = "https://www.youtube.com/watch?v=6omHDfHITZ4&list=PLXa7L1ovsDcMwMxwBF4vyh-RLYkFABlb2"

# Get playlist Thumbnails
playlist = pytube.Playlist(url)
for video in playlist.videos:
    exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
    s = re.findall(exp,video.watch_url)[0][-1]
    letters = string.ascii_uppercase + string.digits
    thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
    file = f"{s}-{( ''.join(random.choice(letters) for i in range(10)) )}.jpg"
    wget.download(thumbnail)
    os.rename("maxresdefault.jpg", file)
    print(thumbnail)

# Get playlist videos
for video in playlist.videos:
    result = pafy.new(video.watch_url)
    streams = result.streams
    for stream in streams:
        print(stream)
    best_quality_video = result.getbestvideo(preftype="mp4")
    bestaudio = result.getbestaudio(preftype="m4a")
    video_stream = ffmpeg.input(best_quality_video.url)
    audio_stream = ffmpeg.input(bestaudio.url)
    ffmpeg.output(video_stream, audio_stream, "output.mp4").run()
    filestream = f"{s}-{( ''.join(random.choice(letters) for i in range(10)) )}-video.mp4"
    os.rename("output.mp4", filestream)




