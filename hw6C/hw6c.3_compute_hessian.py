from sympy import Function, hessian, pprint
from sympy import sin, cos, sqrt, symbols, diff
from mpmath import e

x1, x2 = symbols('x1,x2')
x1_val = 0.9
x2_val = 1.6
# f = Function('f')(x1, x2)
# g1 = Function('g')(x1, x2)
# g2 = sqrt(x1) + x1 * x2
f = (x2 ** 2) * e ** x1
# f = sqrt(x1) + x1*x2
fx1 = diff(f, "x1")
fx2 = diff(f, "x2")
fx1x1 = diff(fx1, "x1")
fx2x2 = diff(fx2, "x2")
fx1x2 = diff(fx1, "x2")
fx2x1 = diff(fx2, "x1")
print(fx1x2)
print(fx2x1)
print(fx1x2.evalf(subs={x1: x1_val, x2: x2_val}))

h = hessian(f, (x1, x2))
pprint(h)
pprint(h.evalf(subs={x1: x1_val, x2:x2_val}))
