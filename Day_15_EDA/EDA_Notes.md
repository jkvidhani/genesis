# 📊 Day 15 — Pandas Filtering & Groupby
> Theory Notes for Revision

---

## 🔑 Core Functions

### `groupby()`
Groups rows by a column and applies an aggregation function on another column.
```python
df.groupby("column")["target"].mean()
df.groupby("column")["target"].agg(["mean", "min", "max"])
```
**When to use:** When you want to compare a metric across different categories.
Example: Average survival rate per gender, average fare per class. 

---

### `value_counts()`
Counts how many times each unique value appears in a column.
```python
df["column"].value_counts()                    # raw counts
df["column"].value_counts(normalize=True)      # as proportions (0.0 to 1.0)
```
**When to use:** When you want to understand the distribution of a categorical column.

---

### `sort_values()`
Sorts the entire DataFrame based on one or more column values.
```python
df.sort_values("column")                       # ascending (default)
df.sort_values("column", ascending=False)      # descending
df.sort_values(["col1", "col2"])               # sort by multiple columns
```

---

### `idxmax()` / `idxmin()`
Returns the **index label** of the maximum or minimum value — not the value itself.
```python
df.groupby("col")["target"].mean().idxmax()   # WHICH group has highest mean
df.groupby("col")["target"].mean().idxmin()   # WHICH group has lowest mean
```

**Key difference:**
- `.max()` → returns the maximum VALUE
- `.idxmax()` → returns the INDEX (label) of that maximum value

---

### Filtering with conditions
```python
df[df["column"] > value]                                    # single condition
df[(df["col1"] > val1) & (df["col2"] == val2)]             # AND condition
df[(df["col1"] > val1) | (df["col2"] == val2)]             # OR condition
```
---

## Task Completed:
1. What was the survival rate by gender?

2. What was the average fare paid by each passenger class?

3. Which passenger class had the highest survival rate?

4. What was the average age of survivors vs non-survivors?

5. How many passengers embarked from each port?

6. Find top 5 most expensive tickets

7. What percentage of male vs female passengers survived?

---

## ⚠️ Key Concepts

### `.mean()` on a binary column (0/1)
When a column contains only 0s and 1s, taking the mean gives you the **rate** automatically.
```python
df["Survived"].mean()   # gives survival rate e.g. 0.38 = 38% survived
```
No extra calculation needed — mean of binary = proportion of 1s.

---

### Chaining operations
You can chain multiple operations in one line:
```python
df.groupby("col")["target"].mean().idxmax()
# Step 1: groupby → groups data
# Step 2: mean() → calculates mean per group
# Step 3: idxmax() → finds which group has highest mean
```

---

### Outliers in numerical columns
An outlier is a value that is extremely far from the rest of the data.
- Detected by comparing to mean/median
- Can skew ML model predictions
- Common fixes: log transform, capping (winsorization), or dropping

---

## 📌 Common Mistakes

```python
# ❌ Wrong — idxmax directly on grouped Survived gives row index, not group
df.groupby("Pclass")["Survived"].idxmax()

# ✅ Correct — mean first, then idxmax to find which class
df.groupby("Pclass")["Survived"].mean().idxmax()

# ❌ Wrong — value_counts on a mean result is meaningless
df.groupby("Sex")["Survived"].mean().value_counts()

# ✅ Correct — multiply mean by 100 to get percentage
df.groupby("Sex")["Survived"].mean() * 100
```

---

## 🎯 ML Relevance

**Why groupby matters in ML:**
Before building any model you must understand how your target variable (what you're predicting) relates to your features (inputs). Groupby is how you measure that relationship for categorical features.

**Why value_counts matters in ML:**
Class imbalance — if 90% of your data is one class and 10% is another, your model will be biased. `value_counts()` reveals this instantly.

**Why sorting matters in ML:**
Identifying top/bottom values helps detect outliers and understand feature distributions before preprocessing.