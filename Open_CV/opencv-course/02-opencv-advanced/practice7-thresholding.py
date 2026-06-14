import cv2 as cv
import numpy as np

#org
img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('Lady',img)

#canny
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(3,3),0)
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#threshold
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresholded',thresh)

#cvt to bgr
canny_bgr = cv.cvtColor(canny,cv.COLOR_GRAY2BGR)
thresh_bgr = cv.cvtColor(thresh,cv.COLOR_GRAY2BGR)

#resize
size = (300,300)
canny_r = cv.resize(canny_bgr, size)
img_r = cv.resize(img, size)
thresh_r = cv.resize(thresh_bgr, size)


#stack
stacked = np.hstack([img_r,canny_r,thresh_r])
cv.imshow('stacked',stacked)

cv.waitKey(0)