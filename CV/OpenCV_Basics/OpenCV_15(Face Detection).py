import cv2 as cv

img = cv.imread("imgs/group 1.jpg")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

face_rectangle = haar_cascade.detectMultiScale(gray, 1.1, 1)

print(f'Number of faces found = {len(face_rectangle)}')

for (x, y, w, h) in face_rectangle:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Detected Face", img)

cv.waitKey(0)
