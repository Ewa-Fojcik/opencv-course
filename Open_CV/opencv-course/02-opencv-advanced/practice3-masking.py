import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\cats 2.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

circle1 = cv.circle(blank.copy(),(img.shape[1]//2 - 145,img.shape[0]//2 - 65),100,255,-1)
circle2 = cv.circle(blank.copy(),(img.shape[1]//2 + 145,img.shape[0]//2 + 65),100,255,-1)

combigned_mask = cv.bitwise_or(circle1,circle2)
masked = cv.bitwise_and(img,img,mask=combigned_mask)
cv.imshow('masked',masked)



cv.waitKey(0)