from sympy import Function, hessian, pprint, Matrix
from sympy import sin, cos, sqrt, symbols, diff, pi
from mpmath import e
import numpy as np
from numpy import float64

x1, x2 = symbols('x1,x2')
x1_val = pi / 3
x2_val = pi / (2 * sqrt(2))
x_vec = np.array([x1_val, x2_val])
# f = Function('f')(x1, x2)
# g1 = Function('g')(x1, x2)
# g2 = sqrt(x1) + x1 * x2
# f = 4.5 * x2 ** 2 + 2 * x1 * x2 + 4 * x2 ** 2
# f = 2 * x1 ** 2 + 2 * x1 * x2 + 2.5 * x2 ** 2
# f = 2.5 * x1 ** 2 + 2 * x1 * x2 + 5.5 * x2 ** 2
# f = 12 * x1 ** 2 + 3 * x1 * x2 + 12 * x2 ** 2 + 9 * e ** (4 * x1 * x2) + 8 * (sin(x2)) ** 2 + 5 * cos(x1 * x2)
f = 3 + x1 ** 2 / 8 + x2 ** 2 / 8 - sin(x1) * cos(sqrt(2) / 2 * x2)
# X = Matrix([f])
# Y = Matrix([x1, x2])
# jac = X.jacobian(Y)
# print(jac)
fx1 = diff(f, "x1")
fx2 = diff(f, "x2")
jac = np.array([fx1.evalf(subs={x1: x1_val, x2: x2_val}),
                fx2.evalf(subs={x1: x1_val, x2: x2_val})])
h = hessian(f, (x1, x2))
# print(h)
RHS = -jac
RHS = np.array(RHS).reshape((2,)).astype(float64)
Hf = np.array(h.evalf(subs={x1: x1_val, x2: x2_val})).astype(float64)

print(jac)
print()
print(Hf)
print()
# print(Hf.shape, RHS.shape)
Sk = np.linalg.solve(Hf, RHS)
# print(Sk)
xk = Sk + x_vec
# print(x_vec + Sk)
print(xk)
print()
# print(RHS)

# fx1x1 = diff(fx1, "x1")
# fx2x2 = diff(fx2, "x2")
# fx1x2 = diff(fx1, "x2")
# fx2x1 = diff(fx2, "x1")
# print(fx1x2)
# print(fx2x1)
# print(fx1x2.evalf(subs={x1: x1_val, x2: x2_val}))
#
# h = hessian(f, (x1, x2))
# pprint(h)
# pprint(h.evalf(subs={x1: x1_val, x2: x2_val}))
a = 1.581
print(a*RHS + x_vec)