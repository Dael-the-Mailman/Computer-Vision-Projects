import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works with photos, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only works with live videos
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', rescaleFrame(img, scale=.25))

cv.waitKey(0)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()