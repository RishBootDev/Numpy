import numpy as np


# in numpy the array is created using the np.array method with datatype int
#The difference between int8, int16, int32, and int64 in NumPy lies in the amount of memory each data type uses to store integers and the range of values they can represent.

arr_int = np.array([200, 201, 202], dtype=np.int16)
print(arr_int)