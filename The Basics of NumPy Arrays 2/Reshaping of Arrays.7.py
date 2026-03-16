"""# Another useful type of operation is reshaping of arrays. The most flexible way of
# doing this is with the reshape() method. For example, if you want to put the num‐
# bers 1 through 9 in a 3×3 grid, you can do the following:"""
import numpy as np

print("===Normal array===")
Grid = np.arange(1,10)
print(Grid)
print("===Reshape_Array===")
Update_Grid = Grid.reshape(3,3)
print(Update_Grid)



"""Another common reshaping pattern is the conversion of a one-dimensional array
into a two-dimensional row or column matrix. You can do this with the reshape
method, or more easily by making use of the newaxis keyword within a slice opera‐
tion:"""
print("==My New Array==")
x = np.array([1,2,4])
# row vector via reshape
x.reshape(1,3)
print(x)
# row vector via newaxis
x[np.newaxis, :]
print(x)
# column vector via reshape
x.reshape((3, 1))
print(x)
# column vector via newaxis
x[:, np.newaxis]
print(x)