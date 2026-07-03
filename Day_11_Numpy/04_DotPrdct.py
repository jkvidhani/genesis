
# 4.Create two arrays [1,2,3] and [4,5,6]. Multiply element-wise and find the dot product.
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
c = a * b 
print(c)
print(f"Dot product: {np.dot(a,b)}")
