import numpy as np
import matplotlib.pyplot as plt

shape_size = 600 * 482
image = np.random.random(size=shape_size)
image = image.reshape((600, 482))
f = 0.6106976905893376

u,sigma,vt = np.linalg.svd(image,full_matrices=False)
plt.plot(sigma[:50])
plt.ylabel("sigmas")
plt.title("sigmas")
plt.show()
total = sum(sigma)
# print(sigma[:50])