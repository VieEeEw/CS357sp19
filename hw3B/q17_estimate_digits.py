import numpy as np
from numpy import linalg as la
from math import log10, ceil, floor
import scipy
from scipy import linalg

w = la.cond(A)
w = log10(w)
ep = np.finfo(float).eps
s = abs(log10(ep))

correct_digits = floor(s - w)
x = la.solve(A, b)
