import time
import cv2 as cv
import Hand_Tracking as ht

w_cam, h_cam = 640, 480
cap = cv.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

prev_time = 0
detector = ht.hand_detector(min_detection_confidence=0.75)
fing_tip_ids = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lms_list = detector.find_position(img, draw=False)

    if len(lms_list) != 0:
        fingers = []

        # Thumb
        # NOTE: To detect the thumb on right hand use ">". To detect thumb on left hand
        #       use "<"
        if lms_list[fing_tip_ids[0]][1] > lms_list[fing_tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lms_list[fing_tip_ids[id]][2] < lms_list[fing_tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        total_fingers = fingers.count(1)

        cv.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv.FILLED)
        cv.putText(img, str(total_fingers), (45, 375), cv.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img, f"FPS: {int(fps)}", (20, 70), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

    cv.imshow("Finger Counter", img)
    cv.waitKey(1)
