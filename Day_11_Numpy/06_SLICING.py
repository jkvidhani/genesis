
# 6.From a 10x10 matrix, extract the first 3 rows and last 2 columns.
import numpy as np

a = np.arange(1,101)
b = a.reshape(10,10)

print(f" First 3 rows:\n{b[0:3]} \n\n Last 2 col:\n{b[:, -2:]}")  
#✨✨ b[:, -2:]