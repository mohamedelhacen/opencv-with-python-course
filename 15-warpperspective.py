import cv2
import numpy as np

image = cv2.imread("data/cards.png")
print(image.shape)
# For soduko image
# pts1 = np.float32([[70, 80], [500, 70], [30, 520], [530, 530]])
# pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

pts1 = np.float32([[120, 180], [190, 220], [65, 290], [140, 320]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
resulted = cv2.warpPerspective(image, M, (300, 300))

cv2.imshow("Original", image)
cv2.imshow("Result", resulted)
cv2.waitKey(0)