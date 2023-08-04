import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global drawing, mode, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(image, (x, y), 10, (255, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(image, (x, y), 10, (255, 0, 0), -1)

image = np.full((200, 512, 3), 255, dtype=np.uint8)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw)

while True:
    cv2.imshow("Image", image)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode # Change between drawing mode (circle or rectangle)
    elif k == ord('q'):
        break
cv2.imwrite("data/painted_image.png", image) # Save the resulted image
cv2.destroyAllWindows()