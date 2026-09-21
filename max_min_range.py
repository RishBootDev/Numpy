import numpy as np

data = np.array([12, 15, 7, 10, 18, 21])

minimum = np.min(data)     # Output - 7
maximum = np.max(data)     # Output - 21

# for the 2d array 

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

# update your code below

third = array_3d[2]

#print(np.max(array_3d))   # 27
#print(np.min(array_3d))   # 1

print(np.max(third))
print(np.min(third))