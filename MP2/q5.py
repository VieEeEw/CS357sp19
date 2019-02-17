import numpy as np
from scipy.signal import convolve2d
from matplotlib import colors
import matplotlib
import matplotlib.pyplot as plt
from math import floor, sqrt


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


def filter_design_variable(xvec, H, H1):
    x = xvec.reshape(H1.shape)
    xf = convolve2d(x, H, mode='same') / H1
    xf = xf.reshape(xvec.shape)
    return xf


H, H1 = create_kernel(2.5, nelx, nely)
xfilt = filter_design_variable(xvec, H, H1)
image = -xfilt.reshape((nelx, nely)).T
image_plot = plt.imshow(image, cmap='gray', vmin=0, vmax=250)
matplotlib.pyplot.imshow(image, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
