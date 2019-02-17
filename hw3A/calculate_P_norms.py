import numpy as np
from numpy import linalg as la

v = np.array([5, 2, 0, -2])
for i in range(1, 6):
    print(i, la.norm(v, i))
