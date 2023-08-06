import cv2
import numpy as np

messi = cv2.imread("data/messi5.jpg")
logo = cv2.imread("data/logo.png")

rows, cols, channels = logo.shape
roi = messi[150:rows+150, 100:cols+100]

# Create a mask from logo and the inverse mask
logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(logoGray, 10, 255, cv2.THRESH_BINARY)
inv_mask = cv2.bitwise_not(mask)

# black-out area of mask in the roi
img1_bg = cv2.bitwise_and(roi, roi, mask=inv_mask)

# Taking just the logo arcs
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)

result = cv2.add(img1_bg, logo_fg)
messi[150:rows+150, 100:cols+100] = result

# cv2.imshow("logo fg", logo_fg)
# cv2.imshow("Img back", img1_bg)
# cv2.imshow("Mask", mask)
# cv2.imshow("Inv Mask", inv_mask)

cv2.imshow("Messi", messi)
# cv2.imshow("Logo", logo)
cv2.waitKey(0)