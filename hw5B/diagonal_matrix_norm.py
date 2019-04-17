import numpy as np
import scipy.linalg as la

# A = np.diag([0.1,0.8,9.0,2.1])
# print(A)
# print(la.norm(A))
# print(8 / la.norm(A))
A = np.array([[1,7],
              [-6,-42],
              [-5,-35],
              [7,49],
              [2,14]])
u,s,v= la.svd(A)
print(u)
print(s)
print(v)
# print(A @ A.T)