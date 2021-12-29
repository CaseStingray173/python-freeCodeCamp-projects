import cv2 as cv
import numpy as np

cats = cv.imread("imgs/cats 2.jpg")
cv.imshow("Cats", cats)

blank = np.zeros(cats.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

circle = cv.circle(blank.copy(), (cats.shape[1] // 2 + 45, cats.shape[0] // 2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)
masked = cv.bitwise_and(cats, cats, mask=weird_shape)
cv.imshow("Masked Image", masked)

cv.waitKey(0)
