import cv2
import numpy as np

image = cv2.imread('data/sudoku.png', 0)

ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)

th1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Original", image)
cv2.imshow("Binary", thresh1)
cv2.imshow("Otsu", thresh)
cv2.imshow("Adaptive Mean", th1)
cv2.imshow("Adaptive Gaussian", th2)
# cv2.imshow("Binary Inv", thresh2)
# cv2.imshow("Trunc", thresh3)
# cv2.imshow("ToZero", thresh4)

cv2.waitKey(0)
