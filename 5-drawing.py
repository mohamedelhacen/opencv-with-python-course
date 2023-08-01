import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.line(image, (0, 0), (511, 511), (255, 0, 0), 3)

cv2.rectangle(image, (10, 50), (200, 400), (0, 0, 255), 3)
cv2.circle(image, (128, 128), 60, (0, 255, 0), 5)

cv2.putText(image, "OpenCV with Python", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.ellipse(image, (256, 256), (200, 100), 45, 180, 360, (0, 255, 0), -1)

pts = np.array([[10, 5], [300, 200], [100, 100], [256, 50]], np.int32)
cv2.polylines(image, [pts], False, (0, 0, 255), 5)

cv2.imshow("Image", image)
cv2.imwrite("data/drawing.png", image)
cv2.waitKey(0)