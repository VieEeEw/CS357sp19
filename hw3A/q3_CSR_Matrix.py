import numpy as np
from scipy.sparse import csr_matrix

indptr = np.array([0, 2, 3, 6, 6])
indices = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])
A_csr = csr_matrix((data, indices, indptr), shape=(4, 3))
print(A_csr)

# csr = csr_matrix((data, indices, indptr), shape=(4, 3)).toarray()
# print(csr)

data, index_list, rowptr = (A_csr.data, A_csr.indices, A_csr.indptr)
# print(data, index_list, rowptr)
# cols, rows = A_csr.shape
A = np.zeros(A_csr.shape)
print(A)
d_count = 0
index_list_count = 0
row_count = 0
last_row_element = 0
for n in rowptr:
    if n == 0:
        continue
    delta = n - last_row_element
    last_row_element = n
    for i in range(delta):
        A[row_count,index_list[index_list_count]] = data[d_count]
        index_list_count += 1
        d_count += 1

    row_count += 1

# print(A)

