import cv2
import numpy as np

image = cv2.imread("data/messi5.jpg") # Load the image in BGR color space

# image = cv2.imread("data/messi5.jpg", 0) # Load the image in grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image in grayscale

# blue_px = image[100, 100, 0] # Access the pixel with coordinate (100, 100, 0)
# image[100, 100, 2] = 0
# px = image[100, 100]
# print(px)

# roi = image[20: 200, 100:400]
# image[60: 240, 140: 440] = (255, 255, 255)

b, g, r = cv2.split(image) # Split channels
print(b.shape)
merged = cv2.merge((b, g, r)) # Merge channels
cv2.imshow("Blue Channel", b)
cv2.imshow("Gree Channel", g)
cv2.imshow("Red Channel", r)
cv2.imshow("Original", image)
cv2.imshow("Merge", merged)
# cv2.imshow("ROI", roi)
# cv2.imshow("Gray", gray_image)
cv2.waitKey(0)