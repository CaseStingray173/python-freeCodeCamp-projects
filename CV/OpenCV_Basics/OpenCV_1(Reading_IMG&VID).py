import cv2 as cv

######
# Reading Images
# img = cv.imread("imgs/cat_large.jpg")

# The first parameter is the window name, and the second is the image itself
# cv.imshow("Cat Large", img)
######

######
# Reading Videos
# When using the VideoCapture you usually give a file name, but if you are using
# a web cam you would pass in an integer (And in most cases that number is 0)
video = cv.VideoCapture("imgs/dog.mp4")

# Inside a while loop we view the video frame by frame
while True:
    # The video.read() reads in the video frame by frame
    isTrue, frame = video.read()
    cv.imshow("Dog Video", frame)

    # To stop the video playing infinitely
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video pointer
video.relase()

# Destroy all windows
cv.destroyAllWindows()

# This is a keyboard binding function, when passed in a 0 it
# waits infinitely until a key is pressed
# cv.waitKey(0)
