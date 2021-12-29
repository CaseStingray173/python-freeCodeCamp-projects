import mediapipe as mp
import cv2 as cv
import time

prev_time = 0
cap = cv.VideoCapture("people.mp4")
mp_draw = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=2)
draw_spec = mp_draw.DrawingSpec(thickness=2, circle_radius=1)
while True:
    success, temp = cap.read()
    img = cv.resize(temp, (750, 800))
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)
    if results.multi_face_landmarks:
        for face_lms in results.multi_face_landmarks:
            mp_draw.draw_landmarks(img, face_lms, mp_face_mesh.FACE_CONNECTIONS, draw_spec, draw_spec)
            for id, lms in enumerate(face_lms.landmark):
                # print(lms)
                h, w, c = img.shape
                x, y = int(lms.x * w), int(lms.y * h)
                print(id, ": ", x, y)
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img, f"FPS: {int(fps)}",
               (20, 70),
               cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv.imshow("Image", img)
    cv.waitKey(1)
