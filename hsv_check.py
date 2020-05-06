# checks if the lower and upper bounds work

import cv2
import numpy as np
import time
w = 100
h = 200
x1 = 117
y = 103
lower_bound = np.array([75,170,243])
upper_bound = np.array([130,255, 255])
values = np.array([])


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #frame = cv2.GaussianBlur(frame, (5,5),0)
    cv2.imshow('feed', frame)
    kernel = np.ones((5, 5), np.uint8)
    frame = cv2.dilate(frame, kernel, iterations=2)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('mask', mask)



    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()