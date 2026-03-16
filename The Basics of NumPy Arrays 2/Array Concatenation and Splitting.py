# All of the preceding routines worked on single arrays. It’s also possible to combine
# multiple arrays into one, and to conversely split a single array into multiple arrays.
# We’ll take a look at those operations here

import numpy as np

"""⭐Concatenation of arrays⭐"""
# Concatenation, or joining of two arrays in NumPy, is primarily accomplished
# through the routines np.concatenate, np.vstack, and np.hstack. np.concatenate
# takes a tuple or list of arrays as its first argument, as we can see here:

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
z = np.array([11,12,13,14])
xyz = np.concatenate([x,y,z])
print(xyz)


# np.concatenate can also be used for two-dimensional arrays
Grid = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
con_Array = np.concatenate([Grid,Grid])
print(con_Array)


# For working with arrays of mixed dimensions, it can be clearer to use the np.vstack
# (vertical stack) and np.hstack (horizontal stack) functions

# A= np.array([1,2,3,4])
# Grid2 = np.array([[5,6,7,8],[9,10,11,12]]) # two d array
# # vertically stack the arrays
# vertically = np.stack(x,Grid2)
# print(vertically)



"""⭐Splitting of arrays⭐"""
# The opposite of concatenation is splitting, which is implemented by the functions
# np.split, np.hsplit, and np.vsplit. For each of these, we can pass a list of indices
# giving the split points:
print("===Split_Array===")
myFullArray = np.array([1,2,3,4,5,5,6,7,8])
mylist = x1,x2,x3 = np.split(myFullArray,[3,5])
for value in mylist:
    print(value)   # soory for this the for loop look cool here that's why used warna koyi use nahi he yaha par

grid3 = np.arange(16).reshape((4, 4))
print(grid3)
upper, lower = np.vsplit(grid3, [2])
print(upper)
print(lower)