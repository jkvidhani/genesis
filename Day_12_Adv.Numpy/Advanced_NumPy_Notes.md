# 🚀 Day 12 — Advanced NumPy

## 📡 1. Broadcasting

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2,3)
b = np.array([10, 20, 30])            # shape (3,)

# b broadcasts across each row automatically
a + b  
# Output: [[11, 22, 33], [14, 25, 36]]
```

**Rule:** Shapes are compatible if dimensions are equal OR one of them is 1.

## 🧭 2. Axis Operations

```python
a = np.array([[1, 2, 3], 
              [4, 5, 6]])

np.sum(a)           # 21 — sum everything
np.sum(a, axis=0)   # [5, 7, 9] — sum down columns (Vertical)
np.sum(a, axis=1)   # [6, 15] — sum across rows (Horizontal)

np.mean(a, axis=0)  # column means
np.max(a, axis=1)   # max of each row
```

## 🧰 3. Useful Functions

```python
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])

np.argmax(a)   # index of max value → 5
np.argmin(a)   # index of min value → 1
np.unique(a)   # [1, 2, 3, 4, 5, 6, 9] — unique values
np.cumsum(a)   # cumulative sum (running total)
np.diff(a)     # difference between consecutive elements
```

## 🎲 4. Random Module

```python
np.random.seed(42)            # for reproducibility (gets same random numbers every time)
np.random.rand(3, 3)          # random floats between 0 and 1
np.random.randint(0, 100, 10) # 10 random integers between 0 and 100
np.random.normal(0, 1, 1000)  # normal distribution (bell curve)
np.random.shuffle(a)          # shuffle array in place
```

## 🔗 5. np.concatenate

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])  # [1, 2, 3, 4, 5, 6]

# Using .reshape to give them an axis=0 before stacking
np.concatenate([a.reshape(1,3), b.reshape(1,3)], axis=0)  # vstack equivalent
```

## 💡 Modifying an array with boolean indexing:

```python
a[a < 3] = 0  # replaces all values less than 3 with 0
```


## 📝 Question Solved-

1. Create a 3x3 matrix and a 1D array of size 3. Add them using broadcasting.
2. Create a 4x4 random integer matrix (values 1-50). Find sum, mean, max of each row AND each column separately.
3. Given array `[5, 2, 8, 1, 9, 3, 7, 4, 6]` — find the index of max and min without sorting.
4. Find all unique values AND their counts in `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]`.
5. Generate 1000 random numbers from normal distribution. Find mean and std — should be close to 0 and 1.
6. Create two 2x3 matrices. Concatenate them both horizontally and vertically.
7. Given a 5x5 random matrix — find which row has the highest sum.
8. Given marks `[45, 78, 92, 34, 88, 61, 55, 73]` — replace all marks below 60 with 0 using boolean indexing.

