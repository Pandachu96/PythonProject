import cv2


def image_scaled_up(path, scale):
    img = cv2.imread(path)
    resized_up = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LANCZOS4)
    return resized_up