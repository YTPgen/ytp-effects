import numpy as np
import cv2
import ytp_effects
import random
from moviepy.audio.AudioClip import AudioArrayClip

# from face_feature_recognizer.face_feature_recognizer import FaceFeatureRecognizer
import moviepy.editor as me
from tqdm import tqdm
import random
from ytp_effects.video.scramble import scramble

# class FullFrame(object):
#     def __init__(self, video_frame, audio_frames):
#         self.video_frame = video_frame
#         self.audio_frames = audio_frames


# class CutClip(object):
#     def __init__(self, video_clip: me.VideoFileClip):
#         self.video_fps = video_clip.fps
#         self.audio_fps = video.audio.fps
#         self.frames = self.video_to_frames(video_clip)

#     def video_to_frames(self, video_clip: me.VideoFileClip):
#         audio_frames = video.audio.to_soundarray()
#         frames = []
#         i = 0
#         audio_frames_per_frame = video_clip.audio.fps / video.fps
#         for t, video_frame in tqdm(video.iter_frames(with_times=True)):
#             copy_from = i
#             i = i + audio_frames_per_frame
#             next_frame = FullFrame(video_frame, audio_frames[int(copy_from) : int(i)])
#             frames.append(next_frame)
#         return frames

#     def to_video(self) -> me.VideoFileClip:
#         video_frames = [f.video_frame for f in self.frames]
#         afs = [af.audio_frames for af in self.frames]
#         audio_frames = np.array([item for sublist in afs for item in sublist])
#         video = me.ImageSequenceClip(video_frames, self.video_fps)
#         video.audio = AudioArrayClip(audio_frames, self.audio_fps)
#         return video


# def scramble(
#     cut_clip: CutClip, scramble_frame_length=1, unique_scramble=True
# ) -> CutClip:
#     scrambled_frames = []
#     clip_frames_length = len(cut_clip.frames)
#     while (
#         len(cut_clip.frames) >= scramble_frame_length
#         and len(scrambled_frames) < clip_frames_length
#     ):
#         max_start_index = len(cut_clip.frames) - scramble_frame_length
#         frame_index = 0 if max_start_index == 0 else random.randint(0, max_start_index)
#         for f in cut_clip.frames[frame_index : frame_index + scramble_frame_length]:
#             scrambled_frames.append(f)
#         if unique_scramble:
#             del cut_clip.frames[frame_index : frame_index + scramble_frame_length]
#     if unique_scramble:
#         for f in cut_clip.frames:
#             scrambled_frames.append(f)
#     if len(scrambled_frames) > clip_frames_length:
#         scrambled_frames = scrambled_frames[:clip_frames_length]
#     cut_clip.frames = scrambled_frames
#     return cut_clip


# cap = cv2.VideoCapture("jv-interview.mp4")
video = me.VideoFileClip("fresh_prince.mp4").subclip(20, 45)
# audio = video.audio
# duration = video.duration
# angle = 0
# z = 1.5
# shake = 35

# cut_clip = CutClip(video)
# cut_clip = scramble(cut_clip, 1, False)
# output_video = me.ImageSequenceClip(output_video_frames, video.fps)
# output_video.audio = AudioArrayClip(output_audio_frames, audio.fps)
# output_video = cut_clip.to_video()
# video = scramble(video, 3)

import random

audio = video.audio
audio_frames = audio.to_soundarray()
import math

audio_frames = np.clip(
    np.array([f + math.cos(f[0]) for f in tqdm(audio_frames)]), -0.98, 0.98
)
video.audio = AudioArrayClip(audio_frames, audio.fps)
video.write_videofile("test.mp4")
