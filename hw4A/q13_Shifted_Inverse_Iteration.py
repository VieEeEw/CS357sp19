import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from math import sqrt

q = 1
LHS = A - q * np.identity(3)

P, L, U = la.lu(LHS)

y = la.solve_triangular(L, P.T @ x, lower=True)
x = la.solve_triangular(U, y)
x /= la.norm(x)
for i in range(500):
    pre = x
    y = la.solve_triangular(L, P.T @ pre, lower=True)
    x = la.solve_triangular(U, y)
    x /= la.norm(x)

eigenvalue = x.T @ A @ x / (x.T @ x)
eigenvector = x
