# 1.Create a 3x3 matrix and a 1D array of size 3. Add them using broadcasting.
import numpy as np

a = np.arange(0,9).reshape(3,3) #3x3 Array
print(f"{a}\n") 

b = np.array([1,1,1]) #1D Array
print(f"{b}\n")

c = a+b # b broadcasts across each row
print(f"Broadcasting:\n{c}")