from Components.YoutubeDownloader import download_youtube_video
<<<<<<< HEAD
from Components.Edit import extractAudio, crop_videos
=======
from Components.Edit import extractAudio, crop_videos, find_good_intervals
>>>>>>> 81c4e01 (second commit)
from Components.Transcription import transcribeAudio
from Components.LanguageTasks import GetHighlight
import random

url = input("Enter YouTube video URL: ")
Vid = download_youtube_video(url)
if Vid:
    Vid = Vid.replace(".webm", ".mp4")
    print(f"Downloaded video and audio files successfully! at {Vid}")

    Audio = extractAudio(Vid)
    if Audio:

        transcriptions = transcribeAudio(Audio)
        if len(transcriptions) > 0:
            TransText = ""
            print(f"Transcriptions found: {transcriptions}")
<<<<<<< HEAD
            intervals = []
            duration = random.randint(30, 55)
            for text, start, end in transcriptions:
                if end - start < duration:
                    end = start + duration
                intervals.append((start, end))
=======
            intervals = find_good_intervals(transcriptions, max_duration=60)
>>>>>>> 81c4e01 (second commit)

            # start, stop = GetHighlight(TransText)
            # print(f"Start: {start} , End: {stop}")

            crop_videos(Vid, intervals)

        else:
            print("No transcriptions found")
    else:
        print("No audio file found")
else:
    print("Unable to Download the video")
