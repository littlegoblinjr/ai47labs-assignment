from moviepy import *
from moviepy.video.fx.Resize import Resize
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut

def stitch_video():

    scene_clips = []

    TOTAL_SCENES = 10

    for i in range(1, TOTAL_SCENES + 1):
        image_clip = ImageClip(f"scene_images/scene_{i}.jpg")
        audio_clip = AudioFileClip(f"scene_audios/scene_{i}.wav")
        duration = max(audio_clip.duration, 10)

        clip = (
            image_clip
            .with_duration(duration)
            .with_position("center")
            .with_audio(audio_clip)
            .with_effects([
                Resize(lambda t: 1 + 0.02 * t),
                FadeIn(1),
                FadeOut(1)
            ])
        )

        scene_clips.append(clip)

    final_video = concatenate_videoclips(scene_clips, method="compose")

    final_video.write_videofile(
        "movie_recap.mp4",
        fps=24,

    )


    