import numpy as np
from scipy import special
# Introducing UFuncs
# For many types of operations, NumPy provides a convenient interface into just this
# kind of statically typed, compiled routine. This is known as a vectorized operation.
# You can accomplish this by simply performing an operation on the array, which will
# then be applied to each element. This vectorized approach is designed to push the
# loop into the compiled layer that underlies NumPy, leading to much faster execution


# Exploring NumPy’s UFuncs
# Array arithmetic
# NumPy’s ufuncs feel very natural to use because they make use of Python’s native
# arithmetic operators. The standard addition, subtraction, multiplication, and division
# can all be used:

x = np.arange(4)
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) # floor division
print("x ** 2 = ", x ** 2)
print("x % 2 = ", x % 2)




"""Operator Equivalent_ufunc Description
+ np.add      Addition (e.g., 1 + 1 = 2)
- np.subtract Subtraction (e.g., 3 - 2 = 1)
- np.negative Unary negation (e.g., -2)
* np.multiply Multiplication (e.g., 2 * 3 = 6)
/ np.divide   Division (e.g., 3 / 2 = 1.5)
 np.floor_divide Floor division (e.g., 3 // 2 = 1)
** np.power Exponentiation (e.g., 2 ** 3 = 8)
% np.mod Modulus/remainder (e.g., 9 % 4 = 1)"""



"""⭐Absolute value⭐"""
# Just as NumPy understands Python’s built-in arithmetic operators, it also understands
# Python’s built-in absolute value function:
y = np.array([1,-2,3,-5,3,3])
abs_avlue = abs(y)
print(abs_avlue)


# also we can use this method also 

f = ([2, 1, 0, 1, 2])
np.absolute(f)


# This ufunc can also handle complex data, in which the absolute value returns the
# magnitude:

v = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print(v)
my_New_value = abs(v)
print(my_New_value)




"""⭐⭐⭐Trigonometric functions⭐⭐⭐"""
# NumPy provides a large number of useful ufuncs, and some of the most useful for the
# data scientist are the trigonometric functions. We’ll start by defining an array of
# angles:

theta = np.linspace(0,np.pi,3)

print("the value of theta is",theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))


# The values are computed to within machine precision, which is why values that
# should be zero do not always hit exactly zero. Inverse trigonometric functions are also
# available:

x = [-1, 0, 1]
print("x = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))



"""⭐⭐⭐Exponents and logarithms⭐⭐⭐"""
# Another common type of operation available in a NumPy ufunc are the exponentials:
print("==Exponents and logarithms==")
x = [1, 2, 3]
print("x =", x)
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))

# The inverse of the exponentials, the logarithms, are also available. The basic np.log
# gives the natural logarithm; if you prefer to compute the base-2 logarithm or the
# base-10 logarithm, these are available as well:
print("==inverse of the exponentials==")
print("x =", x)
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))

# There are also some specialized versions that are useful for maintaining precision
# with very small input:
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))


"""⭐⭐⭐Specialized ufuncs⭐⭐⭐"""
# NumPy has many more ufuncs available, including hyperbolic trig functions, bitwise
# arithmetic, comparison operators, conversions from radians to degrees, rounding and
# remainders, and much more. A look through the NumPy documentation reveals a lot
# of interesting functionality.
# Another excellent source for more specialized and obscure ufuncs is the submodule 
# scipy.special. If you want to compute some obscure mathematical function on
# your data, chances are it is implemented in scipy.special. There are far too many
# functions to list them all, but the following snippet shows a couple that might come
# up in a statistics context:


z = [1,2,3,4,5]

print("gamma(x) =", special.gamma(z))
print("ln|gamma(x)| =", special.gammaln(z))
print("beta(x, 2) =", special.beta(z, 2))


"""⭐⭐⭐ Advanced Ufunc Features⭐⭐⭐"""
# Specifying output

myx = np.arange(5)
myy = np.empty(5)
np.multiply(myx,10,out=myy)
print(myy)
