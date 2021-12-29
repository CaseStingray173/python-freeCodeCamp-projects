import cv2 as cv

img = cv.imread("imgs/cat.jpg")

cv.imshow("Cat", img)

# This converts an image from BGR to GRAY scale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray_img)

# This is how we blur an image
# (7,7) decides how blurry the image becomes, the bigger
# the number the more blurry the image becomes
blur_image = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blurred Image", blur_image)

# This is how you create an Edge Cascade
canny_image = cv.Canny(img, 125 ,175)
cv.imshow("Canny Edges", canny_image)

# This is how you dilate an image
dilate_image = cv.dilate(canny_image, (3,3), 3)
cv.imshow("Dilated Image", dilate_image)

# This is how you do Eroding
erode_image = cv.erode(dilate_image, (3, 3), 3)
cv.imshow("Eroded Image", erode_image)

# This is how you resize images
resize_image = cv.resize(img, (500, 500), cv.INTER_CUBIC)
cv.imshow("Resized Image", resize_image)

# This is how you crop images
crop_image = img[50:200, 200:400]
cv.imshow("Cropped Image", crop_image)

cv.waitKey(0)
