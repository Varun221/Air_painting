"""
AIR - PAINTING
This program is a paint application - BUT IN AIR !!
It lets you select, colors and brush sizes as you paint in air.
All along with a save option.
"""

import cv2
import numpy as np

# colour definitions
red = (4, 4, 247)
yellow = (4, 255, 255)
green = (4, 255, 4)
blue = (255, 4, 4)
white = (255, 255, 255)
cyan = (255, 255, 4)
purple = (153, 0, 153)
pink = (127, 0, 255)
orange = (0, 127, 255)
grey = (160, 160, 160)
black = (0, 0, 0)
brown = (0, 76, 153)
box1 = (0, 102, 204)
box2 = (128, 255, 0)
box3 = (153, 153, 255)

# These are the selected colours by the user
# default selection values
sel_col = red
sel_bsh = 1

# Some variables for smooth processing
cx = 0
cy = 0
fresh = True
saveonce = False
savestat = True

# contains the coordinates, color, brush size, hold status
store = np.zeros((1, 7), dtype=np.int32)
first = True

# These are the ranges for the pointer, feel free to change according to your needs
lower_bound = np.array([75, 130, 130])
upper_bound = np.array([130, 255, 255])

# these are the rangers for the holder.
hold_low = np.array([140, 50, 200])
hold_up = np.array([165, 180, 255])
hold = False

# you wanna paint or not?
painting = False


# This function checks if a "button" is pressed or not
def rangecheck(x, y, a, b):
    """ return true if (a,b) lies in the square of (x,y) with 14 as side"""
    if (a < x + 7 and a > x - 7 and b < y + 7 and b > y - 7):
        return True
    else:
        return False


cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()
    """
    4 videos are setup here,
    1. frame - this undergoes processing in order to produce mask
    2. mask - the black and white image that is used to detect contours
    3. paint - this contains our drawing and palette and whatever the user paints
    4. orig -  the original footage
    """

    # flip and resize
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (900, 650))
    # The changes and painting will be made in paint
    paint = frame.copy()
    orig = frame.copy()
    paint = np.uint8(paint)

    # cv2.imshow('feed',frame)

    """CREATING THE PALETTE"""""

    # The border lines
    paint = cv2.line(paint, (0, 650 - 50), (900 - 75, 650 - 50), (0, 0, 0), 3)
    paint = cv2.line(paint, (0, 648 - 50), (900 - 75, 648 - 50), brown, 1)
    paint = cv2.line(paint, (900 - 75, 0), (900 - 75, 650 - 50), (0, 0, 0), 3)
    paint = cv2.line(paint, (898 - 75, 0), (898 - 75, 650 - 50), brown, 1)

    # filling the palette
    paint[:, 827:900] = paint[603:650, :] = white

    # colours in the pallete along with their black border
    paint = cv2.circle(paint, (825 + 5 + 15, 5 + 15), 15, red, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 5 + 15), 15, black, 1)

    paint = cv2.circle(paint, (825 + 5 + 15, 40 + 15), 15, yellow, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 40 + 15), 15, black, 1)

    paint = cv2.circle(paint, (825 + 5 + 15, 75 + 15), 15, green, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 75 + 15), 15, black, 1)

    paint = cv2.circle(paint, (825 + 5 + 15, 110 + 15), 15, blue, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 110 + 15), 15, black, 1)

    paint = cv2.circle(paint, (825 + 5 + 15, 145 + 15), 15, white, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 145 + 15), 15, black, 1)

    paint = cv2.circle(paint, (825 + 5 + 15, 180 + 15), 15, black, -1)
    paint = cv2.circle(paint, (825 + 5 + 15, 180 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 5 + 15), 15, cyan, -1)
    paint = cv2.circle(paint, (860 + 15, 5 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 40 + 15), 15, purple, -1)
    paint = cv2.circle(paint, (860 + 15, 40 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 75 + 15), 15, pink, -1)
    paint = cv2.circle(paint, (860 + 15, 75 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 110 + 15), 15, orange, -1)
    paint = cv2.circle(paint, (860 + 15, 110 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 145 + 15), 15, grey, -1)
    paint = cv2.circle(paint, (860 + 15, 145 + 15), 15, black, 1)

    paint = cv2.circle(paint, (860 + 15, 180 + 15), 15, brown, -1)
    paint = cv2.circle(paint, (860 + 15, 180 + 15), 15, black, 1)

    # brush sizes
    paint = cv2.line(paint, (835, 240), (890, 240), brown, 1)
    paint = cv2.line(paint, (835, 240 + 40), (890, 240 + 40), brown, 3)
    paint = cv2.line(paint, (835, 240 + 80), (890, 240 + 80), brown, 5)
    paint = cv2.line(paint, (835, 240 + 120), (890, 240 + 120), brown, 7)
    paint = cv2.line(paint, (835, 240 + 160), (890, 240 + 160), brown, 9)

    # start, stop and save buttons
    # start with lines
    paint = cv2.line(paint, (825, 450), (900, 450), black, 2)
    paint = cv2.line(paint, (825, 500), (900, 500), black, 2)
    paint = cv2.line(paint, (825, 550), (900, 550), black, 2)
    paint = cv2.line(paint, (825, 600), (900, 600), black, 2)

    # Then the boxes
    paint[452:498, 828:898] = box1
    paint[502:548, 828:898] = box2
    paint[548:598, 828:898] = box3

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    paint = cv2.putText(paint, 'START', (828, 478), font, 0.9, black)
    paint = cv2.putText(paint, 'STOP', (832, 528), font, 0.92, black)
    paint = cv2.putText(paint, 'SAVE', (832, 578), font, 0.92, black)

    # displaying the selected color -
    if painting == True:
        paint = cv2.line(paint, (832, 640), (892, 640), sel_col, thickness=sel_bsh)

    # Signature
    font2 = cv2.FONT_HERSHEY_COMPLEX
    paint = cv2.putText(paint, 'AIR_PAINTING - BY YERRAM VARUN', (40, 640), font2, 1, (204, 0, 0), 2)
    paint = cv2.rectangle(paint, (36, 610), (640, 650), (0, 255, 255), 3)

    """CREATING THE MASK"""""
    kernel = np.ones((5, 5), np.uint8)
    frame = cv2.dilate(frame, kernel, iterations=2)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    hold_mask = cv2.inRange(frame_hsv, hold_low, hold_up)
    hold_mask = cv2.GaussianBlur(hold_mask, (7, 7), 0)

    hold_vals = hold_mask == 255
    if np.sum(hold_vals) > 3000:
        hold = True
    else:
        hold = False
    print(hold)

    """PLACING THE POINTER ON THE PAINT"""""
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        cnt = max(contours, key=cv2.contourArea)
        # if cv2.contourArea(cnt) >00:
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        if cx >= 825 or cy >= 600:
            # using different cursor in palette
            paint = cv2.circle(paint, (cx, cy), 2, black, -1)
        else:
            paint = cv2.line(paint, (cx - 5, cy), (cx + 5, cy), (0, 0, 255), 2)
            paint = cv2.line(paint, (cx, cy - 5), (cx, cy + 5), (0, 0, 255), 2)
    else:
        if fresh == True:
            paint = cv2.putText(paint, 'CLICK START', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            fresh = False

    """LETS PUT LIFE INTO THIS BABY"""""

    # The start button
    if rangecheck(863, 475, cx, cy):
        painting = True

    # the stop button
    if rangecheck(863, 525, cx, cy):
        painting = False

    # the save button
    if rangecheck(863, 570, cx, cy):
        savestat = True

    # hold status
    paint = cv2.putText(paint, 'HOLD : {}'.format(hold), (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 100), 2)

    # Painting status
    if painting == True:

        paint = cv2.putText(paint, 'PAINT ON', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # colors
        if rangecheck(825 + 5 + 15, 5 + 15, cx, cy):
            sel_col = red
        if rangecheck(825 + 5 + 15, 40 + 15, cx, cy):
            sel_col = yellow
        if rangecheck(825 + 5 + 15, 75 + 15, cx, cy):
            sel_col = green
        if rangecheck(825 + 5 + 15, 110 + 15, cx, cy):
            sel_col = blue
        if rangecheck(825 + 5 + 15, 145 + 15, cx, cy):
            sel_col = white
        if rangecheck(825 + 5 + 15, 180 + 15, cx, cy):
            sel_col = black
        if rangecheck(860 + 15, 5 + 15, cx, cy):
            sel_col = cyan
        if rangecheck(860 + 15, 40 + 15, cx, cy):
            sel_col = purple
        if rangecheck(860 + 15, 75 + 15, cx, cy):
            sel_col = pink
        if rangecheck(860 + 15, 110 + 15, cx, cy):
            sel_col = orange
        if rangecheck(860 + 15, 145 + 15, cx, cy):
            sel_col = grey
        if rangecheck(860 + 15, 180 + 15, cx, cy):
            sel_col = brown

        # lines
        if rangecheck(860, 240, cx, cy):
            sel_bsh = 1
        if rangecheck(860, 280, cx, cy):
            sel_bsh = 3
        if rangecheck(860, 320, cx, cy):
            sel_bsh = 5
        if rangecheck(860, 360, cx, cy):
            sel_bsh = 7
        if rangecheck(860, 400, cx, cy):
            sel_bsh = 9

        # Let's do the painting now
        # The coordinates are loaded to store.
        if first == False:
            y = np.zeros((1, 7), np.int32)
            y[0, 0] = cx
            y[0, 1] = cy
            (y[0, 2], y[0, 3], y[0, 4]) = sel_col
            y[0, 5] = sel_bsh
            y[0, 6] = hold
            if cx < 820 and cy < 600:
                store = np.append(store, y, axis=0)

        if first == True:
            if cx < 820 and cy < 600:
                store[0, 0] = cx
                store[0, 1] = cy
                (store[0, 2], store[0, 3], store[0, 4]) = sel_col
                store[0, 5] = sel_bsh
                store[0, 6] = hold
                first = False

    else:
        paint = cv2.putText(paint, 'CLICK START', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    i = 0
    for i in range(store.shape[0] - 1):
        if store[i, 6] == False:
            paint = cv2.line(paint,
                             (int(store[i, 0]), int(store[i, 1])),
                             (int(store[i + 1, 0]), int(store[i + 1, 1])),
                             (int(store[i, 2]), int(store[i, 3]), int(store[i, 4])),
                             thickness=int(store[i, 5])
                             )
    # you can save the file once.
    if painting == False and saveonce == False and savestat == True:
        cv2.imwrite('save.png', paint)
        save = True

    cv2.imshow('paint', paint)
    # cv2.imshow('store', paintstore)
    #cv2.imshow('hold_mask', hold_mask)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
