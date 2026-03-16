import numpy as np

# Create a length-10 integer array filled with zeros
zero_Array = np.zeros(10,dtype=int)
print(zero_Array)

# Create a 3x5 floating-point array filled with 1s 
onesArray = np.ones((3,5),dtype=float)
print(onesArray,type(onesArray))

# Create a 3x5 array filled with 3.14
full_Array = np.full((3,5),3.14)
print(full_Array)


# Create an array filled with a linear sequence
 # Starting at 0, ending at 20, stepping by 2
 # (this is similar to the built-in range() function)
range_Array = np.arange(0,20,2) # its is completley similer to the range function in python so you can apply the range concept here
print(range_Array)


 # Create an array of five values evenly spaced between 0 and 1
even_sapce_array = np.linspace(0,1,5)
print(even_sapce_array)


# Create a 3x3 array of uniformly distributed
 # random values between 0 and 1
random_Array = np.random.random((3,3))
print(random_Array)


# Create a 3x3 array of normally distributed random values
 # with mean 0 and standard deviation 1

normol_Array = np.random.normal(0,1,(3,3))
print(normol_Array)


 # Create a 3x3 array of random integers in the interval [0, 10)
r_int_array = np.random.randint(0,10,(3,3))
print(r_int_array)
#or
r2_int_array = np.random.normal(1,10,(4,5))
print(r2_int_array)


# Create a 3x3 identity matrix
identify_matrix = np.eye(3)
print(identify_matrix)


# Create an uninitialized array of three integers
 # The values will be whatever happens to already exist at that
 # memory location
empty_array = np.empty(3)
print(empty_array)



