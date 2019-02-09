import numpy as np
# delta = np.finfo(float).eps
delta = 0.15
smallest = delta
smallest_num = delta
while smallest != 0:
    smallest_num = smallest
    smallest /= 2

print(smallest_num)