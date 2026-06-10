import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((256,256,3), dtype=np.float32)

for i in range(256):
    R = i*0.0039
    G = 1-i*0.0039
    B = 1
    img[i, : ,0] = R
    img[i, : ,1] = G 
    img[i,:,2] = B

plt.imshow(img)
plt.show()