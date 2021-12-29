import cv2 as cv
import numpy as np

# Reading in an image
cats = cv.imread("imgs/cats.jpg")

# Displaying the image
cv.imshow("Cats", cats)

blank_img = np.zeros(cats.shape, dtype='uint8')
cv.imshow("Blank Image", blank_img)

# Converting the color(BGR) image to gray scale image
gray_img = cv.cvtColor(cats, cv.COLOR_BGR2GRAY)

# Displaying the gray scale image
cv.imshow("Gray Cats", gray_img)

# Blurring the image
blur_image = cv.GaussianBlur(gray_img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blurred image", blur_image)

# Getting the edges of the gray scale image using Canny
canny_image = cv.Canny(blur_image, 125, 175)

# Displaying the canny image
cv.imshow("Canny Image", canny_image)


# We can use threshold instead of using Canny to find the contour of images
# threshold() takes in a gray scale image, a min threshold, a max threshold and
# a threshold type
# threshold() looks at an image and binarizes the image
# ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
# # Displaying the thresh image
# cv.imshow("Thresh Image", thresh)

# Getting the contours of the image
# findContours() take in an image(gray scale and edges),
# a mode in which to find the contour (RETR_TREE for all
# hierarchical contours, RETR_EXTERNAL, for all the external contours,
# and RETR_LIST for all contours), and contour approximation method


# Using canny_image for finding contours
# contours, hierarchies = cv.findContours(canny_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Using thresh for finding contours
contours, hierarchies = cv.findContours(canny_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours(s) found!')

# Drawing contours on the blank image
cv.drawContours(blank_img, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank_img)

cv.waitKey(0)
