import mediapipe as mp
import cv2 as cv
import time

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv.VideoCapture("dance.mp4")
prev_time = 0
while True:
    success, temp = cap.read()
    img = cv.resize(temp, (750, 750))
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    # # Prints the landmarks coordinates
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        for id, lms in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, ": ", lms)
            cx, cy = int(lms.x * w), int(lms.y * h)
            cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)


    # Getting the fps for the video
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Displaying the video
    cv.imshow("Image", img)
    cv.waitKey(1)
