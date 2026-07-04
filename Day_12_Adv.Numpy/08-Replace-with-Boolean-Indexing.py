
# 8.Given marks [45,78,92,34,88,61,55,73] — replace all marks below 60 with 0 using boolean indexing.
import numpy as np

marks = np.array([45,78,92,34,88,61,55,73])
marks[ marks < 60 ] = 0
print(marks)

