import numpy as np
A = {0: {2: 17, 3: 31}, 1: {3: 5}, 3: {1: 14}}
x = np.array([1, 1, 1, 1])
Ax = np.zeros(x.shape)
for row_num in A.keys():
    for col_num in A[row_num].keys():
        Ax[row_num] += A[row_num][col_num] * x[col_num]

print(Ax)
print(type(x.shape),x.shape)