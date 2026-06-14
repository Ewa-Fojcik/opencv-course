import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('materials\Resources\Photos\cats.jpg')
cv.imshow('cats',img)



while True:
    cv.imshow('cats',img)
    key = cv.waitKey(0) & 0xff
    colors = ('b', 'g', 'r')
    

    if key == ord('h'):
        cv.imshow('cats',img)
        plt.figure()
        plt.title('Histogram')
        plt.xlabel('Boxes')
        plt.ylabel('No. of pixels')
        for i, col in enumerate(colors):
            hist = cv.calcHist([img],[i],None,[256],[0,256])
            plt.plot(hist,color=col)
            plt.xlim([0,256])
        plt.show()

    elif key == ord('m'):
        plt.figure()
        plt.title('Histogram')
        plt.xlabel('Boxes')
        plt.ylabel('No. of pixels')
        blank = np.zeros(img.shape[:2],dtype='uint8')
        mask = cv.circle(blank,(img.shape[0]//2,img.shape[1]//2),150,255,-1)
        masked = cv.bitwise_and(img,img,mask=mask)
        cv.imshow('masked',masked)

        for i,col in enumerate(colors):
            hist1 = cv.calcHist([masked],[i],mask,[256],[0,256])
            plt.plot(hist1,color = col)
            plt.xlim([0,256])
        plt.show()
        
    elif key == ord('d'):
        break



cv.waitKey(0)