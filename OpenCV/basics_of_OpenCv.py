import cv2

image = cv2.imread('lena.jpg', 0)

print(image)

cv2.imshow('image', image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', image)
    cv2.destroyAllWindows()