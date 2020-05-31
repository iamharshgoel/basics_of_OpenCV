import numpy as np
from cv2 import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, heirarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))

cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

cv2.imshow('image', img)
cv2.imshow('Gray Image', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
