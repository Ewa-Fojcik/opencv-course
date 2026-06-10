import numpy as np
import matplotlib.pyplot as plt

N = 400
img = np.zeros((N,N,3))

for i in range(0,N):
    img[i,:,1]=i/N
for j in range(0,N):
    img[:,j,0]=j/N


plt.imshow(img)
plt.show()
