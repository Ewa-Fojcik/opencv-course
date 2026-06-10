import numpy as np
import matplotlib.pyplot as plt

N = 300
img = np.zeros((N,N,3))

img[ : ,0:149,0] = 1
img[ : ,150:300,2] = 1
img[ 150 ,: , :] = 1.0

plt.imshow(img)
plt.show()