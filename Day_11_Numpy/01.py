# 1.Create a 1D array of numbers 1-20. Print only even numbers using boolean indexing.
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#OR
arrr = np.arange(1,21)

print(arr[arr%2==0]) 
