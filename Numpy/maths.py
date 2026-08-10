import numpy as np

#mathematical operations:
arr = np.array([1,2,3])

print (arr)

print("\naddition:")
print(arr + 2 )

print("\nsubtraction:")
print(arr - 2 )

print("\nmultiplication:")
print(arr * 2  )

print("\nPower:")
print(arr ** 2 )

print("\nModulus:")
print(arr % 2 )

#Aggregation Function:
arr1 = np.array([10,20,30,40,50])

print(np.sum(arr1))
print(np.mean(arr1))
print(np.min(arr1))
print(np.max(arr1))
print(np.average(arr1))
print(np.std(arr1))
print(np.var(arr1))