import sympy as sp
from sympy import sin
from mpmath import e
from sympy import *

x, h = symbols('x h')
value = 1

f = 3 * x ** 3 + x ** 2 + 3 * x + 1
# f = 17*x**3 + 21*x**2 + 4*x + 2
fp = diff(f, x)
fpp = diff(fp, x)

print(f)
print(fp)
print(fpp)
ft = f + fp * h + fpp / 2 * h ** 2
result = ft.subs(x, value)
print(result)
