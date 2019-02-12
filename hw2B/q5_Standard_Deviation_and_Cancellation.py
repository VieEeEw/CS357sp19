import numpy as np
from math import sqrt
sequence = np.array([a for a in np.arange(1, 11, 1)])
bad_sequence = np.array([a for a in np.arange(1991232345.234, 1991232385.23412, 2.234)])
# print(x)
def sig1(x):
    mean = np.mean(x)
    sum_arr = (x - mean)**2
    # print(sum_arr)
    sum = np.sum(sum_arr)
    sigma = sqrt(sum/(len(x)-1))
    return sigma

def sig2(x):
    mean = np.mean(x)
    # print(mean)
    sum_arr = x**2 - mean**2
    # print(x**2,len(x)*mean**2)
    print(sum_arr)
    sum = abs(np.sum(sum_arr))
    sigma = sqrt(sum / (len(x) - 1))
    return sigma

var_seq_tp = sig1(sequence)
print(var_seq_tp)
var_seq_op = sig2(sequence)
print(var_seq_op)
print(np.std(sequence))
var_seq_tp = sig1(bad_sequence)
print(var_seq_tp)
var_seq_op = sig2(bad_sequence)
print(var_seq_op)