import numpy as np
prob = np.float64(0.047)
combine = np.float64(1.0)
for i in range(100000):
    combine *= prob
    if combine != 0.0:
        print(combine)
    else:
        print(i)
        break
print(combine)