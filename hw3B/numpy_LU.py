from scipy import linalg as la
import numpy as np

a = np.array([[1, 6],
              [2, 7]])

matrix = la.lu(a)
for m in matrix:
    print(m)
