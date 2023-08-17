import cv2
import numpy as np

image = cv2.imread("data/starry_night.jpg")
grayscal_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
print(grayscal_image.shape)

print(image.size)
print(grayscal_image.size)

print(type(image))
print(type(grayscal_image))

print(image.dtype)
print(grayscal_image.dtype)

cv2.imshow("BGR Image", image)
cv2.imshow("Grayscal Image", grayscal_image)
cv2.imshow("RGB Image", rgb_image)
cv2.imwrite('gray.jpg', grayscal_image)
cv2.imwrite('rgb.jpg', rgb_image)
cv2.waitKey(0)