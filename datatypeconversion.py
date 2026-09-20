import numpy as np

# Create an array of integers
int_array = np.array([1, 2, 3, 4, 5])

# Convert the integer array to a string array
str_array = int_array.astype(str)

print(int_array)     # Output - [1 2 3 4 5]
print(str_array)     # Output - ['1' '2' '3' '4' '5']

# create an array of integers
int_array = np.array([1, 2, 3, 4])

# convert data type of int_array to float
float_array = int_array.astype('float')

# print the arrays and their data types
print(int_array)     # Output - [1 2 3 4] 
print(float_array)   # Output - [1. 2. 3. 4.]