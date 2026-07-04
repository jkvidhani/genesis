
# 4.Find all unique values AND their counts in [1,2,2,3,3,3,4,4,4,4].
import numpy as np

a = np.array([1,2,2,3,3,3,3,4,4,4,4,4])

unique_val, counts = np.unique(a, return_counts= True)
print(f"Unique Values: {unique_val}")
print(f"Counts: {counts}")