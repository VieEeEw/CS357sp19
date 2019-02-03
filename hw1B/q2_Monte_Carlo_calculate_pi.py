from math import sqrt
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def calculate_pi(x, y):
    count = 0
    for x1, y1 in zip(x, y):
        if sqrt(x1 ** 2 + y1 ** 2) <= 1:
            count += 1
    return 4 * count / len(x)


pi = []
for i in range(7):
    sample_x = np.random.rand(10 ** i)
    sample_y = np.random.rand(10 ** i)
    pi.append(calculate_pi(sample_x, sample_y))

pi = np.array(pi)

sample_sizes = [10 ** x for x in range(7)]
errors = [abs(math.pi - x) for x in pi]
plt.loglog(sample_sizes, errors)
plt.xlabel("sample_size")
plt.ylabel("errors")
plt.title("sample_size_VS_errors")
plt.show()
