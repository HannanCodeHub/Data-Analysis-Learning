import numpy as np

#np.isnan
arr = np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr)) #true means nan is in the value and false means there is some val

#replace nan value:
cleaned_arr = np.nan_to_num(arr, nan = 1)
print(cleaned_arr)

#handle infinite value:

arrayH = np.array([1,2,np.inf,4,5,-np.inf])
print(np.isinf(arrayH))

#replace it with a finite value:
cleaned_arrH = np.nan_to_num(arrayH, posinf=1000, neginf=-1000)

print(cleaned_arrH)