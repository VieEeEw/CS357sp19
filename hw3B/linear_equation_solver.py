from numpy import linalg as la
import numpy as np

a = np.array([[2, 1, 0],
              [0, 1, 0],
              [3, 0, 3]])
b = np.array([38, 14, 51]).reshape(3, 1)
d = la.det(a)
print(d)
print(la.solve(a, b))
