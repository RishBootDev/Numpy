import numpy as np


# direct functions from numpy for mean and median

data = np.array([1, 1, 1, 4, 5, 6, 7, 8, 9, 10])

print(np.mean(data))      # Output - 5.2
print(np.median(data))    # Output - 5.5

# mean and median if the array is 2d array
array1 = np.array([[4, 5, 6], [13, 16, 19]])

# np.mean() flattens the array [4, 5, 6, 13, 16, 19]
# Sum = 63, Count = 6 -> Mean = 63 / 6 = 10.5
print(np.mean(array1))    

# np.median() finds the middle value of the flattened sorted array
# Middle elements are 6 and 13 -> Median = (6 + 13) / 2 = 9.5
print(np.median(array1))
