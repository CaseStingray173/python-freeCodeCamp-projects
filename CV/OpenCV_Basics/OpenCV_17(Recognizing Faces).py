import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

celebs = ["Ben Afflek", "Elton John", "Jerry Seinfeld", "Madonna", "Mindy Kaling"]

# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

test_img = cv.imread("val/ben_afflek/1.jpg")
gray = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)

cv.imshow("Celeb", gray)

# Detecting the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f"Label = {celebs[label]} with a confidence of {confidence}")

    cv.putText(test_img, str(celebs[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
    cv.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Detected Face", test_img)

cv.waitKey(0)