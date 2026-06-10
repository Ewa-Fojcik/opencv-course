import numpy as np
import matplotlib.pyplot as plt

N = 200
img = np.zeros((N,N,3))

img[100,100,:] = [1,1,0]

plt.imshow(img)
plt.show()