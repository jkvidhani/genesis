
# 9.Find all indices where value is greater than 50 in array [10, 60, 30, 80, 20, 90].
import numpy as np

a = np.array([10, 60, 30, 80, 20, 90])

# M1
for i in range(len(a)):
    if a[i]>50:
        print(i)

# M2
indi = np.where(a > 50)
print(indi)
    