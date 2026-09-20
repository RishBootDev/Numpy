import numpy as np


# in numpy the array is created using the np.array method with datatype int
#The difference between int8, int16, int32, and int64 in NumPy lies in the amount of memory each data type uses to store integers and the range of values they can represent.

arr_int = np.array([200, 201, 202], dtype=np.int16)
print(arr_int)

# similarly we have the float datatype
arr_float = np.array([1.0, 2.5, 3.8], dtype=np.float64)
print(arr_float)      # Output: [1.  2.5 3.8]


# and complex data type
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)
print(arr_complex)    # Output: 1.+2.j 3.+4.j]

# boolean data type in the numpy
arr_bool = np.array([True, False, True], dtype=np.bool_)
print(arr_bool)     # Output: [True False True]

# Notice '_' in the syntax np.bool_