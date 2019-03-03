import numpy as np
from math import cos, sin,pi
from numpy import linalg as la

def rotation_matrix(theta, counterclockwise=True):
    radian = theta / 180 * pi
    matrix = np.array([[cos(radian), -sin(radian)], [sin(radian), cos(radian)]])
    if counterclockwise:
        print(matrix)
    else:
        """matrix.T or matrix inverse for rotational matrix is the same
           and reverse the rotation direction"""
        print(matrix)
        print(matrix.T)
        print(la.inv(matrix))
        #


rotation_matrix(330,True)