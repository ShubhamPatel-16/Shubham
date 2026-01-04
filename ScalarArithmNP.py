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
# array = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10]])
# print(np.sum(array))        #sum of all elements
# print(np.mean(array))       #average of all elements 
# print(np.std(array))        #standard deviation of all elements
# print(np.argmax(array))   #index of maximum element

# print(np.sum(array, axis=0))      #sum of each column.   0 for column
# print(np.sum(array, axis=1))      #sum of each row       1 for row
# print(np.mean(array, axis=0))     #mean of each column

# 10 Sorting

# unsorted_array = np.array([3,1,4,2,5])
# sorted_array = np.sort(unsorted_array)
# print(sorted_array)
# print(unsorted_array)   #original array remains unchanged
# print(np.argsort(unsorted_array))  #indices that would sort the array

# multidim array sorting
# array = np.array([[3,1,4],
#                   [2,5,0]])
# # sorted_array = np.sort(array, axis=1)  #sort each row
# # print(sorted_array)
# # sorted_array = np.sort(array, axis=0)  #sort each column            
# # print(sorted_array) 

# print(np.argsort(array, axis=1))  #indices that would sort each row
# print(np.argsort(array, axis=0))  #indices that would sort each column

# 11 Filtering
# filtering = refer to process of selecting elements,
#             from array that match specific criteria
ages = np.array([[13,53,52,23,68,97,83],
                [15,73,92,64,18,19,17]])
teenagers = ages[ages <18]
adults = ages[(ages >=18) & (ages <65)]   #₹() & ()
SeniorCitizens = ages[ages >=65]
even = ages[ages %2 ==0]
print(teenagers)
print(adults)
print(SeniorCitizens)
print(even) 
# print(ages[0, ages[0,:] < 18])  #first row, all columns where age <18
# print(ages[1, ages[1,:] < 18])  #second row, all columns where age <18