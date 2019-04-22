import sympy as sp
from sympy import sin, cos
from mpmath import e
from sympy import *

x, h = symbols('x h')
x_0 = 0.45

# f = -e ** (-x ** 2)
f = cos(x)
fp = diff(f, x)
fpp = diff(fp, x)

print(f)
print(fp)
print(fpp)
ft = f + fp * h + fpp / 2 * h ** 2
x_next = x - fp / fpp
print(x_next.subs("x", x_0))
