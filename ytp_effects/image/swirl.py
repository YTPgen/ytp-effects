from skimage.transform import swirl as skswirl
import numpy


def swirl(
    image: numpy.ndarray, center: numpy.ndarray = None, strength: float = 1, radius=100
):
    return skswirl(image, center, strength=strength, radius=radius)
