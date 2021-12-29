import math
import time
from ctypes import cast, POINTER
import cv2 as cv
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import Hand_Tracking as ht

cap = cv.VideoCapture(0)
cam_wid, cam_hei = 640, 480
cap.set(3, cam_wid)
cap.set(4, cam_hei)
prev_time = 0

detector = ht.hand_detector(min_detection_confidence=0.75)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume_range = volume.GetVolumeRange()
min_vol = volume_range[0]
max_vol = volume_range[1]
vol = 0
vol_bar = 400
vol_per = 0
while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lms_list = detector.find_position(img, draw=False)

    if len(lms_list) != 0:
        # print(lms_list[4], lms_list[8])
        x_1, y_1 = lms_list[4][1], lms_list[4][2]
        x_2, y_2 = lms_list[8][1], lms_list[8][2]
        c_x, c_y = (x_1 + x_2) // 2, (y_1 + y_2) // 2

        cv.circle(img, (x_1, y_1), 10, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x_2, y_2), 10, (255, 0, 255), cv.FILLED)
        cv.line(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)
        cv.circle(img, (c_x, c_y), 10, (255, 0, 0), cv.FILLED)

        length = math.hypot(x_2 - x_1, y_2 - y_1)
        print(length)

        # Hand range 50 - 300, Volume range -65 - 0
        vol = np.interp(length, [20, 205], [min_vol, max_vol])
        vol_bar = np.interp(length, [50, 300], [400, 150])
        vol_per = np.interp(length, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv.circle(img, (c_x, c_y), 10, (0, 0, 255), cv.FILLED)

    cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(img, f"{int(vol_per)}%", (50, 450), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 2)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img, f"FPS: {int(fps)}", (10, 70), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    cv.imshow("Volume Control", img)
    cv.waitKey(10)
