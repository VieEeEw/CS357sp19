import numpy as np
# 先sort，从小加到大最准确
data = np.array([0.123412341, 1.23421341, 2.2341234, 4.234123])
data_sum = sum(data)
print(data_sum)
data_sum = sum(np.sort(data))
print(data_sum)