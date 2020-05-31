import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)

cv2.imshow('Original Image', img)
cv2.imshow('PyrDown 1 Image', lr1)
cv2.imshow('PyrDown 2 Image', lr2)
cv2.imshow('PyrUp 1 image', hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()
