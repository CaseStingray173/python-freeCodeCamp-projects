import time
import cv2 as cv
import numpy as np
import Hand_Tracking as ht
import autopy as ap

prev_time = 0
w_cam, h_cam = 640, 480
frame_red = 100  # Frame Reduction
smoothening = 7
w_screen, h_screen = ap.screen.size()
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0


cap = cv.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

detector = ht.hand_detector(max_num_hands=1)

while True:
    # 1. FIND HAND LANDMARKS
    success, img = cap.read()
    img = detector.find_hands(img)
    lms_list, bbox = detector.find_pos_bbox(img)

    # 2. GET THE TIP OF THE INDEX AND MIDDLE FINGERS
    if len(lms_list) != 0:
        x_1, y_1 = lms_list[8][1:]
        x_2, y_2 = lms_list[12][1:]

        # 3. CHECK WHICH FINGERS ARE UP
        fingers = detector.fingers_up()
        cv.rectangle(img, (frame_red, frame_red), (w_cam - frame_red, h_cam - frame_red), (255, 0, 255), 2)
        # 4. ONLY INDEX FINGER : MOVING MODE
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. CONVERT COORDINATES
            x_3 = np.interp(x_1, (frame_red, w_cam - frame_red), (0, w_screen))
            y_3 = np.interp(y_1, (frame_red, h_cam - frame_red), (0, h_screen))

            # 6. SMOOTHEN VALUES
            curr_x = prev_x + (x_3 - prev_x) / smoothening
            curr_y = prev_y + (y_3 - prev_y) / smoothening

            # 7. MOVE MOUSE
            ap.mouse.move(w_screen - curr_x, curr_y)
            cv.circle(img, (x_1, y_1), 10, (255, 0, 255), cv.FILLED)
            prev_x, prev_y = curr_x, curr_y

        # 8. BOTH INDEX AND MIDDLE FINGERS ARE UP : CLICKING MODE
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. FIND DISTANCE BETWEEN FINGERS, IF DISTANCE SHORT CLICK MOUSE
            length, img, line_info = detector.find_distance(8, 12, img)
            if length < 35:
                cv.circle(img, (line_info[4], line_info[5]), 10, (0, 255, 0), cv.FILLED)
                ap.mouse.click()

    # 10. FRAME RATE
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv.putText(img, f"FPS: {int(fps)}", (20, 50), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv.imshow("Mouse Pointer", img)
    cv.waitKey(1)
