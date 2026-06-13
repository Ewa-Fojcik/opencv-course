import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('Lady',img)

#translation
def translate(img, x, y):
    transMAT = np.float32([[1,0,x],[0,1,y]])
    dimetions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMAT, dimetions)

translated = translate(img, -100,100)
cv.imshow('translated', translated)

#rotation
def rotate(img,angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMAT = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimentions = (width, height)
     
    return cv.warpAffine(img, rotMAT, dimentions)

rotated = rotate(img, -45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('rotated rotated', rotated_rotated)

#resize image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#flipping
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

#cropping
cropped = img[200:400,300:400]
cv.imshow('cropped',cropped)


cv.waitKey(0)