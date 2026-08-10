import numpy as np

#1d array:
arr_1d = np.array([1,2,3,4,5])
print("1d array:")
print(arr_1d)

#2d array:
arr_2d = np.array([[1,2,3],
          [4,5,6],
          [7,8,9] ])

print("\n2d array:")
print(arr_2d)

#multi dimensial array:
#matrix:
matrix = np.array([[1,2,3],
                  [10,25,40]])

print("\nMatrix:")
print(matrix)    

#fill array with default values(zeros):
zeros_array = np.zeros(3)
print("\nzeros array:")
print(zeros_array)

#fill array with default values(one):
ones_array = np.ones((3,3))
print("\nones array:")
print(ones_array)

#fill array with default values:
fill_array = np.full((3,3),8)
print("\nfull array:")
print(fill_array)

#creating sequences of numbers in numpy:
arr = np.arange(1,20,3)
print("\nsequence array:")
print(arr)

#creating identity matrices:
identity_matrix = np.eye(3)
print("\nidentity matrix:")
print(identity_matrix)

#to know about array size and shape:
array_ss = np.array([[1,2,3],
                    [10,25,40]])

print("\nShape:")
print(array_ss.shape)  

print("\nSize:")
print(array_ss.size)    

#to know about no. of dimenision (ndim):
arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print("\nDimensions:")
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

#type of array:
print("\ntype of array:")
print(arr_1d.dtype)

#change the type of array:
arr = np.array([1.2,3.4,5.99,6.7])
print("\n")
print(arr)
print ("\nType before casting :")
print(arr.dtype)


print ("\nType after casting :")
arr_type = arr.astype(int)
print(arr_type.dtype)