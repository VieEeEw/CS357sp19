import numpy as np
import math

def create_kernel(rmin):
    N = 2*math.floor(rmin) + 1
    H = np.zeros((N,N))
    xc = N//2
    yc = N//2
    for i in range(N):
        for j in range(0, N):
            delta = math.sqrt((xc - i)**2 + (yc - j)**2)
            H[i][j] = max(0, rmin-delta)
    return H