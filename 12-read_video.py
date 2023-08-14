import cv2
import numpy as np

cap = cv2.VideoCapture("data/output.avi")

# width = int(cap.get(3)) # Width
# height = int(cap.get(4)) # Height
#
# # Define a codec (Windows: DIVX, IOS & Linux: XVID)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

i = 0
while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        i += 1
        cv2.putText(frame, 'frame:' + str(i), (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 255), 2)
        # out.write(frame)
        cv2.imshow("Video", frame)
        # cv2.imshow("Gray", gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()