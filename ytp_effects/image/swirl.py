import skimage.transform
import numpy


def swirl(
    image: numpy.ndarray, center: numpy.ndarray = None, strength: float = 1, radius=100
):
    return skimage.transform.swirl(image, center, strength=strength, radius=radius)
