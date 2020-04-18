import numpy
import cv2


def rotate(
    image: numpy.ndarray, degrees: float, scale: float = 1, center: tuple = None
) -> numpy.ndarray:
    """Rotates an image.
    
    Args:
        image (numpy.ndarray): Image to rotate.
        center (tuple, optional): (x,y) tuple of center of rotation. Defaults to center of image.
        scale (float, optional): Scale of image after rotation. Defaults to 1.
    
    Returns:
        numpy.ndarray: Rotated image.
    """
    (height, width) = image.shape[:2]
    if center == None:
        center = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, degrees, scale)
    return cv2.warpAffine(image, rotation_matrix, (width, height))
