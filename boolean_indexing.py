import numpy as np

# Create a sample array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a boolean mask
mask = arr > 5

# Print the original array and the mask
print("Original array:", arr)
print("Boolean mask:  ", mask)

# Use the boolean mask to index the array
filtered_arr = arr[mask]

# Print the filtered array
print("Filtered array:", filtered_arr)

# You can also create and apply a mask in one step
even_numbers = arr[arr % 2 == 0]
print("Even numbers: ", even_numbers)