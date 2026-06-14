import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('Lady',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel gradient magnitude reprezentation
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combigned_sobel = cv.bitwise_or(sobelx,sobely)

#canny
canny = cv.Canny(gray,125,175)
cv.imshow('canny',canny)

cv.imshow('sobel x',sobelx)
cv.imshow('sobel y',sobely)
cv.imshow('combigned sobel',combigned_sobel)

cv.waitKey(0)