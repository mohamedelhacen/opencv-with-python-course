import cv2
import numpy as np

# image = np.zeros((400, 400), dtype=np.uint8)
#
# cv2.putText(image, "OpenCV", (10, 220), cv2.FONT_HERSHEY_COMPLEX,
#             3, (255), 5)
image = cv2.imread('data/j.png')

kernel = np.ones((5, 5), np.uint8)
# Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# Opening: Erosion + Dilation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# Closing: Dilation + Erosion
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Gradient: Erosion - Dilation
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Tophat: image - opening
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Blackhat: closing - image
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow("Original", image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)