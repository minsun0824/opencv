import cv2 as cv
import sys
import numpy as np
from function import*

blank = np.zeros((500,500),dtype='uint8')
cv.imshow('Black',blank)

img = cv.imread('C:/Users/sunny/opencv/opencv/opencv-practice/Photos/cat.jpg')
if img is None:
    print('Image load failed')
    sys.exit()
cv.imshow('Cat',img)
cv.waitKey(0)