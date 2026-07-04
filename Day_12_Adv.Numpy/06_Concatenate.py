
# 6.Create two 2x3 matrices. Concatenate them both horizontally and vertically.
import numpy as np


# ➡️ 1D Array
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# By reshaping the 1D arrays into 2D matrices (1 row, 3 columns) before concatenating,
# we give them an 'axis=1' (columns) so they can be stacked horizontally without crashing!

print(f" H.Concatenate: \n{np.concatenate([x.reshape(1,3), y.reshape(1,3)], axis = 1)}") # np.hstack([x,y])
print(f" V.Concatenate: \n{np.concatenate([x.reshape(1,3), y.reshape(1,3)], axis = 0)}\n-------------") # np.vstack([x,y])


#➡️ 2

# M1
a = np.arange(0,6)
b = np.arange(6,12)

#Reshape manually or can be done in 'np.concatenate([a.reshape(2,3), b.reshape(2,3)], axis = ? )'
a = a.reshape(2,3)
b = b.reshape(2,3)

print(f" H.Concatenate: \n{np.concatenate([a,b], axis = 1)}")  # np.hstack([a,b])
print(f" V.Concatenate: \n{np.concatenate([a,b], axis = 0)}")  # np.vstack([a,b])

#------------------------------------------------------

# M2

# Let's create two ACTUAL 2x3 matrices (2 rows, 3 columns) manually.
# Notice the double brackets [[ ]] which make it 2D!
x = np.array([[1, 2, 3], 
              [4, 5, 6]])

y = np.array([[7, 8, 9], 
              [10, 11, 12]])

# ---------------------------------------------------------
# HORIZONTAL (Axis 1) - Side by Side
# ---------------------------------------------------------
# x and y both have 2 rows. We are glued them together left-to-right.
print("--- Horizontal Stacking (Axis 1) ---")
print(np.concatenate([x, y], axis=1))
# This is EXACTLY the same as: print(np.hstack([x, y]))

print("\n") # Just printing a blank line for readability

# ---------------------------------------------------------
# VERTICAL (Axis 0) - Top to Bottom
# ---------------------------------------------------------
# We drop 'y' directly underneath 'x' like stacking bricks.
print("--- Vertical Stacking (Axis 0) ---")
print(np.concatenate([x, y], axis=0))
# This is EXACTLY the same as: print(np.vstack([x, y]))