import mediapipe as mp
import cv2 as cv
import time

cap = cv.VideoCapture(0)
prev_time = 0
mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection()

while True:
    success, temp = cap.read()
    img = cv.resize(temp, (700, 700))
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # # Using inbuilt function to draw the box around face
            # mp_draw.draw_detection(img, detection)

            # print(detection.location_data.relative_bounding_box)

            # Making the box drawing manually
            bound_box_c = detection.location_data.relative_bounding_box
            h, w, c = img.shape
            bound_box = int(bound_box_c.xmin * w), int(bound_box_c.ymin * h), \
                        int(bound_box_c.width * w), int(bound_box_c.height * h)
            cv.rectangle(img, bound_box, (255, 0, 255), 2)
            cv.putText(img, f"{int(detection.score[0] * 100)}%",
                       (bound_box[0], bound_box[1]-20),
                       cv.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img, f"FPS: {int(fps)}", (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)
