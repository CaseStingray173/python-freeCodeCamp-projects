import cv2 as cv
import numpy as np

cat = cv.imread("imgs/cat.jpg")

cv.imshow("Cat", cat)

# Translation
# def translate(img, x, y):
#     trans_mat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, trans_mat, dimensions)


# If x < 0 the image gets translated to left
# If y < 0 the image gets translated to up
# If x > 0 the image gets translated to right
# If y > 0 the image gets translated to down

# translated_image = translate(cat, -100, 100)
# cv.imshow("Translated", translated_image)

# Rotation
# def rotate(img, angle, rot_point=None):
#     (height, width) = img.shape[:2]
#
#     if rot_point is None:
#         rot_point = (width//2, height//2)
#
#     rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
#     dimensions = (width, height)
#
#     return cv.warpAffine(img, rot_mat, dimensions)


# rotated_image = rotate(cat, -45)
# cv.imshow("Rotated", rotated_image)

# rotated_image_2 = rotate(rotated_image, -90)
# cv.imshow("Rotated twice", rotated_image_2)


# Resizing
# resized_image = cv.resize(cat, (500, 500), cv.INTER_CUBIC)
# cv.imshow("Resized image", resized_image)


# Flipping
# flip() takes an image, and 0, 1 or -1
# 0 is for flipping the image vertically (over the X-axis)
# 1 is for flipping the image horizontally (over the Y-axis)
# -1 is for flipping the image both horizontally and vertically
flip_image = cv.flip(cat, -1)
cv.imshow("Flipped Image", flip_image)


# Cropping
cropped_image = cat[200:400, 300:400]
cv.imshow("Cropped Image", cropped_image)


cv.waitKey(0)
