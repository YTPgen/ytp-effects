import cv2
import numpy


def invert(image: numpy.ndarray):
    return cv2.bitwise_not(image)


def add_red(image: numpy.ndarray, amount):
    pass
