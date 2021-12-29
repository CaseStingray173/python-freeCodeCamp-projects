import cv2 as cv

cats = cv.imread("imgs/cats.jpg")
cv.imshow("Cats", cats)

gray = cv.cvtColor(cats, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# SIMPLE THRESHOLDING
# IN SIMPLE THRESHOLDING YOU GET TO DECIDE THE THRESHOLD VALUE BUT IT MIGHT
# NOT WORK ALL THE TIME
threshold, thresh_img = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh_img)

threshold, thresh_img_inverse = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_img_inverse)

# ADAPTIVE THRESHOLDING
# IN ADAPTIVE THRESHOLDING THE COMPUTER DECIDES THE THRESHOLD AUTOMATICALLY
adaptive_thresh_img = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("Adaptive Thresholding", adaptive_thresh_img)


cv.waitKey(0)
