import numpy as np
import cv2 as cv

img = cv.imread('materials\Resources\Photos\cat.jpg')
cv.imshow('cat',img)

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None: 
        rotPoint=(width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimentions = (width,height)

    return cv.warpAffine(img,rotMat,dimentions)


angle = 0
while True:
    angle += 5
    rotated = rotate(img,angle)
    cv.putText(rotated,str(angle), (300,40),cv.FONT_HERSHEY_PLAIN,1.0,(255,255,255),thickness=2)
    cv.imshow('rotated pic',rotated)

    if cv.waitKey(50) & 0xff==ord('d'):
        break

cv.destroyAllWindows()


