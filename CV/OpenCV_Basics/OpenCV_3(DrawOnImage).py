import cv2 as cv
import numpy as np

# There are two ways you can draw on images:
# Draw on an existing image like "cat.jpg"
# or draw on blank frame (or a blank image)

# Creating a blank frame of height: 500, width: 500
# color channel: 3
blank_frame = np.zeros((500, 500, 3), dtype="uint8")

# Displaying a blank frame with default color(Black)
# cv.imshow("Blank", blank_frame)

# Setting the frame's color
# if you keep blank_frame[:], it will paint all the pixels
# if you specify like blank_frame[200:300, 300:400] it will only
# color specified pixels
# blank_frame[200:300, 300:400] = 0, 0, 255
# cv.imshow("Green Colored", blank_frame)


# ### Draw a rectangle ###

# rectangle() takes an image to draw the rectangle over
# thickness does multiple things: first it sets the thickness of the border
# when an integer > 0 is given, when -1 or thickness=cv.FILLED is used
# it paints the rectangle created with the color of the borders

# cv.rectangle(blank_frame, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
# Instead of giving the rectangle fixed dimensions like (250,500) (or if we want
# to use a midpoint of the image) we can do this :
# cv.rectangle(blank_frame, (0, 0), (blank_frame.shape[1]//2, blank_frame.shape[0]//2), (0, 255, 0), thickness=-1)

# cv.imshow("Rectangle", blank_frame)

# ### Draw a circle ###

# circle() is used to draw a circle on a blank image or frame.
# it takes an image, a midpoint, radius, and border thickness)
# cv.circle(blank_frame, (blank_frame.shape[1]//2, blank_frame.shape[0]//2), 40, (0, 0, 255), thickness=-1)
# cv.imshow("Circle", blank_frame)

# ### Draw a line ###

# line() draws line on an image
# cv.line(blank_frame, (100, 250), (300, 400), (255, 255, 255), thickness=2)
# cv.imshow("Line", blank_frame)

# ### Write text ###

# putText() write text on image. It takes an image, the text,
# its starting location, font, text scale, and thickness
cv.putText(blank_frame, "Hello World!!!", (125, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank_frame)

cv.waitKey(0)
