import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

identity_filter = np.array([[0, 0, 0], [0, 1.0, 0], [0, 0, 0]])
identity_image = convolve2d(image, identity_filter, mode='same')

blur_filter = [1 / 9 for i in range(9)]
blur_filter = np.array(blur_filter).reshape(3, 3)
blurred_image = convolve2d(image, blur_filter, mode='same')

sharpen_filter = 2 * identity_filter - blur_filter
sharpened_image = convolve2d(image, sharpen_filter, mode='same')
