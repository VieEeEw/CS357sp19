import numpy as np

def func(xvec):
    # xvec: 1d numpy array
    # f: float
    # code to obtain f
    return f

def dfunc(x, dx):
    # ADD CODE HERE
    df = []
    for i in range(len(x)):
        origin = func(x)
        x[i] += dx
        after = func(x)
        derivative = (after - origin ) / dx
        x[i] -= dx
        df.append(derivative)
    return np.array(df)