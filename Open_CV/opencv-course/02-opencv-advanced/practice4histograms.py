import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('materials\Resources\Photos\cats.jpg')
img2 = cv.imread('materials\Resources\Photos\lady.jpg')
cv.imshow('Cats', img1)
cv.imshow('Lady',img2)

plt.figure()
plt.title('colored histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist1 = cv.calcHist([img1],[i],None,[256],[0,256])
    hist2 = cv.calcHist([img2],[i],None,[256],[0,256])

    plt.subplot(1,2,1)
    plt.plot(hist1,col)
    plt.xlim([0,256])

    plt.subplot(1,2,2)
    plt.plot(hist2,col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)