import numpy as np
import cv2
import ytp_effects
import random
from moviepy.audio.AudioClip import AudioArrayClip
from face_feature_recognizer.face_feature_recognizer import FaceFeatureRecognizer
import moviepy.editor as me
from tqdm import tqdm


# cap = cv2.VideoCapture("jv-interview.mp4")
video = me.VideoFileClip("fresh_prince.mp4").subclip(0, 20)
audio = video.audio
duration = video.duration

angle = 0
z = 1.5
shake = 35

output_video_frames = []
video
output_audio_frames = video.audio.to_soundarray()
frames_processed = 0
# audio_stutter_len = 3000
audio_stutter_len = 2000
stutter_counter = 0
k = 0
t = 18

for i in tqdm(range(len(output_audio_frames))):
    stutter_counter += 1
    if stutter_counter >= audio_stutter_len:
        k += 1
        stutter_counter = 0
    if k > 20:
        t += 1
        k = 0

    output_audio_frames[i] = audio.get_frame(
        i % audio_stutter_len + t * video.audio.fps
    )

print("Audio done")

for t, video_frame in tqdm(video.iter_frames(with_times=True)):
    # cv2 expects BGR format
    video_frame = cv2.cvtColor(video_frame, cv2.COLOR_RGB2BGR)
    # output_audio_frames[int(t * audio.fps)] = audio.get_frame(stutter_counter)
    # ret, frame = cap.read()
    faces = FaceFeatureRecognizer.find_faces(video_frame)
    # faces = FaceFeatureRecognizer.face_centers(video_frame)
    # for face in faces:
    #     video_frame = ytp_effects.image.distort.swirl(video_frame, face, 3, 50)
    #     video_frame = ytp_effects.image.distort.bulge(video_frame, 1.4, center=face)
    #     output_audio_frames.append(output_audio_frames[-1])
    # else:
    # if len(faces) > 0:
    # for i in range(
    #     int(t * audio.fps),
    #     int(min(len(output_audio_frames) - 1, (t + 1 / video.fps) * audio.fps,)),
    # ):
    #     output_audio_frames[i] = output_audio_frames[int(t * audio.fps)]
    # output_audio_frames.append(audio_frame)

    video_frame = ytp_effects.image.fry.deep_fry(video_frame, faces)
    # frame = ytp_effects.image.translate.translate(
    #     frame, random.randrange(-shake, shake), random.randrange(-shake, shake)
    # )
    # zoomish = random.uniform(z / 2, z)
    # frame = ytp_effects.image.zoom.zoom(frame, zoomish, zoomish)
    # # frame = ytp_effects.image.spin.rotate(frame, angle)
    # frame = ytp_effects.image.distort.pixelate(frame, 12)
    # cv2.imshow("frame", video_frame)
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
    # angle += -25
    output_video_frames.append(video_frame)
    # frames_processed += 1
    # print(
    #     f"Processing {100*frames_processed/(video.fps * video.duration):.3f}%\r", end=""
    # )

# cv2.destroyAllWindows()
# output_audio_frames = audio
output_video = me.ImageSequenceClip(output_video_frames, video.fps)
output_video.audio = AudioArrayClip(output_audio_frames, audio.fps)
output_video.write_videofile("test.mp4")
