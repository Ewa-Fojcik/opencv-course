import numpy as np
import cv2 as cv

#load cat img
img = cv.imread('materials\Resources\Photos\cat.jpg')
print(img.shape)
cv.imshow('cat',img)

#drawred rectangle around cats head, type text, draw green text in the middle
cv.rectangle(img,(300,50),(620,350),(0,0,255),thickness=2)
cv.putText(img,'Cat detected',(300,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,1.0,(255,255,255),thickness=2)
cv.circle(img,(img.shape[1]//2, img.shape[0]//2),40,(0,255,0),thickness=2)
cv.imshow('cat',img)

cv.waitKey(0)