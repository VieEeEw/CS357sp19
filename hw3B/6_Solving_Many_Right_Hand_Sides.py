from scipy import linalg as la
import scipy
import numpy as np

def solve_multiple_systems_v1(A, b):
    n = len(b)
    res = []
    for i in range(n):
        xi = scipy.linalg.solve(A, b[i])
        res.append(xi)
    return res

def solve_multiple_systems_v2(A, b):
    n = len(b)
    lu_piv = scipy.linalg.lu_factor(A)
    res = []
    for i in range(n):
        xi = scipy.linalg.lu_solve(lu_piv, b[i])
        res.append(xi)
    return res

