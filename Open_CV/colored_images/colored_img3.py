import numpy as np
import matplotlib.pyplot as plt

N = 400
img = np.zeros((N,N,3))

img[:,:,:] = 0.0
img[50:350,50:350,:]=1
img[195:205,50:350]=[1,0,0]
img[50:350,195:205]=[1,0,0]


plt.imshow(img)
plt.show()
