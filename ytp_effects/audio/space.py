import numpy as np

def robotify(audio_frames: np.ndarray, frequency=3)
for t in range(len(audio_frames)):
    audio_frames[t] *= math.sin(t / frequency)