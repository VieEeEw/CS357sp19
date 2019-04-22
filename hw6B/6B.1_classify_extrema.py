import sympy as sp
from sympy import sin
from mpmath import e
from sympy import *
from sympy.solvers import solve

x = symbols('x')
x0 = -0.499
x1 = 4.449

f = -x ** 3 / 3 + 4 * x ** 2 / 2 + 2 * x + 2
# f = 17*x**3 + 21*x**2 + 4*x + 2
fp = diff(f, x)
fpp = diff(fp, x)
roots = solve(fp, x)
print(roots[0].evalf(), roots[1].evalf())

print(f)
print(fp)
print(fpp)
print(fpp.subs(x, roots[0].evalf()), fpp.subs(x, roots[1].evalf()))
#
# result0 = ft.subs(x, x0)
# result1 = ft.subs(x, x1)
# print(result0)
# print(result1)
