import numpy as np

#Basic slicing example

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2:6])  # Output: [2 3 4 5] - default step is 1

#Slicing without any start or stop values would function as follows

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[:5])  # Output: [0 1 2 3 4] - exclusive of stop index
print(arr[5:])  # Output: [5 6 7 8 9] - inclusive of start index

#Slicing with negative indices would function as follows

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[-4:])  # Output: [6 7 8 9] - inclusive of start index - last element is at index -1
print(arr[:-4])  # Output: [0 1 2 3 4 5] - exclusive of stop index -last element is at index -1
#Using step - both positive and negative

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[::2])     # Output: [0 2 4 6 8] - Slice the entire array with a step of 2
print(arr[7:1:-2])  # Output: [7 5 3] - Slice from index 7 to index 2 in reverse order