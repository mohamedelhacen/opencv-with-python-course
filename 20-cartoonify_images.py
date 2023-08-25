import cv2
import numpy as np

image = cv2.imread('data/obama.jpeg')
# h, w, _ = image.shape
# image = cv2.resize(image, (int(w * 0.4), int(h * 0.4)))

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("ksize", "Trackbar", 7, 100, nothing)
cv2.createTrackbar("bsize", "Trackbar", 7, 100, nothing)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

while True:
    ksize = cv2.getTrackbarPos("ksize", "Trackbar")
    bsize = cv2.getTrackbarPos("bsize", "Trackbar")

    if ksize % 2 == 0:
        ksize += 1
    if bsize % 2 == 0:
        bsize += 1

    blur = cv2.medianBlur(gray, ksize)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, bsize, 2)
    result = cv2.bitwise_and(image, image, mask=edges)
    # cv2.putText(result, f"ksize: {str(ksize)} | bsize: {str(bsize)}", (20, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Original", image)
    cv2.imshow("Edges", edges)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.imwrite('edges.jpg', edges)
cv2.imwrite('result.jpg', result)
cv2.destroyAllWindows()