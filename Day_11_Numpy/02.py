# 2.Create a 3x3 matrix of zeros. Replace diagonal with 1s (manually, no np.eye).
import numpy as np

z = np.zeros((3,3))
print(z)   

# M1
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            z[i][j] = 1
print(z)

# M2
np.fill_diagonal(z, 1)  #✨✨
print(z)
   
        
        
