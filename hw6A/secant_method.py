import sympy as sp
from sympy import sin
from mpmath import e
import numpy as np


def newton_method(x_val, expr, tol=1e-5):
    count = 0
    expr_diff = sp.diff(expr, 'x')
    pre = expr.subs('x', x_val)
    while True:
        x_val = x_val - expr.subs('x', x_val) / expr_diff.subs('x', x_val)
        print(x_val)
        print(x_val.evalf())
        break
        if abs(pre - abs(expr.subs('x', x_val))) < tol:
            break
        count += 1
        pre = abs(expr.subs('x', x_val))
    # print(count)


def secant(x_0, x_1, expr, tol=1e-5):
    count = 0
    x_k_1 = x_0
    x_k = x_1
    while True:
        temp = x_k
        x_k = x_k - expr.subs('x', x_k) / ((expr.subs('x', x_k) - expr.subs('x', x_k_1)) / (x_k - x_k_1))
        x_k_1 = temp
        print(x_k)
        print(x_k.evalf())
        break
        if abs(x_k - x_k_1) < tol:
            break
        count += 1
    # print(count)


def bisection(a, b, expr, step, tol=1e-5):
    for i in range(step):
        m = (a + b) / 2
        mid = expr.subs('x', m)
        if np.sign(a) == np.sign(mid):
            a = m
        else:
            b = m
    print(a, b, m)


if __name__ == '__main__':
    x = sp.symbols('x')
    expr = sin(x / 6)
    x1 = -1
    x0 = -2
    a = -1
    b = 4
    newton_method(x1, expr)
    secant(x0, x1, expr)
    bisection(a, b, expr, 2)
