import numpy as np


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


def partition_stiffness_matrix(K, equation_numbers, nk):
    # construct the smaller matrices
    # pass
    KK = swap_rows_columns(K, equation_numbers)
    Kpp = KK[0: nk, 0:nk]
    Kpf = KK[0: nk, nk:]
    Kfp = KK[nk:, 0:nk]
    Kff = KK[nk:, nk:]
    return Kpp, Kpf, Kfp, Kff
