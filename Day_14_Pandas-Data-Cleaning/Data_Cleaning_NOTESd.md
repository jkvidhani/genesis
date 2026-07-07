# 🧹 Day 14 — Data Cleaning & Preprocessing (Cheat Sheet)

## 🏗️ Core Diagnostics
Before manipulating data, you must understand its state, shape, and deficiencies.

### 1. The Shape Attribute
```python
df.shape  # Returns (rows, columns). 
# Note: It is an attribute, NOT a method. No parentheses ().

## Check nulls:
```python
df.isnull().sum()        # count nulls per column
df.isnull().sum() / len(df) * 100  # null percentage
```

## Drop:
```python
df.dropna()                    # drop rows with ANY null
df.dropna(subset=["Age"])      # drop rows where Age is null
df.drop(columns=["Cabin"])     # drop entire column
```

## Fill:
```python
df["Age"].fillna(df["Age"].mean())      # fill with mean
df["Age"].fillna(df["Age"].median())    # fill with median
df["Embarked"].fillna("S")             # fill with most common value
```

## Duplicates:
```python
df.duplicated().sum()    # count duplicates
df.drop_duplicates()     # remove duplicates
```

## Rename columns:
```python
df.rename(columns={"OldName": "NewName"})
```

## Change data type:
```python
df["Age"] = df["Age"].astype(int)
```
## Your task — clean the Titanic dataset:

1.Check null counts for all columns

2.Drop Cabin column — too many nulls

3.Fill Age nulls with median

4.Fill Embarked nulls with most frequent value

5.Verify no nulls remain with isnull().sum()

6.Drop any duplicate rows

7.Print shape before and after cleaning


# ⚠️ Architectural Note: Programmatic Imputation

## The Concept
In Machine Learning data pipelines, hardcoding values based on manual inspection is an anti-pattern. Code must be dynamic, robust, and capable of adapting to unseen data without human intervention.

## The Anti-Pattern (Hardcoding)
```python
df["Embarked"].fillna("S")
```
* **The Flaw:** This requires you to manually run `print(df["Embarked"])` and visually scan for the most frequent value. If the underlying dataset changes (e.g., a new port becomes more frequent), this hardcoded pipeline will silently inject false data into your model.

## The Production Standard (Dynamic)
```python
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```
* **The Mechanics:**
  1. `mode()` calculates the most frequent value automatically.
  2. `[0]` extracts the first string value from the resulting Pandas Series (handling potential multi-mode ties).
* **The Advantage:** This pattern works on *any* dataset, dynamically calculating the correct imputation value at runtime.

