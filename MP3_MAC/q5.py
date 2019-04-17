import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

K = np.array([[20., 10., - 10., 0., - 10., - 10.],
              [10., 10., 0., 0., - 10., - 10.],
              [-10., 0., 20., - 10., - 10., 10.],
              [0., 0., - 10., 10., 10., - 10., ],
              [-10., - 10., - 10., 10., 20., 0.],
              [-10., - 10., 10., - 10., 0., 20.]])

equation_numbers = [1, 2, 4, 3, 5, 6]
nk = 3


def fea_solve(Kpp, Kpf, Kfp, Kff, xp, Ff):
    # do stuff here
    RHS1 = Ff - np.matmul(Kfp, xp)
    xf = la.solve(Kff, RHS1)
    Fp = np.matmul(Kpp, xp) + np.matmul(Kpf, xf)
    return xf, Fp


def partition_stiffness_matrix(K, equation_numbers, nk):
    # construct the smaller matrices
    # pass
    KK = swap_rows_columns(K, equation_numbers)
    Kpp = KK[0: nk, 0:nk]
    Kpf = KK[0: nk, nk:]
    Kfp = KK[nk:, 0:nk]
    Kff = KK[nk:, nk:]
    return Kpp, Kpf, Kfp, Kff


def swap_rows_columns(K: np.ndarray, equation_numbers: np.ndarray) -> np.ndarray:
    # construct the matrix Khat
    temp = np.zeros(K.shape)
    for i, j in enumerate(equation_numbers, 1):
        temp[i - 1] = K[j - 1]

    temp2 = np.copy(temp.T)
    for i, j in enumerate(equation_numbers, 1):
        temp2[i - 1] = temp.T[j - 1]

    temp2 = temp2.T
    return temp2


Kpp, Kpf, Kfp, Kff = partition_stiffness_matrix(K, equation_numbers, nk)
xp = np.array([0, 0, 0])
Ff = np.array([0, 0, -10])
xf, Fp = fea_solve(Kpp, Kpf, Kfp, Kff, xp, Ff)
