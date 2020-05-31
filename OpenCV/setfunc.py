from cv2 import cv2
import datetime

capture = cv2.VideoCapture(0)
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text = 'Width: ' + str(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) + \
            ' Height:' + str(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 500), font, 1,
                            (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


capture.release()
cv2.destroyAllWindows()
