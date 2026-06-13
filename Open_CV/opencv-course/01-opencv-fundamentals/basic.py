import cv2 as cv

img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('lady', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny = cv.Canny(blur,25,75)
cv.imshow('edges',canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated image', dilated)

#Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded img', eroded)

#Resize image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)