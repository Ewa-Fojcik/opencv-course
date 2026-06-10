import numpy as np
import matplotlib.pyplot as plt

N = 500
img = np.zeros((N,N,3))

for i in range(10):
    for j in range(10):
        if (i+j) % 2 == 0:
            img[i*50:i*50+50, j*50:j*50+50] = [1,1,1]
        else:
            img[i*50:i*50+50, j*50:j*50+50] = [0,0,0]

plt.imshow(img)
plt.show()