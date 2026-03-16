import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
        print(output)
        
#this is good for small numbers but not for large
values = np.random.randint(1,10,size=5)
compute_reciprocals(values)



# It takes several seconds to compute these million operations and to store the result!
# When even cell phones have processing speeds measured in Giga-FLOPS (i.e., bil‐
# lions of numerical operations per second), this seems almost absurdly slow. It turns
# out that the bottleneck here is not the operations themselves, but the type-checking
# and function dispatches that CPython must do at each cycle of the loop. Each time
# the reciprocal is computed, Python first examines the object’s type and does a
# dynamic lookup of the correct function to use for that type. If we were working in
# compiled code instead, this type specification would be known before the code exe‐
# cutes and the result could be computed much more efficiently
big_array = np.random.randint(1, 100, size=1000000)
compute_reciprocals(big_array)


