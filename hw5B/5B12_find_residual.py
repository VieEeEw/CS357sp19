import numpy as np
from numpy import linalg as la

U = np.array([[0, 1, 0, 0],
              [1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0]])

sigma = np.array([[12, 0, 0],
                  [0, 11, 0],
                  [0, 0, 0],
                  [0, 0, 0]])

pseudo_sigma = np.array([[1 / 12, 0, 0],
                         [0, 1 / 11, 0],
                         [0, 0, 0],
                         [0, 0, 0]])

vt = np.array([[2 ** -0.5, 2 ** -0.5, 0],
               [2 ** -0.5, -2 ** -0.5, 0],
               [0, 0, 1]])

b = np.array([11,7,2,9])
x = vt.T @ pseudo_sigma.T @ U.T @ b
A = U @ sigma @ vt

print(la.norm(b - A @ x))
