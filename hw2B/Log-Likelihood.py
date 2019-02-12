import numpy as np
prob = np.float64(0.0688)
combine = np.float64(1.0)
for i in range(1,100000,1):
    combine *= prob
    if combine != 0.0:
        # print(combine)
        pass
    else:
        print(i-1)
        break
print(combine)
