import cv2 as cv
import numpy as np

park = cv.imread("imgs/park.jpg")
cv.imshow("Park", park)

blank = np.zeros(park.shape[:2], dtype="uint8")

b, g, r = cv.split(park)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(park.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge_img = cv.merge([b, g, r])
cv.imshow("Merged Image", merge_img)

cv.waitKey(0)


