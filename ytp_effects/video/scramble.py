
import moviepy.editor as me
import random

from ytp_effects.video.cut_clip import CutClip

def scramble(clip: me.VideoFileClip, scramble_frame_length=1, unique_scramble=True) -> CutClip:
    """Scrambles the order of frames in a clip.

    Args:
        clip (moviepy.editor.VideoFileClip): Clip to scramble.
        scramble_frame_length (int, optional): Length of each scramble sequence. Defaults to 1.
        unique_scramble (bool, optional): If set to True allow to reuse same frames. Defaults to True.

    Returns:
        CutClip: [description]
    """    
    cut_clip = CutClip(clip)
    scrambled_frames = []
    clip_frames_length = len(cut_clip.frames)
    while (
        len(cut_clip.frames) >= scramble_frame_length
        and len(scrambled_frames) < clip_frames_length
    ):
        max_start_index = len(cut_clip.frames) - scramble_frame_length
        frame_index = 0 if max_start_index == 0 else random.randint(0, max_start_index)
        for f in cut_clip.frames[frame_index : frame_index + scramble_frame_length]:
            scrambled_frames.append(f)
        if unique_scramble:
            del cut_clip.frames[frame_index : frame_index + scramble_frame_length]
    if unique_scramble:
        for f in cut_clip.frames:
            scrambled_frames.append(f)
    if len(scrambled_frames) > clip_frames_length:
        scrambled_frames = scrambled_frames[:clip_frames_length]
    cut_clip.frames = scrambled_frames
    return cut_clip.to_video()