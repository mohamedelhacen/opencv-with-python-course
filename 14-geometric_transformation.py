import cv2
import numpy as np

image = cv2.imread("data/messi5.jpg")
print(image.shape)
height, width = image.shape[:2]
# Resize images
# resized_image = cv2.resize(image, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)
# print(resized_image.shape)
#
# resized_image2 = cv2.resize(image, None, fx=2, fy=2)
# print(resized_image2.shape)


# Translation
# Create a Matrix Translation M = [[1, 0, tx] [0, 1, ty]]
# M = np.float32([[1, 0, 50], [0, 1, 20]])
# translated = cv2.warpAffine(image, M, (width, height))

# Rotation
M = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
rotated = cv2.warpAffine(image, M, (width, height))

cv2.imshow("Original", image)
cv2.imshow("Rotated", rotated)
# cv2.imshow("Translated", translated)
# cv2.imshow("Resized", resized_image)
# cv2.imshow("Resized 2", resized_image2)
cv2.waitKey(0)