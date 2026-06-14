import cv2 as cv
import numpy as np


img = cv.imread('materials\Resources\Photos\cats 2.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank',blank)

# mask = cv.circle(blank,(img.shape[1]//2 + 45, img.shape[0]//2),100,255,-1)
# cv.imshow('mask',mask)

circle = cv.circle(blank.copy(),(img.shape[1]//2 + 45, img.shape[0]//2),100,255,-1)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('weird shape',weird_shape)



masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('masked image', masked)




cv.waitKey(0)