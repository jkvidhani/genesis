
# 5.Generate 1000 random numbers from normal distribution. Find mean and std — should be close to 0 and 1.
import numpy as np

a = np.random.normal(0,1,1000)

print(a)
print(np.mean(a)) 
print(np.std(a)) 