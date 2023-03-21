import cv2


def gray(src):
    dst1 = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    return dst1
