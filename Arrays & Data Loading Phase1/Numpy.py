"""The ndarray"""

# A NumPy array is a fixed-type, contiguous block of memory.
# Every element sits right next to the next one — no pointers, 
# no boxing. That's why it's 10–100× faster than a Python list

import numpy as np


# python list: each element is a separate python object
my_list = [1, 2, 3, 4]  # 4 pointers == 4 objects


# NumPy array: one contiguous block
my_array = np.array([1, 2, 3, 4])


# The 4 things you should always check on a new array
print(f"Shape: {my_array.shape}")  # (4,) - 1D array
print(f"Dtype: {my_array.dtype}")  # int32 - element type
print(f"Number of dimensions: {my_array.ndim}")  # 1D array - number of Axis
print(f"Number of elements: {my_array.size}")  # 4 - number of elements


"""dtype"""

# NumPy infers dtype from your data
a = np.array([1, 2, 3, 4])  # int64 (integer)
b = np.array([1.1, 3.3, 4.3, 2.3])  # float64 (float)
c = np.array([True, False, True])  # boolean

# For sales data, always use float64 - you will need decimals
sales = np.array([45000, 52000, 48000], dtype=np.float64)
