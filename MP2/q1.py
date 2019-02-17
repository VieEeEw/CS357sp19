import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

xvec1 = np.array([0.2, 0.5, 1.0, 0.2, 0.7, 1.0])
xvec2 = np.array([1.0, 0.3, 0.5, 0.5, 0.0, 0.3])


def get_change(xvec1, xvec2):
    return max(abs(xvec1 - xvec2))
