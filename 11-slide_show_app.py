import cv2
import numpy as np
import os

first_img = np.zeros((512, 512, 3), dtype=np.uint8)
images = "data/"

for file in os.listdir(images):

    img = cv2.imread(images + file)
    img = cv2.resize(img, (512, 512))

    for a in range(1, 11):
        a = a / 10
        b = 1 - a

        res = cv2.addWeighted(img, a, first_img, b, 0)
        cv2.putText(res, f"a:{a} and b:{b:.1f}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)
        cv2.imshow("Result", res)
        if cv2.waitKey(0) == ord("q"):
            break
    if cv2.waitKey(0) == ord("q"):
        break
    first_img = img

cv2.destroyAllWindows()