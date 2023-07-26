import cv2

image = cv2.imread("data/starry_night.jpg")

cv2.imshow("The Display Window", image)
cv2.imwrite("starry_night-saved.png", image)
cv2.waitKey(0)