# 1.Check null counts for all columns
# 2.Drop Cabin column — too many nulls
# 3.Fill Age nulls with median
# 4.Fill Embarked nulls with most frequent value
# 5.Verify no nulls remain with isnull().sum()
# 6.Drop any duplicate rows

import pandas as pd
data = pd.read_csv("train.csv")
df = pd.DataFrame(data)

#7.
before_shape = df.shape

#1
null_col = df.isnull().sum(axis=0)  #print(null_col)

#2
df = df.drop(columns = ["Cabin"])  #print(df)

#3
df["Age"] = df["Age"].fillna(df["Age"].median())  #print(df["Age"].isnull().sum())

#4
df["Embarked"] = df["Embarked"].fillna("S") 
#OR
#✨df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  #print(df["Embarked"].isnull().sum())

#5
print(df.isnull().sum())

#6
df = df.drop_duplicates()  #print(df.duplicated().sum())

#7
after_shape = df.shape
print(before_shape)
print(after_shape)






