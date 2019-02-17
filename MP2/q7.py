import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

xnew1 = topopt(ft=2)
xnew2 = topopt(rmin=1.5, ft=1)
xnew3 = topopt(rmin=2.5, ft=1)
xnew4 = topopt(rmin=4.0, ft=1)

image1 = -xnew1.reshape((60, 30)).T
image2 = -xnew2.reshape((60, 30)).T
image3 = -xnew3.reshape((60, 30)).T
image4 = -xnew4.reshape((60, 30)).T

image_plot_1 = plt.imshow(image1, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
image_plot_2 = plt.imshow(image2, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
image_plot_3 = plt.imshow(image3, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
image_plot_4 = plt.imshow(image4, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1, vmax=0))
