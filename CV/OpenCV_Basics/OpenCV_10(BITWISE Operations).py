import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# BITWISE AND
# bitwise_and() takes two images and places them on each other
# and returns the intersection of those two images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("BITWISE AND", bitwise_and)

# BITWISE OR
# bitwise_or() returns a union of both images
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BITWISE OR", bitwise_or)

# BITWISE XOR
# bitwise_xor() returns opposite to what bitwise_and() returns
# it returns the parts that are not common in both images
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BITWISE XOR", bitwise_xor)

# BITWISE NOT
# bitwise_not() only takes one image and flips the binary color (white to black)
bitwise_not = cv.bitwise_not(circle)
cv.imshow("BITWISE NOT", bitwise_not)

cv.waitKey(0)
