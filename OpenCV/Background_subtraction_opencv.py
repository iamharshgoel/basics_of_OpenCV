import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.bgsegm_BackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
#kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (3, 3))
#fgbg = cv2.bgsegm_BackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()
