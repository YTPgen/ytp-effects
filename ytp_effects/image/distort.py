import skimage.transform
import numpy as np
import cv2
import math


def swirl(
    image: np.ndarray, center: np.ndarray = None, strength: float = 1, radius=100
):
    return (
        skimage.transform.swirl(image, center, strength=strength, radius=radius) * 255
    )


def bulge(image: np.ndarray, strength: float, center: tuple = None) -> np.ndarray:
    """Creates a swelling or deflating effect in an image with a given center.

    Args:
        image (numpy.ndarray): Image to modify
        strength (float): Strength of inflation (can be negative)
        center (tuple, optional): Center of effect (x,y). Defaults to None.

    Returns:
        [type]: [description]
    """
    height, width = image.shape[:2]
    if center is None:
        center = (height // 2, width // 2)

    center_height = center[1]
    center_width = center[0]
    max_radius = min(center_width, center_height)
    dst = image.copy()

    for y in range(len(image)):
        v = y - center_height
        if abs(v) > max_radius:
            continue
        x_start = max(
            0, math.floor(-math.sqrt(max_radius ** 2 - v ** 2) + center_width)
        )
        x_end = min(
            width, math.ceil(math.sqrt(max_radius ** 2 - v ** 2) + center_width)
        )
        for x in range(x_start, x_end):
            u = x - center_width
            r = math.sqrt(u ** 2 + v ** 2)
            r = 1 - r / max_radius
            if r > 0:
                r2 = 1 - strength * r * r
                xp = u * r2
                yp = v * r2

                src_y = max(0, min(int(yp + center_height), height - 1))
                src_x = max(0, min(int(xp + center_width), width - 1))

                dst[y][x] = image[src_y][src_x]
    return dst


def pixelate(image: np.ndarray, strength):
    squish_strength = 1 + strength
    (height, width) = image.shape[:2]
    image = cv2.resize(
        image,
        (int(width / squish_strength), int(height / squish_strength)),
        interpolation=cv2.INTER_NEAREST,
    )
    return cv2.resize(image, (int(width), int(height)), interpolation=cv2.INTER_LINEAR,)
