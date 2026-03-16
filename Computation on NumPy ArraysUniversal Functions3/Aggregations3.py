import numpy as np
"""Aggregations: Min, Max, and Everything in Between"""
# Often when you are faced with a large amount of data, a first step is to compute sum‐
# mary statistics for the data in question. Perhaps the most common summary statistics
# are the mean and standard deviation, which allow you to summarize the “typical” val‐
# ues in a dataset, but other aggregates are useful as well (the sum, product, median,
# minimum and maximum, quantiles, etc.)



"""Summing the Values in an Array"""
print("Summing the Values in an Array")
l = np.random.random(100)
Sum = sum(l)
print(Sum)


big_array = np.random.random(10000000)
mysum = sum(big_array)
othersum = np.sum(big_array)
print(mysum)
print(othersum)

# Be careful, though: the sum function and the np.sum function are not identical, which
# can sometimes lead to confusion! In particular, their optional arguments have differ‐
# ent meanings, and np.sum is aware of multiple array dimensions, as we will see in the
# following section.


"""Minimum and Maximum"""
print("Minimum and Maximum")
# Similarly, Python has built-in min and max functions, used to find the minimum value
# and maximum value of any given array:
Another_array = np.random.random(10000000)
print(min(Another_array))
print(max(Another_array))

# NumPy’s corresponding functions have similar syntax, and again operate much more
# quickly
print("NUMPY MIN AND MAX")
print(np.min(Another_array))
print(np.max(Another_array))


"""Multidimensional aggregates"""
print("Multidimensional aggregates")
# One common type of aggregation operation is an aggregate along a row or column.
# Say you have some data stored in a two-dimensional array:


m = np.random.random((3,4))
print(m)
print(m.sum())

# Aggregation functions take an additional argument specifying the axis along which
# the aggregate is computed. For example, we can find the minimum value within each
# column by specifying axis=0:
print(m.min(axis=0))
