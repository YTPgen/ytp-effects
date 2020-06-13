# import the necessary packages
import cv2
import ytp_effects
import face_feature_recognizer
from face_feature_recognizer.face_feature_recognizer import FaceFeatureRecognizer

# load the image and show it
frame = cv2.imread("jv.jpg")

face_info = FaceFeatureRecognizer.find_faces(frame)
face_pos = FaceFeatureRecognizer.face_centers(frame)[0]

# frame = ytp_effects.image.d.swirl(frame, face_pos, 3, 200)
# frame = ytp_effects.image.fry.deep_fry(frame, face_info)
# frame = ytp_effects.image.fry.space_fry(frame)
# rotated = ytp_effects.image.spin.rotate(image, 150, 0.5)
# frame = ytp_effects.image.invert.invert(frame)
# frame = ytp_effects.image.fry.space_fry(frame)
# rotated = ytp_effects.image.zoom.zoom(frame, 3.5, 1, center_on=face_pos)
# frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
frame = ytp_effects.image.distort.bulge(frame, -5, center=face_pos)
cv2.imshow("rotated", frame)
cv2.waitKey(0)
