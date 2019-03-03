import numpy as np
from numpy import linalg as la
a = np.array([[1,1],[1,-1]])
y = np.array([11,-1]).reshape(2,1)
result = la.solve(a,y)
print(result)

