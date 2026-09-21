import numpy as np

# for 1d array
data = np.array([1, 1, 1, 4, 5, 6, 7, 8, 9, 10])

print(np.var(data))      # Output - 10.36
print(np.std(data))    # Output - 3.2186953878862163

# for 2d array 
import numpy as np

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

# Get the 2nd matrix
second_matrix = array_3d[1]

# Calculate variance and standard deviation
variance = np.var(second_matrix)
std_deviation = np.std(second_matrix)

print(variance)
print(std_deviation)