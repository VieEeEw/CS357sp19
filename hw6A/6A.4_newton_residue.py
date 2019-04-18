import sympy as sp
from sympy import sin
from mpmath import e


def calculate_iteration(x_val, tol, expr):
    count = 0
    expr_diff = sp.diff(expr, 'x')
    pre = expr.subs('x', x_val)
    while True:
        x_val = x_val - expr.subs('x', x_val) / expr_diff.subs('x', x_val)
        if abs(pre - abs(expr.subs('x', x_val))) < tol:
            break
        count += 1
        pre = abs(expr.subs('x', x_val))
    print(count)


if __name__ == '__main__':
    x = sp.symbols('x')
    x_val = 3.2
    tol = 1e-9
    expr = x * (3-x)**2
    calculate_iteration(x_val, tol, expr)
