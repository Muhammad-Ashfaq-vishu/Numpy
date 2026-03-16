# so sample we will start from importing numpy
import numpy as np

#  Creating Arrays from Python Lists
#integer Array
int_array = np.array([1,2,3,4,5,6,7])
print(int_array)

# If we want to explicitly set the data type of the resulting array, we can use the dtype
# keyword:
np_array = np.array([1,2,3,4,5,6],dtype='float32')
print(np_array)

 # nested lists result in multidimensional arrays
my_arr = np.array([range(i,i + 3) for i in [2,4,6]])
print(my_arr)

