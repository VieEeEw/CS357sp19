import numpy as np
import pandas as pd

labels = ['patient ID', 'Malignant/Benign', 'radius (mean)', 'radius (stderr)', 'radius (worst)', 'texture (mean)',
          'texture (stderr)', 'texture (worst)', 'perimeter (mean)', 'perimeter (stderr)', 'perimeter (worst)',
          'area (mean)', 'area (stderr)', 'area (worst)', 'smoothness (mean)', 'smoothness (stderr)',
          'smoothness (worst)', 'compactness (mean)', 'compactness (stderr)', 'compactness (worst)', 'concavity (mean)',
          'concavity (stderr)', 'concavity (worst)', 'concave points (mean)', 'concave points (stderr)',
          'concave points (worst)', 'symmetry (mean)', 'symmetry (stderr)', 'symmetry (worst)',
          'fractal dimension (mean)', 'fractal dimension (stderr)', 'fractal dimension (worst)']
subset_labels = ['smoothness (worst)', 'concave points (stderr)', 'area (mean)', 'fractal dimension (mean)',
                 'perimeter (mean)']

tumor_data = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)
matrix = []
for l in subset_labels:
    matrix.append(tumor_data[l])
A_linear: np.ndarray = np.array(matrix).T
print(A_linear.shape)
