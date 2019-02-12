import numpy as np
import matplotlib.pyplot as plt


def func(x):
    '''
    Parameters
    x: 1D numpy array
    Returns
    f: scalar function value
    '''
    # WRITE YOUR CODE HERE
    return 2 * x[0] ** 2 - 0.5 * x[0] * x[1] + 5 * x[1] ** 3


def dfunc(x):
    '''
    Parameters
    x: 1D numpy array
    Returns
    df: 1D numpy array containing first derivatives wrt x
    '''
    # WRITE YOUR CODE HERE
    d1 = 4 * x[0] - 0.5 * x[1]
    d2 = -0.5 * x[0] + 15 * x[1] ** 2
    return np.array([d1, d2])


def fd(x, dx):
    '''
    Parameters
    x: 1D numpy array
    dx: small perturbation (increment in x)  (scalar)
    Returns
    df: 1D numpy array containing approximations for the first derivatives wrt x
    '''
    # WRITE YOUR CODE HERE
    # d1 = func(x)
    # # x[0] += dx  # increase x1 and fix x2
    # d2 = func([x[0] + dx, x[1]])
    # x0 = (d2 - d1) / dx
    #
    # # x[0] -= dx  # reset it back to original
    #
    # d1 = func(x)  # increase x2 and fix x1
    # # x[1] += dx
    # d2 = func([x[0], x[1] + dx])
    # x1 = (d2 - d1) / dx
    # return np.array([x0, x1])
    print(x)
    d1 = func(x)
    x[0] += dx  # increase x1 and fix x2
    print(x)
    d2 = func(x)
    x0 = (d2 - d1) / dx

    x[0] -= dx  # reset it back to original
    print(x)
    d1 = func(x)  # increase x2 and fix x1
    x[1] += dx
    d2 = func(x)
    x1 = (d2 - d1) / dx
    x[1] -= dx
    return np.array([x0, x1])


xvec = [1, 2]
dxvec = [0.1, 0.2]
error = []
for dx in dxvec:
    df_approx = fd(xvec, dx)
    df_exact = dfunc(xvec)

    ea = max(abs(df_approx - df_exact))
    error.append(ea)
error = np.array(error)
# COMPUTE FINITE DIFFERENCE APPROXIMATIONS FOR DECREASING VALUES OF dx

print(error)

plt.figure()
plt.xlabel("1234")
plt.ylabel("45678")
plt.title("23333")
## Plot the error as a function of the perturbation dx
plt.show()
