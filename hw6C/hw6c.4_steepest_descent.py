from sympy import Function, hessian, pprint
from sympy import sin, cos, sqrt, symbols, diff
from mpmath import e
import numpy as np

x1, x2 = symbols('x1,x2')
x1_val = 2.2
x2_val = 4.3
# f = 10 * x1 ** 3 - 2 * x2 ** 2 + x1 - 1
# f = x1 ** 2 - 2 * x2 ** 4
f = sin(x1) + 2 * sqrt(x2)
fx1 = diff(f, "x1")
fx2 = diff(f, "x2")

entry1 = fx1.evalf(subs={x1: x1_val, x2: x2_val})
entry2 = fx2.evalf(subs={x1: x1_val, x2: x2_val})
vec = np.array([entry1, entry2]).T
print(vec)
# h = hessian(f, (x1, x2))
# pprint(h)
# pprint(h.evalf(subs={x1: x1_val, x2:x2_val}))
