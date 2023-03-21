import cv2

def hsv(src) :
    dst2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    return dst2

def binary(src):
    dst3 = src.copy()
    _, dst3 = cv2.threshold(dst3, 127, 255, cv2.THRESH_BINARY)
    return dst3
    
