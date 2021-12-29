import cv2 as cv

""" USE THIS TO RESCALE IMAGES, VIDEOS, AND LIVE VIDEOS """
# Function to change the size of Images, Videos, and Live Videos
def rescale_frame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Function to change the resolution of only Live Videos
def change_resolution(width, height):
    vid.set(3, width)
    vid.set(4, height)


# Reading and Resizing an Image
# img = cv.imread("imgs/cat.jpg")
# resized_img = rescale_frame(img)
# cv.imshow("Cat", img)
# cv.imshow("Cat Resized", resized_img)


# Reading and Resizing a Video
vid = cv.VideoCapture("imgs/dog.mp4")

while True:
    isTrue, frame = vid.read()

    frame_resized = rescale_frame(frame, scale=0.2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break

cv.waitKey(0)
