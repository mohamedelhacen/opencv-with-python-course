import cv2
import numpy as np

apple = cv2.imread("data/apple.jpg")
orange = cv2.imread("data/orange.jpg")
assert apple.shape == orange.shape
A = apple.copy()
B = orange.copy()
cols, rows, _ = A.shape
# Normal Blending
normal_blending = np.hstack((A[:, :cols//2], B[:, cols//2:]))

# Image Pyramids Blending
# Gaussian Pyrmadis of A and B
gpA = [A]
for i in range(5): # 5 levels
    A = cv2.pyrDown(A)
    gpA.append(A)

gpB = [B]
for i in range(5): # 5 levels
    B = cv2.pyrDown(B)
    gpB.append(B)

# Laplacian Pyramids of A and B
lpA = [gpA[-1]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    LA = cv2.subtract(gpA[i - 1], GE)
    lpA.append(LA)

lpB = [gpB[-1]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    LB = cv2.subtract(gpB[i - 1], GE)
    lpB.append(LB)

LS = []
for la, lb in zip(lpA, lpB):
    cols, rows, _ = la.shape
    ls = np.hstack((la[:, :cols//2], lb[:, cols//2:]))
    LS.append(ls)

lsc = LS[0]
for i in range(1, 6):
    lsc = cv2.pyrUp(lsc)
    lsc = cv2.add(lsc, LS[i])


cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("Normal Blending", normal_blending)
cv2.imshow("Pyramid Blending", lsc)
cv2.waitKey(0)