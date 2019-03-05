import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def fea_solve(Kpp,Kpf,Kfp,Kff,xp,Ff):
    # do stuff here
    RHS1 = Ff - np.matmul(Kfp,xp)
    xf = la.solve(Kff,RHS1)
    Fp = np.matmul(Kpp,xp) + np.matmul(Kpf,xf)
    return xf,Fp