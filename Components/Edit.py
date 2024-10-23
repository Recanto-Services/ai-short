from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip
import subprocess
from Components.FaceCrop import convert_to_vertical, combine_videos


def extractAudio(video_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_path = "audio.wav"
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        print(f"Extracted audio to: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"An error occurred while extracting audio: {e}")
        return None


<<<<<<< HEAD
=======
def find_good_intervals(transcriptions, max_duration=60):
    intervals = []
    for text, start, end in transcriptions:
        # Se o intervalo for maior que a duração máxima, cortamos
        if end - start > max_duration:
            end = start + max_duration
        intervals.append((start, end))
    return intervals


>>>>>>> 81c4e01 (second commit)
def crop_videos(input_file, intervals):
    with VideoFileClip(input_file) as video:
        for i, (start_time, end_time) in enumerate(intervals):
            croped = f"croped{i+1}.mp4"
            output_file = f"output_{i+1}.mp4"
            cropped_video = video.subclip(start_time, end_time)

            # combine_videos(output_file, croped, "Final.mp4")
            cropped_video.write_videofile(output_file, codec='libx264')
            convert_to_vertical(output_file, croped)
            print(f"Generated {output_file} from {start_time} to {end_time}")


# Example usage:
if __name__ == "__main__":
    input_file = r"Example.mp4"  # Test
    print(input_file)
    output_file = "Short.mp4"
    start_time = 31.92
    end_time = 49.2

    crop_video(input_file, output_file, start_time, end_time)
