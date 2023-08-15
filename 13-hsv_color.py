import cv2
import numpy as np

def nothing(x):
    pass

image = cv2.imread('data/baboon.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow("HSV")
cv2.createTrackbar("H Min", "HSV", 0, 179, nothing)
cv2.createTrackbar("S Min", "HSV", 0, 255, nothing)
cv2.createTrackbar("V Min", "HSV", 0, 255, nothing)

cv2.createTrackbar("H Max", "HSV", 179, 179, nothing)
cv2.createTrackbar("S Max", "HSV", 255, 255, nothing)
cv2.createTrackbar("V Max", "HSV", 255, 255, nothing)

while True:

    h_min = cv2.getTrackbarPos("H Min", "HSV")
    s_min = cv2.getTrackbarPos("S Min", "HSV")
    v_min = cv2.getTrackbarPos("V Min", "HSV")

    h_max = cv2.getTrackbarPos("H Max", "HSV")
    s_max = cv2.getTrackbarPos("S Max", "HSV")
    v_max = cv2.getTrackbarPos("V Max", "HSV")

    # Hue in the range of [0, 179], Sat & Value in range of [0, 255]
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Original", image)
    cv2.imshow('Result', result)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()