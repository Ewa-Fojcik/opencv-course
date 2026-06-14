import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('materials\Resources\Photos\cats.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',masked)

plt.figure()
plt.title('Histograms')
plt.xlabel('boxes')
plt.ylabel('No. of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    histogram1 = cv.calcHist([img],[i],None,[256],[0,256])
    histogram2 = cv.calcHist([img],[i],circle,[256],[0,256])

    plt.subplot(1,2,1)
    plt.plot(histogram1,color=col)
    plt.xlim([0,256])

    plt.subplot(1,2,2)
    plt.plot(histogram2,color=col)
    plt.xlim([0,256])
    
plt.show()


cv.waitKey(0)