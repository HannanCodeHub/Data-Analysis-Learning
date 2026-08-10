import numpy as np 

arr = np.array([10,20,30,40,50])

#Indexing:
print(arr[0]) #10
print(arr[2]) #30

#Slicing:

print(arr[0:2]) #10,20
print(arr[:4]) #10,20,30,40
print(arr[::2]) #10,30,50
print(arr[::-1]) #reverse it : 50,40,30,20,10

#Fancy Indexing:
arr1 = np.array([10,20,30,40,50,60,70])
print(arr1[[0, 2, 4]]) #10 , 30 , 50

#filtering data (boolean):
print(arr1[arr1 > 30]) #30,40,50,60,70