import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from math import sqrt

eigenval1 = []
eigenval2 = []
eigenvec1 = []
eigenvec2 = []
cnt = []
ratios = []
for A in As:
    count = 0.0
    x = x_0
    while True:
        pre = x
        x = A @ x
        x /= la.norm(x)
        count += 1
        if la.norm(x - pre) < 10 ** -12:
            break


    eigenvec1.append(x)
    e = x.T @ A @ x / (x.T @ x)
    eigenval1.append(e)
    cnt.append(count)

    P, L, U = la.lu(A)
    y = la.solve_triangular(L, P.T @ pre, lower=True)
    x = la.solve_triangular(U, y)
    x /= la.norm(x)
    while True:
        pre = x
        y = la.solve_triangular(L, P.T @ pre, lower=True)
        x = la.solve_triangular(U, y)
        x /= la.norm(x)
        if la.norm(x - pre) < 10 ** -12:
            break

    e = x.T @ A @ x / (x.T @ x)
    eigenvec2.append(x)
    eigenval2.append(e)

eigenval1 = np.array(eigenval1)
eigenval2 = np.array(eigenval2)
eigenvec1 = np.array(eigenvec1)
eigenvec2 = np.array(eigenvec2)
cnt = np.array(cnt)
for lam1, lam2 in zip(eigenval1, eigenval2):
    ratios.append(lam2 / lam1)
ratios = np.array(ratios)

plt.plot(cnt,ratios)
plt.xlabel("cnt")
plt.ylabel("ratio")
plt.title("ratio VS CNT")