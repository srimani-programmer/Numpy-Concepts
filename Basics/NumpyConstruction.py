import numpy as np

# General lists we can also stor heterogeneous collection of elements.
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [23,4,2,21,3,231,34,11,4,35,44,45]

print(type(list2))
print(type(list1))


# Creating numpy array by passing list as data.
np_array1 = np.array(list1,dtype = np.float64)

print(np_array1)

# dtype is used to determine the type of the datatype that has to be stored in the numpy array object.

np_array2 = np.array(list2,dtype = np.int32)

print(np_array2)

# printing the type of the object

print(type(np_array1))

print(type(np_array2))

# Determining the shape of the numpy array

print('Shape of the np_array1 is:',np_array1.shape)

print('Shape of the np_array2 is:',np_array2.shape)

# Knowing the size of the numpy array

print('size of the np_array1 is:',np_array1.size)
print('size of the np_array2 is:',np_array2.size)

# Knowing the dimensions of the array

print('Dimensions of the np_array1 is:',np_array1.ndim)
print('Dimensions of the np_array2 is:',np_array2.ndim)

# knowing the size of the item in an numpyarray

print('Size of an item in np_array1 is:',np_array1.itemsize)
print('Size of an item in np_array2 is:',np_array2.itemsize)

a1 = np.array([12.5,34,56.65,78.983,90.323232])
a2 = np.array([123,456,9873,5455,7534,44343,443,232,655,987,1232,34,43443])

# in the above array we didn't mention about datatype explicitly, if we want to know the datatype then

print('The datatype of a1 numpyarray is:',a1.dtype)
print('The datatype of a2 numpyarray is:',a2.dtype)










