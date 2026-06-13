import numpy as np
import cv2 as cv

img1 = cv.imread('materials\Resources\Photos\cats.jpg')
cv.imshow('cats', img1)
img2 = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('lady', img2)

#turn gray
gray1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow('gray cats',gray1)
cv.imshow('gray lady',gray2)

#blur images
blured1 = cv.GaussianBlur(gray1,(5,5),cv.BORDER_DEFAULT)
blured2 = cv.GaussianBlur(gray2,(5,5),cv.BORDER_DEFAULT)

#find edges
canny1 = cv.Canny(blured1,125,175)
canny2 = cv.Canny(blured2,125,175)
cv.imshow('canny1', canny1)
cv.imshow('canny 2', canny2)

#get contours
contours1, hierarchies1 = cv.findContours(canny1,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE )
contours2, hierarchies1 = cv.findContours(canny2,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE )

#draw contours
cv.drawContours(img1, contours1,-1,(0,0,255),thickness=2)
cv.drawContours(img2, contours2,-1,(0,0,255),thickness=2)
cv.putText(img1,f'{len(contours1)} contour(s) found',(10,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
cv.putText(img2,f'{len(contours2)} contour(s) found',(10,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)

#normalise pictures
img1_resized = cv.resize(img1,(500,500))
img2_resized = cv.resize(img2,(500,500))


#stack images
stacked = np.hstack([img1_resized, img2_resized])
cv.imshow('stacked images', stacked)


cv.waitKey(0)