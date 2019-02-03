import numpy as np


def genRandomVect():
    # define return numpy array
    x = np.arange(100)
    x = np.random.choice(x, 50, replace=False)
    return (x)


print(genRandomVect())
