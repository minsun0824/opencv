import cv2 as cv
import sys

# img = cv.imread('C:/Users/sunny/opencv/opencv/opencv-practice/Photos/cat_large.jpg')
# if img is None:
#     print('Image load failed')
#     sys.exit()
# cv.imshow('Cat',img)

capture = cv.VideoCapture('C:/Users/sunny/opencv/opencv/opencv-practice/Videos/dog.mp4')
if capture is None:
    print('Image load failed')
    sys.exit()
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
cv.waitKey(0)
cv.destroyAllWindows()