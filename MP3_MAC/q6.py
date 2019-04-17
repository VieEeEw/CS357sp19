import numpy as np

K = np.array([[20., 10., - 10., 0., - 10., - 10.],
              [10., 10., 0., 0., - 10., - 10.],
              [-10., 0., 20., - 10., - 10., 10.],
              [0., 0., - 10., 10., 10., - 10., ],
              [-10., - 10., - 10., 10., 20., 0.],
              [-10., - 10., 10., - 10., 0., 20.]])

equation_numbers = [1, 2, 4, 3, 5, 6]

def my_lu(A: np.ndarray) -> np.ndarray:
    # The upper triangular matrix U is saved in the upper part of the matrix M (including the diagonal)
    # The lower triangular matrix L is saved in the lower part of the matrix M (not including the diagonal)
    # Do NOT use `scipy.linalg.lu`!
    # You should not use pivoting

    n = len(A)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                temp = A[i, k] / A[k, k]
                A[i, k + 1:n] = A[i, k + 1:n] - temp * A[k, k + 1:n]
                A[i, k] = temp
    return A


def my_triangular_solve(M: np.ndarray, b: np.ndarray) -> np.ndarray:
    # A = LU (L and U are stored in M)
    # A x = b (given A and b, find x)
    # M is a 2D numpy array
    # The upper triangular matrix U is stored in the upper part of the matrix M (including the diagonal)
    # The lower triangular matrix L is stored in the lower part of the matrix M (not including the diagonal)
    # b is a 1D numpy array
    # x is a 1D numpy array
    # Do not use `scipy.linalg.solve_triangular`
    n = len(M)
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(0, n):
        temp = b[i]
        for j in range(0, i):
            temp -= y[j] * M[i, j]
        y[i] = temp

    for i in range(n - 1, -1, -1):
        temp = y[i]
        for j in range(i + 1, n):
            temp -= x[j] * M[i, j]
        x[i] = temp / M[i, i]

    return x

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


def fea_solve(Kpp, Kpf, Kfp, Kff, xp, Ff):
    # Use my_lu and my_triangular_solve
    RHS1 = Ff - np.matmul(Kfp, xp)
    M = my_lu(Kff)
    xf = my_triangular_solve(M, RHS1)
    Fp = np.matmul(Kpp, xp) + np.matmul(Kpf, xf)
    return xf, Fp

