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
    swaped = set()
    for i, j in enumerate(equation_numbers, 1):
        if i != equation_numbers[i - 1] and j not in swaped:
            origin = np.copy(K[i - 1])
            after = np.copy([K[j - 1]])
            K[i - 1] = after
            K[j - 1] = origin
            swaped.add(i)
            # swaped.add(j)

    swaped.clear()
    for i, j in enumerate(equation_numbers, 1):
        if i != equation_numbers[i - 1] and j not in swaped:
            origin = np.copy(K[:, i - 1])
            after = np.copy([K[:, j - 1]])
            K[:, i - 1] = after
            K[:, j - 1] = origin
            swaped.add(i)
            # swaped.add(j)

    return K


print(swap_rows_columns(K, equation_numbers))
