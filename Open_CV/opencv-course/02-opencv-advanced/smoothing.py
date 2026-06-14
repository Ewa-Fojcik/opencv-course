import cv2 as cv

img = cv.imread('materials\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

#Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average blur',average)

#Guassian blur
guassian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Guassian', guassian)

#Median blur
median = cv.medianBlur(img,3)
cv.imshow('Median blur', median)

#Bilateral blur
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)