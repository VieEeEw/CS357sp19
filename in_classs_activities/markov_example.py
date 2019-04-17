import numpy as np
import scipy

matrix = [[0.6, 0.4, 0.2, 0.3],
          [0.2, 0.5, 0.1, 0.2],
          [0.15, 0.1, 0.7, 0.0],
          [0.05, 0.0, 0.0, 0.5]]
A = np.array(matrix)

activity_name = ["lecture","","",""]

x0 = np.array([0.8,0.1,0.0,0.1])
x1 = A@x0
print("x1 = ", x1)

x = np.array([0.8,0.1,0.0,0.1])
for i in range(5):
    x = A@x
    print("x = ",x)