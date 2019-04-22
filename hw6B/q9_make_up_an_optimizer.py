import numpy as np

x0 = 2


def f(x):
    return -x ** 3 / 3 + 2 * x ** 2 + 2 * x + 2


def df(x):
    return -x ** 2 + 4 * x + 2



x_k = x0
d = 1
df_val = df(x_k)
while abs(df_val) > 1e-8:
    sk = -f(x_k) / df_val
    x_k = x_k + sk
    df_val = df(x_k)

x = x_k
print(x_k)

# x_k = x0
# d = 1
# delta = 1e-5
# d = 1
# while d > delta:
#     x_k_plus_1 = x_k - f(x_k) / df(x_k)
#     d = abs(x_k - x_k_plus_1)
#     x_k = x_k_plus_1
#     print(df(x_k))
#
# x = x_k
# print(x_k_plus_1)
