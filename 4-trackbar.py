import cv2
import numpy as np


def nothing(x):
    pass


image = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow("Trackbar")

cv2.createTrackbar("R", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("G", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("B", "Trackbar", 0, 255, nothing)

# print(image.shape)
while True:
    b = cv2.getTrackbarPos("B", "Trackbar")
    g = cv2.getTrackbarPos("G", "Trackbar")
    r = cv2.getTrackbarPos("R", "Trackbar")

    # print((b, g, r)) # Print the values of the trackbar
    image[:] = (b, g, r)

    cv2.imshow("Image", image)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()