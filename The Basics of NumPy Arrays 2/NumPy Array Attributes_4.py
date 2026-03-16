# First let’s discuss some useful array attributes. We’ll start by defining three random
# arrays: a one-dimensional, two-dimensional, and three-dimensional array. We’ll use
# NumPy’s random number generator, which we will seed with a set value in order to
# ensure that the same random arrays are generated each time this code is run

import numpy as np

x1 = np.random.randint(10,size=6) # on D arrray
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))

print(x1.ndim)
print(x2.shape)
print(x3.size)
print(x3.dtype)
print(x3.itemsize)
print(x3.nbytes)