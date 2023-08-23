import cv2
import numpy as np

image = cv2.imread("data/leuvenA.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_inv = 255 - gray

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("ksize", "Trackbar", 7, 100, nothing)

while True:
    ksize = cv2.getTrackbarPos("ksize", "Trackbar")
    if ksize % 2 == 0:
        ksize += 1

    blur = cv2.GaussianBlur(gray_inv, (ksize, ksize), 0)
    result = cv2.divide(gray, 255 - blur, scale=256)
    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    # cv2.putText(result, f"Ksize: {str(ksize)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
    #             1, (0, 0, 255), 2)
    cv2.imshow("Original", image)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()