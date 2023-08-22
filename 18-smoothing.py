import cv2
import numpy as np

image = cv2.imread("data/einstein.jpeg", 0)

noise = np.random.normal(0, 1, image.size).reshape(image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)
# Average blurring
blur = cv2.blur(noisy_image, (7, 7))
# Gaussian blurring
guassian = cv2.GaussianBlur(noisy_image, (7, 7), 0)
# Median
median = cv2.medianBlur(noisy_image, 7)
# Bilateral
bilateral = cv2.bilateralFilter(noisy_image, 7, 75, 75)

cv2.imshow("Original", image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Average", blur)
cv2.imshow("Gaussian", guassian)
cv2.imshow("Median", median)
cv2.imshow("Bilatral", bilateral)
cv2.waitKey(0)