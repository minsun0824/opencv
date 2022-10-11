import cv2 as cv
import sys
import numpy as np
from function import*

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Black',blank)

img = cv.imread('C:/Users/sunny/opencv/opencv/opencv-practice/Photos/cat.jpg')
if img is None:
    print('Image load failed')
    sys.exit()
#cv.imshow('Cat',img)

#1. paint the image a certain color
blank[100:250,50:70] = 0,255,255
cv.imshow('Green',blank)

#2. draw a rectangle
cv.rectangle(blank,(50,0),(blank.shape[1]//2,blank.shape[2]//2),(100,255,100),thickness=cv.FILLED)
cv.imshow("Rectangle",blank)

#3. draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

#4. draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=3)
cv.imshow('Line',blank)

#5. write text
cv.putText(blank,'Hello',(250,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)