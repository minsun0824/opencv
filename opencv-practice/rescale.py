import cv2 as cv
import sys

img = cv.imread('C:/Users/sunny/opencv/opencv/opencv-practice/Photos/cat.jpg')
if img is None:
    print('Image load failed')
    sys.exit()
cv.imshow('Cat',img)

def rescaleFrame(frame,scale = 0.75):
    #every
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #live video only
    capture.set(3,width)
    capture.set(4,width)


resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)

#video
capture = cv.VideoCapture('C:/Users/sunny/opencv/opencv/opencv-practice/Videos/dog.mp4')
if capture is None:
    print('Image load failed')
    sys.exit()
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
cv.waitKey(0)
cv.destroyAllWindows()
