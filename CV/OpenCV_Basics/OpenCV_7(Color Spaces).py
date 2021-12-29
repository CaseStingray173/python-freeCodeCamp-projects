import cv2 as cv

# Reading an image
park = cv.imread("imgs/park.jpg")
# Displaying the image
cv.imshow("Park Image", park)

# This will use the matplotlib to display the image with inverted colors
# RGB from BGR
# plt.imshow(park)
# plt.show()

# Converting from BGR to GRAY SCALE
gray_img = cv.cvtColor(park, cv.COLOR_BGR2GRAY)
# Displaying the gray image
cv.imshow("Gray Scale Image", gray_img)
# Converting from BGR to HSV
hsv_img = cv.cvtColor(park, cv.COLOR_BGR2HSV)
# Displaying the hue saturation value
cv.imshow("Hue Saturation Image", hsv_img)

# Converting BGR to LAB(L*A*B)
lab_img = cv.cvtColor(park, cv.COLOR_BGR2LAB)
# Displaying the LAB image
cv.imshow("LAB Image", lab_img)

# Converting BGR to HLS
hls_img = cv.cvtColor(park, cv.COLOR_BGR2HLS)
# Displaying the HLS image
cv.imshow("HLS Image", hls_img)

# Converting BGR to RGB
rgb_img = cv.cvtColor(park, cv.COLOR_BGR2RGB)
# Displaying the RGB image
cv.imshow("RGB Image", rgb_img)

cv.waitKey(0)
