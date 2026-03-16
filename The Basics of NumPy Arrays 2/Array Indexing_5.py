# Array Indexing: Accessing Single Elements
# If you are familiar with Python’s standard list indexing, indexing in NumPy will feel
# quite familiar. In a one-dimensional array, you can access the i
# th value (counting from
# zero) by specifying the desired index in square brackets, just as with Python lists
import numpy as np 

myArray = np.random.randint(8,size=3)
myArray2 = np.random.randint(8,size=(2,3))
myArray3 = np.random.randint(8,size=(2,3,4))

# so now lets perform slicing on this 
print(myArray[0])
print(myArray2[1])
print(myArray3[0:4])


#this is little bit confuesing lets try with one d sample Array

Array = np.array([1,2,3,4,5,6,7,8,])

#now lets try on this

print(Array[0:4])
print(Array[1])
print(Array[4])

# it works same like python list 

# To index from the end of the array, you can use negative indices:
print(Array[-1])
print(Array[-3])


# In a multidimensional array, you access items using a comma-separated tuple of
# indices:

print(myArray2[0,0])
print(myArray2[1,1])