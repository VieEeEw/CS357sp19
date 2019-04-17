import numpy as np
import pandas as pd

labels = ['patient ID', 'Malignant/Benign', 'radius (mean)', 'radius (stderr)', 'radius (worst)', 'texture (mean)',
          'texture (stderr)', 'texture (worst)', 'perimeter (mean)', 'perimeter (stderr)', 'perimeter (worst)',
          'area (mean)', 'area (stderr)', 'area (worst)', 'smoothness (mean)', 'smoothness (stderr)',
          'smoothness (worst)', 'compactness (mean)', 'compactness (stderr)', 'compactness (worst)', 'concavity (mean)',
          'concavity (stderr)', 'concavity (worst)', 'concave points (mean)', 'concave points (stderr)',
          'concave points (worst)', 'symmetry (mean)', 'symmetry (stderr)', 'symmetry (worst)',
          'fractal dimension (mean)', 'fractal dimension (stderr)', 'fractal dimension (worst)']

tumor_data: pd.DataFrame = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)


def myfunc(category: str) -> np.float64:
    if category == "M":
        return 1.0
    else:
        return -1.0


col2 = tumor_data[labels[1]]
b = col2.apply(myfunc)
b = np.array(b)
print(np.array(b))
