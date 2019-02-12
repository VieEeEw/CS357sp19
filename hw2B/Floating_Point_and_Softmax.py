import numpy as np
import math
z = [0.00000, 86.55428, 84.81076, 84.97763]
z = np.array(z)

def softmax(z,i):
    sum = 0
    for x in z:
        sum += math.e ** x
    result = math.e ** z[i] / sum
    return result

def overfloat(z):
    sum = 0
    for x in z:
        sum += math.e ** x
    return sum


sum = overfloat(z)
large = np.finfo(np.float32).max
delta = large - sum
print(large - sum)
print(math.log(delta,math.e))
# accumulation = delta
# while accumulation < 1:
#     accumulation += delta
#     z[0] = accumulation
#     softmax(z,0)