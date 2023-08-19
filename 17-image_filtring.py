import cv2
import numpy as np

image = cv2.imread("data/sudoku.png")

# Blurring
kernel1 = np.ones((5, 5), np.float32) / 25
blured = cv2.filter2D(image, -1, kernel1)

# Sharpening
kernel2 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, kernel2)

cv2.imshow("Original", image)
cv2.imshow("Blured", blured)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)