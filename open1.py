import cv2

def hsv(src) :
    dest = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    return dest

def binary(src):
    dst3 = src.copy()
    _, dst3 = cv2.threshold(dst3, 127, 255, cv2.THRESH_BINARY)
    return dest
    
