import cv2 as cv

img = cv.imread('materials\Resources\Photos\cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)