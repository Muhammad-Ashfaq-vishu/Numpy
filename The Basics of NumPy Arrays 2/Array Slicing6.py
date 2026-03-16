# Array Slicing: Accessing Subarrays
# Just as we can use square brackets to access individual array elements, we can also use
# them to access subarrays with the slice notation, marked by the colon (:) character.
# The NumPy slicing syntax follows that of the standard Python list; to access a slice of
# an array x, use this:
import numpy as np

# ⭐⭐⭐One-dimensional subarrays⭐⭐⭐
oneD = np.arange(11)
print(oneD)

print(oneD[0:5]) 
print(oneD[5:])
print(oneD[4:7])
#  every other element
print(oneD[::2])
print(oneD[::3])
print(oneD[::5])
#  every other element, starting at index 1
print(oneD[1::2])
# all elements, reversed
print(oneD[::-1])
print(oneD[5::-2])


# ⭐⭐⭐Multidimensional subarrays⭐⭐⭐
print("===This is twoD array===")
twoD = np.random.randint(10,size=(3,4))
print(twoD)

# two rows, three columns
print("===two rows and three columns")
print(twoD[:2,:3])

# all rows, every other column
print("====all rows, every other column===")
print(twoD[:3,::2])


#subarray dimensions can even be reversed together:
print(twoD[::-1,::-1])



# Accessing array rows and columns. One commonly needed routine is accessing single
# rows or columns of an array. You can do this by combining indexing and slicing,
# using an empty slice marked by a single colon (:):

# first column of twoD
print("==first column of twoD==")
print(twoD[:,2])

 # first row of twoD
print("== first row of twoD==")
print(twoD[0:,])


# Creating copies of arrays
print("==Orginal Arra==y")
first_Array = np.random.randint(7,size=(3,4))
print(first_Array)
print("==Copy Array==")
copy_Array = first_Array[:2,:2]
print(copy_Array)

# If we now modify this subarray, the original array is not touched:
copy_Array[0,0] = 42
print(copy_Array)