from cv2 import cv2

capture = cv2.VideoCapture('vtest.avi')

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        print("Frame Width: {0}".format(width))
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Frame Height: {0}".format(height))
        fps = capture.get(cv2.CAP_PROP_FPS)
        print("Frames per second: {0}".format(fps))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


capture.release()
cv2.destroyAllWindows()
