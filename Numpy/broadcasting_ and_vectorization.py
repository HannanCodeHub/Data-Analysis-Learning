import numpy as np

#perform operation on different array (large size) -> broadcasting
#without loops easily hojayeg and is faster .
#expand smaller -> larger
#1d -> 2d 

prices = np.array([100,200,300,450,780,960,1000])

discount = 15 

final_prices = prices - (prices * discount/100)

print(final_prices)

#how numpy handle different shape of arrays:

#single value:
arr = np.array([10,20,30])

print("expanding single elements:")
result = arr * 2 
print (result)

#1d to 2d array:
matrix = np.array([[1,2,3], [4,5,6]]) #2 x 3 matrix
vector = np.array([10,20,30]) #1d array

print("Matching dimensions:")
result2 = matrix + vector
print(result2)

#Incompatible shapes:
# inArray1 = np.array([[1,2,3], [4,5,6]]) 
# inArray2 = np.array([10,20]) 

# res = inArray1 + inArray2

# print(res) # error !!
# #can be solved by reshape.

#VECORIZATION:
#it is faster than loops for large data
#used for matrix and 100x faster than loops.

arr_v = np.array([10,20,30])
arr_v2 = np.array([1,2,3])

print("VECTORIZATION:")
result_v = arr_v + arr_v2
print(result_v)

multiplied = arr_v * 3 
print(multiplied)