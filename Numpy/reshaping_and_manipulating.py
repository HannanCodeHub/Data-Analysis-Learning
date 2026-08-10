import numpy as np 

arr = np.array([1,2,3,4,5,6])

#reshape:
reshape_arr = arr.reshape(2,3)
print(reshape_arr)

#ravel()-> view and flatten()-> copy:

arr_2d = np.array([[1,2,3] , [4,5,6]])

print("\nRavel:")
print(arr_2d.ravel())

print("\nFlatten:")
print(arr_2d.flatten())

#insertion in array:
arrIn = np.array([1,2,3,4,5,6])
print("\n")
print(arrIn)
insert_arr = np.insert(arrIn, 2, 7)
print("\n")
print(insert_arr)

#insertion in 2d array:
arr_In2d = np.array([[1,2] , [3,4]])

insert_arr2d = np.insert(arr_In2d, 2, [5,6], axis = 0) #axis = 0 -> rows , axis = 1 -> column , axis = None -> single line 
print(insert_arr2d)

#append :
arrA = np.array([1,2,3,4,5])
new_arrA = np.append(arrA, [6,7,8,9,10])
print(new_arrA)

#concate:
arr0 = np.array([1,2,3])
arr0_1 = np.array([4,5,6])

new_array = np.concatenate((arr0,arr0_1))

print(new_array)

#removing elements from array:
deleted_arr = np.delete(arr0,2)
print(deleted_arr)

#Stacking:
arr_st1 = np.array([1,2,4])
arr_st2 = np.array([3,4,5])

print("\n VStack")
print(np.vstack((arr_st1, arr_st2)))

print("\n HStack")
print(np.hstack((arr_st1, arr_st2)))

#Splitting:
arr_Split = np.array([10,20,30,40,50,60])

print(np.split(arr_Split,3))