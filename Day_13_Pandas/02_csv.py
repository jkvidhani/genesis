# 6.Download Titanic dataset from Kaggle → load it → run head(), info(), describe(), shape.

import pandas as pd

df = pd.read_csv("train.csv")

print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)