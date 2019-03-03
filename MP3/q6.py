import numpy as np


def my_lu(A):
    # The upper triangular matrix U is saved in the upper part of the matrix M (including the diagonal)
    # The lower triangular matrix L is saved in the lower part of the matrix M (not including the diagonal)
    # Do NOT use `scipy.linalg.lu`!
    # You should not use pivoting

    M = ...
    return M


def my_triangular_solve(M, b):
    # A = LU (L and U are stored in M)
    # A x = b (given A and b, find x)
    # M is a 2D numpy array
    # The upper triangular matrix U is stored in the upper part of the matrix M (including the diagonal)
    # The lower triangular matrix L is stored in the lower part of the matrix M (not including the diagonal)
    # b is a 1D numpy array
    # x is a 1D numpy array
    # Do not use `scipy.linalg.solve_triangular`

    x = ...

    return x


def fea_solve(Kpp, Kpf, Kfp, Kff, xp, Ff):
    # Use my_lu and my_triangular_solve

    xf = ...
    Fp = ...
    return xf, Fp