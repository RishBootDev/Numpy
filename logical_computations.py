import numpy as np

# two boolean arrays
a = np.array([True, False, True, False])
b = np.array([True, True, False, False])

# logical AND operation
result = np.logical_and(a, b)
print("Logical AND:", result)

# logical OR operation
result = np.logical_or(a, b)
print("Logical OR:", result)

# logical NOT operation
result = np.logical_not(a)
print("Logical NOT:", result)

# logical XOR operation
result = np.logical_xor(a, b)
print("Logical XOR:", result)
