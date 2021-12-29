import os
import cv2 as cv
import numpy as np

celebs = ["Ben Afflek", "Elton John", "Jerry Seinfeld", "Madonna", "Mindy Kaling"]
DIR = r"C:\Users\patel\Desktop\Celebs"

haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []


def create_train():
    for celeb in celebs:
        path = os.path.join(DIR, celeb)
        label = celebs.index(celeb)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

print("Training Done ----------------------")

features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer of the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)
