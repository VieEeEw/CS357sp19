import numpy as np
from numpy import linalg as la

a1 = 0b111 / 2
a2 = 0b110 / 2
a3 = 0b111
x1 = np.array([3.625, 3.375, 7.25])
x2 = np.array([a1, a2, a3])

s1 = sum(x1)
s2 = a1 + a2 + a3
print(s1, s2, s2 - s1)
