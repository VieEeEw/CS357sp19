from sympy import Function, hessian, pprint, Matrix
from sympy import sin, cos, sqrt, symbols, diff
from mpmath import e
import numpy as np
from numpy import float64

x1, x2 = symbols('x1,x2')
x1_val = 9
x2_val = 9
x_vec = np.array([x1_val, x2_val])
# f = Function('f')(x1, x2)
# g1 = Function('g')(x1, x2)
# g2 = sqrt(x1) + x1 * x2
# f = 4.5 * x2 ** 2 + 2 * x1 * x2 + 4 * x2 ** 2
# f = 2 * x1 ** 2 + 2 * x1 * x2 + 2.5 * x2 ** 2
# f = 2.5 * x1 ** 2 + 2 * x1 * x2 + 5.5 * x2 ** 2
f =  x1 ** 2 +  x1 * x2 +  x2 ** 2 + 5*x1
X = Matrix([f])
Y = Matrix([x1, x2])
jac = X.jacobian(Y)
print(jac)
fx1 = diff(f, "x1")
fx2 = diff(f, "x2")

h = hessian(X, Y)
print(h)
RHS = -jac.evalf(subs={x1: x1_val, x2: x2_val})
RHS = np.array(RHS).reshape((2,)).astype(float64)
Hf = np.array(h.evalf()).astype(float64)
print(Hf)
print(RHS)
print(Hf.shape, RHS.shape)
Sk = np.linalg.solve(Hf, RHS)
print(Sk)
xk = Sk + x_vec
print(xk)
# print(x_vec + Sk)
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
