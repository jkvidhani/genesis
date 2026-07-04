
# 2.Create a 4x4 random integer matrix (values 1-50). Find sum, mean, max of each row AND each column separately.
import numpy as np

a = np.random.randint(1,50,16).reshape(4,4)
print(f"{a}\n")

#ROW
print(f"sum of rows:\n{np.sum(a, axis=1)}\n")
print(f"max of rows:\n{np.max(a, axis=1)}\n")
print(f"mean of rows:\n{np.mean(a, axis=1)}\n")

#Coloumns
print(f"Sum of col:\n{np.sum(a, axis=0)}\n")
print(f"Max of col:\n{np.max(a, axis=0)}\n")
print(f"Mean of col:\n{np.mean(a, axis=0)}\n")

