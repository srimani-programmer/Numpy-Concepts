# working with the indexing concept in the numpy array

import numpy as np

# creating an array with indices()

sample_array = np.indices((5,3),dtype=np.int16)
print(sample_array)

# creating an data array

data_array = np.arange(100).reshape(10,10)
print(data_array)

# Indexing the data array

row,col = np.indices((2,6))
print(data_array[row,col])

# standard way of Indexing the array

print(data_array[2:5,3:6]) 

array1 = [[1,2,3,4,5,6],[7,5,6,8,92,22],[4,6,57,32,657,87],[11,22,33,44,55,66]]

data_array1 = np.array((array1),dtype=np.int16)

print(data_array1)

print(data_array1[0:3,2:5])