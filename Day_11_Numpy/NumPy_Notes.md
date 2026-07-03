# 🚀 NumPy: The Basics & Beyond

## ❓ Why NumPy exists
Python lists are slow for math. NumPy arrays are **50x faster** because they store data in fixed types and use C under the hood. Every ML library (Pandas, Scikit-learn, TensorFlow) uses NumPy internally.

---

## 💻 Installation
```bash
pip install numpy
```

---

## 🧱 The Basics
```python
import numpy as np

# Create arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

# Shape and dimensions
print(a.shape)   # (5,)
print(b.shape)   # (2, 3) → 2 rows, 3 columns
print(b.ndim)    # 2

# Creating special arrays
np.zeros((3, 3))      # 3x3 matrix of zeros
np.ones((2, 4))       # 2x4 matrix of ones
np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1
```

---

## ➕ Math Operations
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b        # [5, 7, 9]
a * b        # [4, 10, 18]
a ** 2       # [1, 4, 9]
np.sqrt(a)   # [1, 1.41, 1.73]
np.sum(a)    # 6
np.mean(a)   # 2.0
np.max(a)    # 3
np.min(a)    # 1
np.std(a)    # standard deviation
```

---

## ✂️ Indexing and Slicing
```python
a = np.array([10, 20, 30, 40, 50])

a[0]      # 10
a[-1]     # 50
a[1:4]    # [20, 30, 40]
a[::2]    # [10, 30, 50] every 2nd element

# 2D indexing
b = np.array([[1, 2, 3], [4, 5, 6]])
b[0]      # [1, 2, 3] first row
b[1][2]   # 6 → row 1, col 2
b[1, 2]   # same thing, cleaner
```

---

## 🚦 Boolean Indexing
```python
a = np.array([10, 25, 30, 45, 50])
a[a > 30]      # [45, 50] — filter values above 30
a[a % 2 == 0]  # even numbers only
```

---

## 🔄 Reshaping
```python
a = np.arange(0, 100)  # array of 0-99
b = a.reshape(10, 10)  # reshape into 10x10 matrix
print(b)
```

---

## 🧠 Advanced Operations
```python
# Dot product:
np.dot(a, b)  # or a @ b

# Vertical and horizontal stacking:
np.vstack([a, b])  # stack vertically (on top of each other)
np.hstack([a, b])  # stack horizontally (side by side)

# Find indices where condition is true:
np.where(a > 50)  # returns indices of elements > 50

# Normalization formula:
normalized = (a - np.min(a)) / (np.max(a) - np.min(a))
```

---

## 🔬 Deeper Level of Indexing and Slicing

### ➡️ Fancy Indexing (Pick specific indices)
```python
a = np.array([10, 20, 30, 40, 50])
a[[0, 2, 4]]  # [10, 30, 50]

# 2D fancy indexing
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b[[0, 2]]        # rows 0 and 2 → [[1,2,3],[7,8,9]]
b[[0,1], [1,2]]  # (row0,col1) and (row1,col2) → [2, 6]
```

### ➡️ Slicing 2D arrays properly
```python
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b[:, 0]     # all rows, column 0 → [1, 4, 7]
b[0, :]     # row 0, all columns → [1, 2, 3]
b[0:2, 1:]  # rows 0-1, columns 1 onwards → [[2,3],[5,6]]
b[:, -1]    # last column → [3, 6, 9]
```

### ➡️ Boolean indexing with multiple conditions
```python
a = np.array([10, 25, 30, 45, 50, 15])
a[(a > 20) & (a < 50)]   # AND → [25, 30, 45]
a[(a < 20) | (a > 40)]   # OR  → [10, 45, 50, 15]
```

### ➡️ Modifying with indexing
```python
a = np.array([1, 2, 3, 4, 5])
a[a < 3] = 0      # replace values less than 3 with 0
print(a)          # [0, 0, 3, 4, 5]

# 2D — set entire row to zeros
b[1, :] = 0       # row 1 becomes all zeros
```

### ➡️ np.where (Conditional replacement)
```python
a = np.array([10, 25, 30, 45, 50])

# where condition is true → replace with 1, else 0
np.where(a > 30, 1, 0)   # [0, 0, 0, 1, 1]

# where condition is true → keep value, else replace with 0
np.where(a > 30, a, 0)   # [0, 0, 0, 45, 50]
```
