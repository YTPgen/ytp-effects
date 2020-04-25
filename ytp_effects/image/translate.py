import cv2
import numpy as np


def translate(image: np.ndarray, by_x: float, by_y: float):
    """Translates an image by given x and y.
    All pixels will be moved by (x,y) and empty spaces filled by black.

    Args:
        image (np.ndarray): Image to translate
        by_x (float): Translation on X axis
        by_\y (float): Translation on Y axis
    """
    T = np.float32([[1, 0, by_x], [0, 1, by_y]])
    return cv2.warpAffine(image, T, (image.shape[1], image.shape[0]))
