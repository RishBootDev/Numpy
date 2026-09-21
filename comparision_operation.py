import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

print(array1 > array2)      # Output - [False False False  True  True]
print(array1 < array2)      # Output - [ True  True False False False]
print(array1 == array2)     # Output - [False False  True False False]

# so basically the operation on arrays in python signifies the operation at elements present at the common index of both the array


arr1 = np.array([[ 1,  2,  3], [ 4,  5,  6]])
arr2 = np.array([[ 4,  5,  6], [ 1,  2,  3]])

# Example with 2d array

print(arr1 >= arr2)
print(arr1 != arr2)