import numpy as np
import math
z = [0.00000, 85.03178, 86.32700, 86.06900]
z = np.array(z)

def softmax(z,i):
    sum = 0
    for x in z:
        sum += math.e ** x
    result = math.e ** z[i] / sum
    return result

delta = np.finfo(float).eps
accumulation = delta
while accumulation < 1:
    accumulation += delta
    z[0] = accumulation
    softmax(z,0)