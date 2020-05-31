import numpy as np
from cv2 import cv2

image = cv2.imread('lena.jpg', 1)
image = cv2.line(image, (0, 0), (255, 255), (0, 0, 255), 2)
image = cv2.arrowedLine(image, (0, 0), (255, 255), (0, 255, 255), 2)
image = cv2.rectangle(image, (25, 70), (200, 170), (0, 255, 0), 5)
image = cv2.circle(image, (447, 63), 63, (255, 0, 0), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, "OpenCV", (10, 500), font,
                    5, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
