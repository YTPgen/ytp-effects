import os
import tempfile

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioArrayClip, AudioClip
import librosa


def pitch_shift(audio: AudioClip, steps: int) -> AudioClip:
    """Shifts an audio clip by a given amount of tone steps.

    Args:
        audio (AudioClip): Input audio
        steps (int): Amount of steps to shift

    Returns:
        AudioClip: Pitch shifted audio
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_file = os.path.join(tmpdir, "tmp.wav")
        pitched_file = os.path.join(tmpdir, "pitched.wav")
        audio.write_audiofile(tmp_file)
        y, sr = librosa.core.load(tmp_file, audio.fps)
        y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=steps)
        librosa.output.write_wav(pitched_file, y_shifted, sr)
        return AudioFileClip(pitched_file)
