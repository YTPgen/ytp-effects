import deeppyer
import numpy
import random
import asyncio
import cv2
from face_feature_recognizer.face import Face

from importlib_resources import files

_nani_eye = cv2.imread(
    files("ytp_effects.image.resources").joinpath("nani.png").as_posix(),
    cv2.IMREAD_UNCHANGED,
)


def overlay_eye(image: numpy.ndarray, center: tuple, size: float) -> numpy.ndarray:
    """Adds a shining eye overlay with given center.

    Args:
        image (numpy.ndarray): Image
        center (tuple): Center of eye effect (x,y)
    """
    # Resize nani eyes to fit face size
    nani_eye = cv2.resize(_nani_eye, (size, size))
    effect_h, effect_w, channels = nani_eye.shape
    # Detect the corners of the effect without going out of bounds
    y1, y2 = (
        max(0, center[1] - effect_h // 2),
        min(image.shape[0], center[1] + effect_h - effect_h // 2),
    )
    x1, x2 = (
        max(0, center[0] - effect_w // 2),
        min(image.shape[1], center[0] + effect_w - effect_w // 2),
    )
    # If we have gone out of bounds, calculate how much of the nani eyes to cut out
    nani_y1, nani_x1 = (
        max(0, -(center[1] - effect_h // 2)),
        max(0, -(center[0] - effect_w // 2)),
    )
    nani_y2, nani_x2 = (y2 - y1 + nani_y1, x2 - x1 + nani_x1)
    # Get the alpha channels to make effect transparent
    nani_alpha = nani_eye[nani_y1:nani_y2, nani_x1:nani_x2, 3] / 255.0
    original_alpha = 1.0 - nani_alpha
    try:
        for c in range(0, 3):
            image[y1:y2, x1:x2, c] = (
                nani_alpha * nani_eye[nani_y1:nani_y2, nani_x1:nani_x2, c]
                + original_alpha * image[y1:y2, x1:x2, c]
            )
    except ValueError as e:
        print(e)
    return image


def deep_fry(image: numpy.ndarray, faces: list):
    image = fry(image, color=(0, 0, 255))
    for f in faces:
        left_eye_pos = f.center_of(f.left_eye)
        right_eye_pos = f.center_of(f.right_eye)
        nani_eye_size = 2 * abs(left_eye_pos[0] - right_eye_pos[0])
        image = overlay_eye(image, left_eye_pos, nani_eye_size)
        image = overlay_eye(image, right_eye_pos, nani_eye_size)
    return image


def fry(image: numpy.ndarray, color: tuple = (5, 5, 200), color_strength: float = 0.4):
    (height, width) = image.shape[:2]
    # Place it in the frier
    color_filter = numpy.zeros_like(image)
    color_filter[:] = color
    image = cv2.addWeighted(color_filter, color_strength, image, 1 - color_strength, 0)

    # Season the image with artifacts
    image = cv2.resize(
        image, (int(width / 2.2), int(height / 2.2)), interpolation=cv2.INTER_NEAREST
    )
    image = cv2.resize(
        image, (int(width / 3.9), int(height / 3.9)), interpolation=cv2.INTER_AREA
    )
    image = cv2.resize(
        image, (width // 6, height // 6), interpolation=cv2.INTER_LANCZOS4
    )
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LANCZOS4)

    # Add some sharp salt
    kernel = numpy.array([[-1, -1, -1], [-1, 14, -1], [-1, -1, -1]])
    image = cv2.filter2D(image, -1, kernel)
    return image


def space_fry(image: numpy.ndarray):
    image[:, :, 0] -= 50  # (or 20)
    image[:, :, 1] -= 50
    image = cv2.addWeighted(image, 4, cv2.blur(image, (30, 30)), -4, 128)

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return image
