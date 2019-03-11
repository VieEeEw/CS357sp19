import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from math import sqrt

Ke = np.arange(200)
A1 = np.zeros((200,200))
A22 = np.zeros((200, 200))


for i in range(200):
    if i == 0:
        row = np.zeros(200)
        row[i] = -2
        row[i + 1] = 1
        A1[i] = row
    elif i == 199:
        row = np.zeros(200)
        row[i] = -2
        row[i - 1] = 1
        A1[i] = row
    else:
        row = np.zeros(200)
        row[i] = -2
        row[i + 1] = 1
        row[i - 1] = 1
        A1[i] = row

for i in range(200):
    if i == 0:
        row = np.zeros(200)
        row[i] = -(2 + Ke[i])
        row[i + 1] = 1
        A22[i] = row
    elif i == 199:
        row = np.zeros(200)
        row[i] = -(2 + Ke[i])
        row[i - 1] = 1
        A22[i] = row
    else:
        row = np.zeros(200)
        row[i] = -(2 + Ke[i])
        row[i + 1] = 1
        row[i - 1] = 1
        A22[i] = row

val1, vec1 = la.eig(A1)
val2, vec2 = la.eig(A22)

eigens1 = [(x,y) for x,y in zip(val1,vec1.T)]
eigens2 = [(x,y) for x,y in zip(val2,vec2.T)]
eigens1.sort(key=lambda r:abs(r[0]))
eigens2.sort(key=lambda r:abs(r[0]))


# print(eigens1[0])
val1_low5freq = [x for x,y in eigens1[:5]]
val2_low5freq = [x for x,y in eigens2[:5]]
vec1_low5freq = [y for x,y in eigens1[:5]]
vec2_low5freq = [y for x,y in eigens2[:5]]

val1_low5freq = np.array(val1_low5freq).T
val2_low5freq = np.array(val2_low5freq).T
vec1_low5freq = np.array(vec1_low5freq).T
vec2_low5freq = np.array(vec1_low5freq).T

print(A22)
A2 = np.zeros((200, 200))
to_insert = np.zeros(200)
to_insert[0] = -(2 + Ke[0])
to_insert[1] = 1
# print(to_insert)
A2[0, :] = to_insert
to_insert = np.zeros(200)
to_insert[0] = 1
to_insert[1] = -(2 + Ke[1])
to_insert[2] = 1
for i in range(1, 199):
    A2[i, :] = to_insert
    to_insert = np.roll(to_insert, 1)
    to_insert[i + 1] = -(2 + Ke[i + 1])
# print(to_insert)
print(to_insert)
to_insert[0] = 0
A2[199, :] = to_insert
print(A2)