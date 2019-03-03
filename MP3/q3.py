import numpy as np


def swap_rows_columns(K: np.ndarray, equation_numbers: np.ndarray) -> np.ndarray:
    # construct the matrix Khat
    P = np.zeros(K.shape)
    
    for i, j in enumerate(equation_numbers):
        P[i, j - 1] = 1

    return np.matmul(P, K)
