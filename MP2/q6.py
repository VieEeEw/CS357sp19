import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib
from math import floor, sqrt
from scipy.signal import convolve2d

rmin = 2


def create_kernel(rmin, nelx, nely):
    N = 2 * floor(rmin) + 1
    H = np.zeros((N, N))
    xc = N // 2
    yc = N // 2
    for i in range(N):
        for j in range(N):
            delta = sqrt((xc - i) ** 2 + (yc - j) ** 2)
            H[i][j] = max(0, rmin - delta)
    H1 = convolve2d(np.ones((nelx, nely)), H, mode='same')
    return H, H1


f_value = func(xvec)
df = dfunc(xvec)
xnew = optimizer(xvec, f_value, df)
xfilt = filter_design_variable(xnew)
i = 0

while get_change(xvec, xfilt) > tol and i < maxiter - rmin:
    xvec = xfilt
    f_value = func(xvec)
    df = dfunc(xvec)
    xnew = optimizer(xvec, f_value, df)
    xfilt = filter_design_variable(xnew)
    i += 1

xnew = xfilt

xfilt = xfilt.reshape((nelx, nely))
image = -xfilt.T
image_plot = plt.imshow(image, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
