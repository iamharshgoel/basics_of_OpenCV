from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('road.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

roi_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]


def roi(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_line(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = roi(canny_image, np.array([roi_vertices], np.int32))

lines = cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/180,
                        threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)

image_with_lines = draw_line(image, lines)

plt.imshow(cropped_image)
plt.imshow(image_with_lines)
plt.show()
