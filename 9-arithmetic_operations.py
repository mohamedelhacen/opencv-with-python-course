import cv2
import numpy as np

# x = np.uint8([250]) # one element array [250]
# y = np.uint8([10]) # [10]
#
# # Normal Addition
# # in the scale of [0, 256]
# print(x + y) # 250 + 10 = 260 // 256
#
# # OpenCV Addition, in the scale of [0, 255]
# print(cv2.add(x, y)) # 250 + 20 = 260 ---> 255

img1 = cv2.imread("data/apple.jpg")
img2 = cv2.imread("data/baboon.jpg")

# # Normal addition
# normal_addition = img1 + img2
# # Opencv Addition
# opencv_addition = cv2.add(img1, img2)
# # blend two images
# weighted_image = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

# Bitwise operations: Not, Or, Xor, ...

not_operation = cv2.bitwise_not(img1, img2)
and_operation = cv2.bitwise_and(img1, img2)
or_operation = cv2.bitwise_or(img1, img2)
xor_operation = cv2.bitwise_xor(img1, img2)

cv2.imshow("Not image", not_operation)
cv2.imshow("And image", and_operation)
cv2.imshow("Or image", or_operation)
cv2.imshow("Xor image", xor_operation)


# cv2.imshow("Weighted image", weighted_image)
# cv2.imshow("Normal Addition", normal_addition)
# cv2.imshow("Opencv Addition", opencv_addition)
# cv2.imshow("Image 1", img1)
# cv2.imshow("Image 2", img2)
cv2.waitKey(0)

