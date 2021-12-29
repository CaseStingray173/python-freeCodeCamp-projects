import cv2 as cv

cats = cv.imread("imgs/cats.jpg")

cv.imshow("Cats", cats)

# This is the first method of blurring
# Average Blur
# (3, 3) is the the kernel/matrix size. The more the kernel
# size the more the image becomes blurry
average = cv.blur(cats, (3, 3))
cv.imshow("Average Blur", average)

# This is the second method of blurring
# Gaussian Blur
gauss = cv.GaussianBlur(cats, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# This is the third method of blurring
# Median Blur
median = cv.medianBlur(cats, 3)
cv.imshow("Median Blur", median)

# This is the fourth method of blurring
# Bilateral Blur
bilateral = cv.bilateralFilter(cats, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)