import pandas as pd
from matplotlib import pyplot as plt

labels: list
tumor_data: pd.DataFrame = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)
user_column = labels[30]
t: plt.Axes = tumor_data[user_column].hist()
t.set_xlabel("haha")
t.set_ylabel("lol")
t.set_title("chichi")
bla: str
