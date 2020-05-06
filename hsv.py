# takes an image and gives hsv values at any point

import cv2
import numpy as np

img = cv2.imread('check.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass
def callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, str(hsv[y,x]), (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,255,0) )
        print(hsv[y,x])

cv2.namedWindow('image')
cv2.setMouseCallback('image', callback)
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
