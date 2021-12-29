import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cats = cv.imread("imgs/cats.jpg")
cv.imshow("Cats", cats)

blank = np.zeros(cats.shape[:2], dtype="uint8")

########
# FOR GRAY SCALE HISTOGRAM COMPUTATION
# gray = cv.cvtColor(cats, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Scale Image", gray)
########

mask = cv.circle(blank, (cats.shape[1] // 2, cats.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(cats, cats, mask=mask)
cv.imshow("Masked Image", masked)

########
# Gray Scale Histogram Computation
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
#
# Plotting the Gray Scale Histogram
# plt.figure()
# plt.title("Gray Scale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()
########

# Color Histogram Computation
plt.figure()
plt.title("Color Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([cats], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
