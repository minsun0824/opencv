import cv2 as cv



img = cv.imread('C:/Users/sunny/opencv/opencv/opencv-practice/Photos/cat.jpg')
cv.imshow('Cat',img)

# 1. grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2. blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# 3. edge cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny',canny)

# 4. dilating the image
dilated = cv.dilate(canny, (7,7), iterations= 3)
cv.imshow('Dilated',dilated)

# 5. eroding
eroded = cv.erode(dilated, (3,3), iterations= 3)
cv.imshow('Eroded', eroded)

# 6. resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# 7. cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)