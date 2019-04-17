import numpy as np

from typing import List

K = np.array([[20., 10., - 10., 0., - 10., - 10.],
              [10., 10., 0., 0., - 10., - 10.],
              [-10., 0., 20., - 10., - 10., 10.],
              [0., 0., - 10., 10., 10., - 10., ],
              [-10., - 10., - 10., 10., 20., 0.],
              [-10., - 10., 10., - 10., 0., 20.]])

equation_numbers = [1, 2, 4, 3, 5, 6]


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


print(swap_rows_columns(K, equation_numbers))
