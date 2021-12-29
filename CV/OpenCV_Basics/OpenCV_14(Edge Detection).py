import cv2 as cv
import numpy as np

park = cv.imread("imgs/park.jpg")
cv.imshow("Cats", park)

gray = cv.cvtColor(park, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian Edge
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian", lap)

# Sobel Edge
sobelx = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 1, 0)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel Combined", combined_sobel)

# Canny Edge
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)
