import cv2
import numpy as np

image = cv2.imread('data/sudoku.png', 0)

blur = cv2.bilateralFilter(image, 7, 75, 75)

edges = cv2.Canny(blur, 70, 200)

cv2.imshow("Original", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)