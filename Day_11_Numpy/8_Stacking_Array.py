
# 8.Stack two arrays [1,2,3] and [4,5,6] vertically and horizontally.
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

hs = np.hstack([a,b])
vs = np.vstack([a,b])

print(hs)
print(vs)