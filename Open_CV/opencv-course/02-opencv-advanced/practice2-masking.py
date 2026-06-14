import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\cats 2.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
pts = np.array([[200,50],[50,350],[350,350]])
triangle_mask = cv.fillPoly(blank,[pts],255)

masked = cv.bitwise_and(img,img,mask=triangle_mask)
cv.imshow('masked',masked)



cv.waitKey(0)