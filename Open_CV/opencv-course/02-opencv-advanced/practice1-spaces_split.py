import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\lady.jpg')

blank = np.zeros(img.shape[:2],dtype='uint8')

#org BGR
cv.imshow('lady', img)

#HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#separate colors
b,g,r = cv.split(img)

red = cv.merge([blank,blank,r])
blue = cv.merge([b,blank,blank])

cv.imshow('red',red)
cv.imshow('blue',blue)

size = (300,300)
img_r = cv.resize(img,size)
hsv_r = cv.resize(hsv,size)
red_r = cv.resize(red, size)
blue_r = cv.resize(blue, size)

stacked = np.hstack([img_r,hsv_r,red_r,blue_r])
cv.imshow('stacked', stacked)


cv.waitKey(0)

