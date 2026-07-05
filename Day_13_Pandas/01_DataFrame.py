# 1. Create a DataFrame of 5 students with columns: Name, Age, Marks, City. Display it.
# 2. Select only Name and Marks columns.
# 3. Filter students with Marks > 70.
# 4. Use loc to get row 2 and iloc to get last row.
# 5. Find mean, max, min of Marks column.


import pandas as pd

Data = {
    "Name" : ["J", "Spidey", "Thor", "Deadpool", "Tony"],
    "Age" : [19,25,9999,69,49],
    "Marks" : [18,98,77,67,100],
    "City" : ["New York", "New York", "Asguard", "Homeless", "California"],
}

df = pd.DataFrame(Data)
print(df)

# print(df[["Name","Age"]])

# print(df[df["Marks"] > 80])

# print(df.loc[2])
# print(df.iloc[-1])

# print(df["Marks"].max())
# print(df["Marks"].min())
# print(df["Marks"].mean())
