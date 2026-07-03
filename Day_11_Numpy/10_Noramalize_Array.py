
# 10.Normalize an array (scale values between 0 and 1): formula = (x - min) / (max - min)
import numpy as np

a =  np.array([1,2,3,4,5])

b = ((a - np.min(a)) / (np.max(a) - np.min(a)))
print(b)