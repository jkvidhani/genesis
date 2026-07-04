
# 7.Given a 5x5 random matrix — find which row has the highest sum.
import numpy as np

a = np.arange(1,26).reshape(5,5)

row_sum = np.sum(a, axis = 1)

print(f"Row with max sum: Row({np.argmax(row_sum)}),sum({np.max(row_sum)})") 