import numpy as np
import matplotlib.pyplot as plt

N=300
img = np.ones((N,N,3))

for i in range(N): 
    for j in range(N):
        distance = np.sqrt((i-150)**2 + (j-150)**2)
        ring = int(distance/30)
        if ring%2==0:
            img[i,j] = [1,1,1]
        else:
            img[i,j] = [0,0,0]

plt.imshow(img)
plt.show()