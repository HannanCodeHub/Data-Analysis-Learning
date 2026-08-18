import matplotlib.pyplot as plt 

#it is used for continuos data:

scores = [35,40,23,45,67,88,90,91,94,78,74,64,50,52,33,23,35,89,23,17,64,72,80,99]

plt.hist(scores , bins = 5 , color = 'purple', edgecolor = 'black')
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.title("Score distribution of students")

plt.show()