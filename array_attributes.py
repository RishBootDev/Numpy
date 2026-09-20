import numpy as np

#size - returns number of elements in the array
num = np.array([1, 2, 3])
print(num.size)     # Output - 3

#dtype - returns data type of elements in the array

num = np.array([1, 2, 3])
print(num.dtype)     # Output - int64

#itemsize - returns the size (in bytes) of each elements in the array

num = np.array([1, 2, 3, 4, 5], dtype=np.int16)
print(num.itemsize)  # Output - 2

#Accessing elements in arrays follows 0 based indexing

arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[2])  # Output: 30

#Negative indices count from the end of the array.

arr = np.array([10, 20, 30, 40, 50])
print(arr[-3])    # Output: 30

#You can use indexing to modify specific elements in an array.
arr = np.array([10, 20, 30, 40, 50])
arr[2] = 100
print(arr)  # Output: [ 10  20 100  40  50]