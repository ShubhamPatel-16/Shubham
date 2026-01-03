import numpy as np     #In terminal: pip install numpy 
# print(np.__version__)

# my_list = [1,2,3,4,5]
# my_list = my_list * 4
# print(my_list)

# array = np.array([1,2,3,4])
# array = array * 5
# print(array)
# print(type(array))  # nd = N-dimention

# Mutidimentional array

# array = np.array([['A','B','C']
#                   ,['D','E','F']
#                  ,['G','H','I']])
# print(array.ndim)
# print(array.shape)

# array = np.array([[['A','B','C'], ['J','K','L']],
#                    ['D','E','F'],
#                  [['G','H','I']]])
# (LAYERS, ROWS, COLUMNS)  

# Slicing

# array = np.array([[],[],[],[],[]])
# array = np.array([[1,2,11,14],
#                  [3,4,12,16],
#                  [5,6,13,17],
#                  [15,7,8,18]])
# aarray [start:stop:step] (9:n+1:). // n(stop) is excluded
# print(array[-2])  // for row
# print(array[0:4:2])
# print(array[0,0])
# print(array[:,2])  # : = all rows selected, first column

#4 Scalar Arithmetics

array = np.array([1,2,3])
print(array + 4)    