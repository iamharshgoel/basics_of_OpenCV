from cv2 import cv2
import time

if __name__ == '__main__':

    capture = cv2.VideoCapture('vtest.avi')
    ret, frame = capture.read()
    if ret == True:
        fps = capture.get(cv2.CAP_PROP_FPS)
        print(
            "Frames per second using video.get(cv2.CAP_PROP_FPS): {0}".format(fps))

    num_frames = 120

    print("Capturing {0} frames".format(num_frames))

    start = time.time()

    for i in range(0, num_frames):
        ret, frame = capture.read()

    end = time.time()
    seconds = end - start

    print("Time taken : {0} seconds".format(seconds))
    fps = num_frames / seconds
    print("Estimated frames per second : {0}".format(fps))

capture.release()
