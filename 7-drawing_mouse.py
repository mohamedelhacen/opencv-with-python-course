import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(image, (x, y), 20, (255, 0, 0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.putText(image, "RButton clicked", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

image = np.full((512, 512, 3), 255, dtype=np.uint8)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_circle)

while True:
    cv2.imshow("Image", image)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()