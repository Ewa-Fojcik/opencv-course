import numpy as np
import matplotlib.pyplot as plt

N = 400
img = np.zeros((N,N,3))

for i in range(N):
    for j in range(N):
        distance = np.sqrt((i-200)**2+(j-200)**2)
        t = distance/150
        if t <= 1:
            img[i,j,0] = 1-t
            img[i,j,1] = 0
            img[i,j,2] = t

plt.imshow(img)
plt.show()