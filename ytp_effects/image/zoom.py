import scipy.ndimage
import numpy
import cv2


def zoom(
    image: numpy.ndarray, factor_x: float, factor_y: float, center_on: tuple = None
) -> numpy.ndarray:
    """Zooms in on a location in an image.
    
    Args:
        image (numpy.ndarray): Image to zoom in
        factor_x (float): Zoom factor on X axis
        factor_y (float): Zoom factor on Y axis
        center_on (tuple): Center of zoom (x,y)
    
    Returns:
        numpy.ndarray: Zoomed in image
    """
    (height, width) = image.shape[:2]
    scaled = cv2.resize(
        image, None, fx=factor_x, fy=factor_y, interpolation=cv2.INTER_LINEAR
    )
    if center_on == None:
        center_on = (height / 2, width / 2)
    else:
        center_on = (center_on[1], center_on[0])
    center_on = (center_on[0] * factor_y, center_on[1] * factor_x)

    crop_from_y = int(max(0, center_on[0] - height / 2))
    crop_to_y = int(min(height * factor_y, crop_from_y + height))

    crop_from_x = int(max(0, center_on[1] - width / 2))
    crop_to_x = int(min(width * factor_x, crop_from_x + width))
    cropped = scaled[crop_from_y:crop_to_y, crop_from_x:crop_to_x]

    # If image is smaller than before, pad with black
    if cropped.shape[0] < height or cropped.shape[1] < width:
        y_pad = max(0, height - cropped.shape[0])
        x_pad = max(0, width - cropped.shape[1])
        return cv2.copyMakeBorder(
            cropped,
            y_pad // 2,
            y_pad - y_pad // 2,
            x_pad // 2,
            x_pad - x_pad // 2,
            cv2.BORDER_CONSTANT,
            value=[0, 0, 0],
        )

    return cropped
