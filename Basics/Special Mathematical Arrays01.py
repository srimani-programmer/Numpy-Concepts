import numpy as np

# creating an empty n-dimensional array 
empty_array = np.empty((3,3))

# (no.of rows, no.of columns)

# Printing the empty array
print(empty_array)
print('\n')

empty_array1 = np.empty((2,3),dtype=np.float32)
print(empty_array1)

empty_array2 = np.empty((3,3),dtype=np.int32)
print(empty_array2)

# Empty arrays will produce some randomor garbage values, these arrays are useful for temporary operation in a program

# creating zero valued array

zerovalue_array = np.zeros((6,6),dtype=np.int32)
print(zerovalue_array)

# Creating the one valued array

onevalue_array = np.ones((4,5))
print(onevalue_array)

# by default the datatype for numericals is float64
print('The datatype for one valued array is:',onevalue_array.dtype)

# Generating random number array
# In random.random() we shouldn't pass dtype attribute.
randomnumber_array = np.random.random((3,4))
print(randomnumber_array)

# Printing the uniform random numbers

uniform_random = np.random.uniform(-6,6,(4,4))
print(uniform_random)


