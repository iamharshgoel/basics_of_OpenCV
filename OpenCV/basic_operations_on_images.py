import numpy as np
from cv2 import cv2

img = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)

print(img.shape)  # returns a tuple of number of rows, columns and channels
print(img.size)  # returns Total number of pixels is accessed
print(img.dtype)  # returns Image datatype is obtained
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]  # make a copy of ball
img[273:333, 100:160] = ball  # place to different coordinates

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#output = cv2.add(img, img2)
output = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
