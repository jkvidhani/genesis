
# 3.Given array [5,2,8,1,9,3,7,4,6] — find index of max and min without sorting.
import numpy as np

a = np.array([5,2,8,1,9,3,7,4,6])
print(f"Max values Index: {np.argmax(a)}")
print(f"Min values Index: {np.argmin(a)}")
