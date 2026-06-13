import cv2 as cv
import numpy as np

#original
img = cv.imread('materials\Resources\Photos\cat.jpg')
cv.imshow('cat', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

#blur
blured = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blured',blured)

#extract edges
canny = cv.Canny(blured,25,75)
cv.imshow('edges',canny)


gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
canny_bgr = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)

h, w = img.shape[:2]
img_small = cv.resize(img, (w//4, h//4))
gray_small = cv.resize(gray_bgr, (w//4, h//4))
blur_small = cv.resize(blured, (w//4, h//4))
canny_small = cv.resize(canny_bgr, (w//4, h//4))

stacked = np.hstack([img_small, gray_small, blur_small, canny_small])
cv.imshow('stacked', stacked)

cv.waitKey(0)