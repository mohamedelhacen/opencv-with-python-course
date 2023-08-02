import cv2
import numpy as np

image = np.full((512, 512, 3), 255, dtype=np.uint8)

cv2.putText(image, 'OpenCV', (200, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 6)

cv2.ellipse(image, (256, 200), (90, 90), 120, 0, 300, (0, 0, 255), -1)
cv2.ellipse(image, (256, 200), (30, 30), 120, 0, 300, (255, 255, 255), -1)

cv2.ellipse(image, (160, 400), (90, 90), 0, 0, 300, (0, 255, 0), -1)
cv2.ellipse(image, (160, 400), (30, 30), 0, 0, 300, (255, 255, 255), -1)

cv2.ellipse(image, (360, 400), (90, 90), 300, 0, 300, (255, 0, 0), -1)
cv2.ellipse(image, (360, 400), (30, 30), 300, 0, 300, (255, 255, 255), -1)
cv2.imwrite("data/opencv-logo.png", image)
cv2.imshow("Image", image)
cv2.waitKey(0)