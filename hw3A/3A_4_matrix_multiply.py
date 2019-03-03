import numpy as np
x = np.array([15,27]).reshape(2,1)
stock_matrix = np.array([[7.8,8.3],[10.8,7.1]])
result = np.matmul(stock_matrix,x)
print(result)