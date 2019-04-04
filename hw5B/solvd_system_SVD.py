import numpy as np

U = np.array([[1, 0, 0],
              [0, -1 / 2 ** 0.5, 1 / 2 ** 0.5],
              [0, 1 / 2 ** 0.5, 1 / 2 ** 0.5]])

sigma = np.diag([1 / 4, 1 / 6, 0])

vt = np.array([[-3 ** 0.5 / 2, 1 / 2, 0],
              [-1 / 2, -3 ** 0.5 / 2, 0],
              [0, 0, 1]])

b = np.array([8, 0, 0])
print(vt.T @ sigma @ U.T @ b)
