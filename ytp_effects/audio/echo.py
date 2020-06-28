import numpy as np

from moviepy.editor import VideoClip

import ytp_effects.audio.utils as utils


def echo(video: VideoClip, delay: float, strength: float = 0.7) -> VideoClip:
    """Puts an echo in the audio track with given delay and strength.

    Args:
        video (VideoClip): Video to transform audio for
        delay (float): Delay of echo in seconds
        strength (float): Strength of echo relative to original sound

    Returns:
        VideoClip: Video with echoed sound
    """
    audio_frames = utils.audio_to_frames(video.audio)
    d = int(audio.fps * delay)
    for i in range(len(audio_frames) - d):
        audio_frames[i] += audio_frames[i - d] * strength
    video.audio = utils.frames_to_audio(audio_frames, video.audio.fps)
    return video
