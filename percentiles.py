import numpy as np

data = np.array([1, 1, 1, 2, 2, 2, 2, 3, 3])

print(np.percentile(data, 25))
print(np.percentile(data, 50))
print(np.percentile(data, 75))

# for the 3d array 
array_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    
    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]],
    
    [[19, 20, 21],
     [22, 23, 24],
     [25, 26, 27]]
])

print(np.percentile(array_3d, 25))
print(np.percentile(array_3d, 50))
print(np.percentile(array_3d, 75))