# 3.Given marks array [45, 78, 92, 34, 88, 61] — find mean, max, min, std.
import numpy as np

arr = np.array([45, 78, 92, 34, 88, 61])
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.std())

sum = np.sum(arr)
print(sum)
print(np.sum(arr))
print(arr.sum())