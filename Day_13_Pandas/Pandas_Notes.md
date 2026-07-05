# 🚀 Day 13 — Pandas Basics

## 📦 Installation
```bash
pip install pandas
```

---

## 🏗️ Core Concepts

### 1. Series — 1D Labeled Array
A Series is like a single column in a table or a 1D array, but with labels (an index) for each item.
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s["b"])  # Output: 20
```

### 2. DataFrame — 2D Table
A DataFrame is like an Excel spreadsheet or a SQL table. It is a 2-dimensional data structure with columns of potentially different types.
```python
data = {    
    "Name": ["Hulk", "Antman", "Thor"],    
    "Marks": [91, 89, 75],    
    "Grade": ["A", "B", "B"]
}

df = pd.DataFrame(data)
print(df)
```

---

## 🛠️ Essential Operations
These are your standard diagnostic tools for any new dataset.
```python
df.head()       # Returns the first 5 rows
df.tail(3)      # Returns the last 3 rows
df.info()       # Prints column data types and counts non-null values
df.describe()   # Generates statistical summary (mean, std, min, max, etc.) of numeric columns
df.shape        # Returns a tuple representing dimensionality: (rows, columns)
df.columns      # Returns a list of all column names
df.dtypes       # Returns the specific data type of each column
```

---

## 🎯 Selecting & Filtering Data

### Basic Selection
```python
df["Name"]             # Selects a single column (returns a Series)
df[["Name", "Marks"]]  # Selects multiple columns (returns a DataFrame) - Note the double brackets!
```

### Slicing Data: `loc` vs `iloc`
Think of a DataFrame like an Excel sheet.
```python
data = {    
    "Name":   ["Hulk", "Antman", "Thor", "Iron Man", "Spiderman"],    
    "Age":    [30, 25, 35, 40, 20],    
    "Marks":  [91, 89, 75, 88, 95],    
    "City":   ["Delhi", "Mumbai", "Pune", "Chennai", "Jaipur"]
}
df = pd.DataFrame(data)
```

#### `loc` (Label-Based)
Uses the literal row index names and column names.
**⚠️ Important:** `loc` slices are inclusive on BOTH ends. `loc[1:3]` includes rows 1, 2, AND 3.
```python
df.loc[0]                    # Entire row 0
df.loc[2, "Marks"]           # Row 2, "Marks" column
df.loc[1:3, "Name":"Marks"]  # Rows 1 through 3, Columns "Name" through "Marks"
```

#### `iloc` (Integer/Position-Based)
Uses numerical positions only (like standard Python arrays).
**⚠️ Important:** `iloc` slices exclude the end index. `iloc[0:3]` includes rows 0, 1, and 2 only.
```python
df.iloc[0]             # First row
df.iloc[-1]            # Last row
df.iloc[0, 2]          # Row index 0, Column index 2
df.iloc[0:3, 0:2]      # Rows 0-2, Columns 0-1
```

#### ❌ Common Mistake Warning
```python
df.loc[0:2, 0:2]             # ❌ Crash! loc needs column NAMES, not numbers.
df.loc[0:2, "Name":"Marks"]  # ✅ Correct.
df.iloc[0:2, 0:2]            # ✅ Correct. iloc uses numbers for both.
```

### Filtering (Boolean Indexing)
```python
df[df["Marks"] > 80]                          # Returns all rows where Marks > 80
df[(df["Marks"] > 80) & (df["Grade"] == "A")] # Multiple conditions (Requires parentheses and bitwise '&')
```

---

## 📥 Ingestion
```python
df = pd.read_csv("students.csv") # Loads a CSV file from your local directory into a DataFrame
```

---

## 📝 Tasks Completed:
1. Create a DataFrame of 5 students with columns: Name, Age, Marks, City. Display it.
2. Select only Name and Marks columns.
3. Filter students with Marks > 70.
4. Use `loc` to get row 2 and `iloc` to get the last row.
5. Find mean, max, min of the Marks column.
6. Download Titanic dataset from Kaggle → load it (`train.csv`) → run `head()`, `info()`, `describe()`, `shape`.
