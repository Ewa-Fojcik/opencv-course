import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\cats.jpg')
cv.imshow('cats org', img)

#turn gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

#blur grayscale img
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blured',blur)

#get the edges
canny = cv.Canny(blur,125,175)
cv.imshow('edges',canny)

#get contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

#draw contours
cv.drawContours(img,contours,-1,(0,0,255),thickness=2)
cv.putText(img,f'{len(contours)} contours(s) found',(10,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2)
cv.imshow('drawn contours', img)


cv.waitKey(0)