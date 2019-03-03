r = 1.0

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
# It may be helpful to complete this function
def norm(x, p):
    """Computes a p-norm.

    Args:
        x (ndarray): input array
        p (int or float): order of the norm

    Returns:
        (float): the p-norm of the array
    """
    return la.norm(x,p)

ps = [1, 2, 5, 0.5]
phi = np.linspace(0, 2 * np.pi, 500)
unit_circle = np.array([np.cos(phi), np.sin(phi)])
plt.figure()
fig_1 = plt.gca()