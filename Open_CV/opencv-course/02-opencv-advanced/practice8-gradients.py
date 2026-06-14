import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('Lady',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Canny
blur = cv.GaussianBlur(gray,(3,3),0)
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#Sobel
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
combigned_sobel = cv.bitwise_or(sobel_x,sobel_y)
combigned_sobel = np.uint8(np.absolute(combigned_sobel))
cv.imshow('combigned sobel',combigned_sobel)

#Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

#cvt color
canny_bgr = cv.cvtColor(canny,cv.COLOR_GRAY2BGR)
combigned_sobel_bgr = cv.cvtColor(combigned_sobel,cv.COLOR_GRAY2BGR)
lap_bgr = cv.cvtColor(lap,cv.COLOR_GRAY2BGR)

#resize
size = (300,300)
img_r = cv.resize(img,size)
canny_r = cv.resize(canny_bgr,size)
combigned_sobel_r = cv.resize(combigned_sobel_bgr,size)
lap_r = cv.resize(lap_bgr,size)

#stack
stacked = np.hstack([img_r,canny_r,combigned_sobel_r,lap_r])
cv.imshow('stacked',stacked)

cv.waitKey(0)