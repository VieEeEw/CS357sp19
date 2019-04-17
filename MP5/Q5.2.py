import pandas as pd
from typing import List,Dict,Optional,Union,Any
import numpy as np
import scipy
import numpy.linalg as la

A = np.array([[1,100],
              [4,500],
              [5,300]])
b = np.array([200,400,100])
r= la.pinv(A) @ b
print(r)