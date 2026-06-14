import cv2 as cv
import numpy as np

img = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('orginal',img)

while True:
    key = cv.waitKey(0) & 0xFF
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(img,(3,3),0)
    canny = cv.Canny(blur,125,175)

    if key == ord('g'):
        cv.imshow('gray',gray)
    elif key == ord('b'):
        cv.imshow('blur',blur)
    elif key == ord('e'):
        cv.imshow('canny',canny)
    elif key == ord('t'):
        threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
        cv.imshow('threshold',thresh)
    elif key == ord('c'):
        contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        result = img.copy()
        cv.drawContours(result,contours,-1,(0,0,255),2)
        cv.imshow('contours',result)
    elif key == ord('m'):
        blank = np.zeros(img.shape[:2],dtype='uint8')
        cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
        masked = cv.bitwise_and(img,img,mask=blank)
        cv.imshow('masked',masked)
    elif key == ord('s'):
        sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
        sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
        combigned_sobel = cv.bitwise_or(sobel_x,sobel_y)
        combigned_sobel = np.uint8(np.absolute(combigned_sobel))
        cv.imshow('sobel',combigned_sobel)
    elif key == ord('o'):
        cv.imshow('original',img)
    elif key == ord('d'):
        break

