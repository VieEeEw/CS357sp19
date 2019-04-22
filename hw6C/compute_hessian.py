from sympy import Function, hessian, pprint
from sympy import sin, cos, sqrt, symbols
from mpmath import e

x1, x2 = symbols('x1,x2')
# f = Function('f')(x1, x2)
# g1 = Function('g')(x1, x2)
# g2 = sqrt(x1) + x1 * x2
g2 = x2 ** 2 * e * x1
pprint(hessian(g2, (x1, x2)))
