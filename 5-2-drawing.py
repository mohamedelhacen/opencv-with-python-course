import cv2
import numpy as np

image = np.zeros((200, 512, 3), np.uint8) * 255

cv2.line(image, (0, 0), (511, 199), (255, 0, 0), 3)
cv2.line(image, (30, 50), (30, 150), (255, 0, 255), 3)

cv2.rectangle(image, (50, 50), (100, 150), (0, 0, 255), 3)
cv2.circle(image, (256, 100), 60, (0, 255, 0), -1)

cv2.putText(image, "OpenCV with Python", (100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.ellipse(image, (400, 100), (60, 30), 0, 0, 360, (255, 255, 0), -1)

pts = np.array([[110, 155], [250, 190], [180, 120]], np.int32)
cv2.polylines(image, [pts], True, (0, 255, 255), 3)

cv2.imshow("Image", image)
cv2.imwrite("drawing.png", image)
cv2.waitKey(0)