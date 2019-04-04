import numpy as np
import pandas as pd
from numpy.linalg import inv

# Load the data
labels = ['patient ID', 'Malignant/Benign', 'radius (mean)', 'radius (stderr)', 'radius (worst)', 'texture (mean)',
          'texture (stderr)', 'texture (worst)', 'perimeter (mean)', 'perimeter (stderr)', 'perimeter (worst)',
          'area (mean)', 'area (stderr)', 'area (worst)', 'smoothness (mean)', 'smoothness (stderr)',
          'smoothness (worst)', 'compactness (mean)', 'compactness (stderr)', 'compactness (worst)', 'concavity (mean)',
          'concavity (stderr)', 'concavity (worst)', 'concave points (mean)', 'concave points (stderr)',
          'concave points (worst)', 'symmetry (mean)', 'symmetry (stderr)', 'symmetry (worst)',
          'fractal dimension (mean)', 'fractal dimension (stderr)', 'fractal dimension (worst)']
subset_labels = ['smoothness (worst)', 'concave points (stderr)', 'area (mean)', 'fractal dimension (mean)']

tumor_data = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)


def myfunc(category: str) -> np.float64:
    if category == "M":
        return 1.0
    else:
        return -1.0


col2 = tumor_data[labels[1]]
b = col2.apply(myfunc)
b = np.array(b)

matrix = []
for l in labels[2:32]:
    matrix.append(tumor_data[l])
A_linear: np.ndarray = np.array(matrix).T
print(A_linear.shape)

matrix = []
for l in subset_labels:
    matrix.append(tumor_data[l])
for l in subset_labels:
    matrix.append(tumor_data[l] ** 2)
for i in range(3):
    for j in range(i + 1, 4):
        matrix.append(tumor_data[subset_labels[i]] * tumor_data[subset_labels[j]])

A_quad: np.ndarray = np.array(matrix).T

weights_linear = inv(A_linear.T @ A_linear) @ A_linear.T @ b
weights_quad = inv(A_quad.T @ A_quad) @ A_quad.T @ b

validate_data = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)

matrix = validate_data[labels[2:32]]
A_val_linear: np.ndarray = np.array(matrix)

df1 = validate_data[subset_labels]
df2 = validate_data[subset_labels] ** 2
A_val_quad = pd.concat([df1, df2], axis=1)
for i in range(3):
    for j in range(i + 1, 4):
        dfn = validate_data[subset_labels[i]] * validate_data[subset_labels[j]]
        A_val_quad = pd.concat([A_val_quad, dfn], axis=1)

A_val_quad: np.ndarray = np.array(A_val_quad)

newb = validate_data[labels[1]].apply(myfunc)
newb = np.array(newb)
fn_linear = ((newb > 0) & ((A_val_linear @ weights_linear) < 0)).sum()
fp_linear = ((newb < 0) & ((A_val_linear @ weights_linear) > 0)).sum()



print(fn_linear)
print(newb.shape, A_val_linear.shape,weights_linear.shape)
