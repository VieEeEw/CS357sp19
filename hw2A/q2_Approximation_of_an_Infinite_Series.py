from math import factorial, sin
import math
import numpy as np
import matplotlib.pyplot as plt

# x = np.random.random()
x = 0.6
desired_rel_error = 2.31152878e-02
N = 0

def exp_taylor(x, n):
    sum = 0
    for i in range(n + 1):
        sum += x ** i / factorial(i)
    return sum


exp_approx = [exp_taylor(x, n) for n in range(10)]
exp_approx = np.array([exp_approx])
exp_approx = exp_approx.reshape(10, )

exp_arr = [math.e ** (x)] * 10
exp_arr = np.array([exp_arr]).reshape(10, )
abs_error = abs(exp_arr - exp_approx)
rel_error = abs(exp_arr - exp_approx) / exp_arr


for i in range(10):
    if rel_error[i] > desired_rel_error:
        N += 1
    else:
        break

print(exp_approx)
print(exp_arr)
print(abs_error)
print(rel_error)
print(N)
degree_arr = [i for i in range(10)]
plt.plot(degree_arr,rel_error)
plt.xlabel('n')
plt.ylabel('rel_error')
plt.grid(True)
plt.title('n-taylor-error')
plt.show()