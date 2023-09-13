import cv2
import numpy as np

image = cv2.imread("data/messi5.jpg")

A = image.copy()
print(A.shape)
gaussians = [A]
# Gaussian Pyramids
for i in range(3):
    A = cv2.pyrDown(A)
    gaussians.append(A)

# A1 = cv2.pyrDown(A)
# A2 = cv2.pyrDown(A1)
# A3 = cv2.pyrDown(A2)
# A4 = cv2.pyrDown(A3)
# A5 = cv2.pyrDown(A4)
# print(A5.shape)

# A5U = cv2.pyrUp(A5)
# A4U = cv2.pyrUp(A4)
# A3U = cv2.pyrUp(A3)
# A2U = cv2.pyrUp(A2)
# A1U = cv2.pyrUp(A1)
# print(A1U.shape)

# Laplacian Pyramids
top_laplacian = gaussians[-1]

laplacians = [top_laplacian]
for i in range(3, 0, -1):
    size = (gaussians[i-1].shape[1], gaussians[i-1].shape[0])
    GE = cv2.pyrUp(gaussians[i], dstsize=size)
    lap = cv2.subtract(gaussians[i-1], GE)
    laplacians.append(lap)


cv2.imshow("Original", image)
cv2.imshow("Layer1", laplacians[3])
cv2.imshow("Layer2", laplacians[2])
cv2.imshow("Layer3", laplacians[1])
# cv2.imshow("A1", A1U)
# cv2.imshow("A2", A2U)
# cv2.imshow("A3", A3U)
# cv2.imshow("A4", A4U)
# cv2.imshow("A5", A5U)

cv2.waitKey(0)