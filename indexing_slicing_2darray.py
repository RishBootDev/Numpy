import numpy as np

# Creating a 4x5 array with values from 1 to 20
arr = np.arange(1, 21).reshape(4, 5)

# Solution as follows

# 1. Extract the element at the third row and fourth column
element = arr[2, 3]
print(element)  # Output: 14

# 2. Extract the entire first row
first_row = arr[0, :]
print(first_row)  # Output: [1 2 3 4 5]

# 3. Extract the entire last column
last_column = arr[:, 4]
print(last_column)  # Output: [ 5 10 15 20]

# 4. Extract a subarray containing the first three rows and the first two columns
subarray = arr[0:3, 0:2]
print(subarray)
