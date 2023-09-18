import cv2
import numpy as np

image = np.full((512, 512, 3), 255, dtype=np.uint8)

cv2.rectangle(image, (10, 50), (100, 400), (255, 0, 0), 2)
cv2.rectangle(image, (150, 150), (300, 300), (255, 0, 0), 2)
cv2.rectangle(image, (200, 200), (250, 250), (255, 0, 0), -1)
cv2.circle(image, (400, 300), 50, (0, 0, 255), -1)
cv2.line(image, (480, 50), (480, 400), (0, 255, 0), 2)
# image = cv2.imread('data/sudoku.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 127, 255)
_, edges = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(edges, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
# print(hierarchy)
cv2.drawContours(image, contours, -1, (0, 255, 255), 4)

cv2.imshow("Image", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)