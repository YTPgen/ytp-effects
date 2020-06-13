import numpy as np


def echo(audio_frames: np.ndarray, fps: int, delay: int, strength : float = 1.0):
    """Puts an echo in the audio track with given delay and strength.

    Args:
        audio_frames (np.ndarray): [description]
        fps (int): [description]
        delay (int): [description]
        strength (float): [description]

    Returns:
        [type]: [description]
    """    
    d = int(fps * delay)
    for i in range(len(audio_frames) - d):
        audio_frames[i] += audio_frames[i - d] * strength
    return audio_frames
