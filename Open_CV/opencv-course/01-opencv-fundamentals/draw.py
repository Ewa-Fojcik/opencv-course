import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
#img = cv.imread('materials\Resources\Photos\cat.jpg')
#cv.imshow('Cat', img)

#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

cv.rectangle(blank,(0,0),(blank.shape[1]//3, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
cv.imshow('circle', blank)

cv.line(blank,(100,250),(200,400), (255,255,255), thickness=2)
cv.imshow('line', blank)

cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)