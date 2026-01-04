import numpy as np
#4 Scalar Arithmetics

# array = np.array([1,2,3])
# print(array + 4)    
# print(array **3) # power 3

#5 vector math functions

# array = np.array([1.03, 2.94, 3.021])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))  
# print(np.ceil(array))  

#Exerci=se

# radii = np.array([1,2,3])
# print(np.pi * radii ** 2)

#6 Element wise 

# array1 =  np.array([1,2,3])
# array2 =  np.array([4,5,6])

# print (array1 + array2).  #+-/*
# print (array1 ** array2)

#7 Comparison operators

# score = np.array([23,45,65,34,77])
# print(score >= 44)
# score[score>46] = 00
# print(score)

#8 broadcasting

# array1 = np.array([[1,2,3,4]
#                    [5,6,7,8]]) #1D array
# array2 = np.array([[1],[2],[3],[4]])  #2D array
# print(array1.shape)             #(row, col)      //both row and col may either be 1 or same number. For broadcasting to work    
# print(array2.shape)             #(row, col)
# print(array1 + array2)        both arrays are broadcasted to a common shape
# print(array1 * array2)

#9 Agregate Functions :
# Agregate Functions = summarize data and typically
#                      return a single value
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
# print(np.sum(array))        #sum of all elements
# print(np.mean(array))       #average of all elements 
# print(np.std(array))        #standard deviation of all elements
# print(np.argmax(array))   #index of maximum element

print(np.sum(array, axis=0))      #sum of each column
print(np.sum(array, axis=1))      #sum of each row
print(np.mean(array, axis=0))     #mean of each column

  