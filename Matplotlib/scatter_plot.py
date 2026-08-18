import matplotlib.pyplot as plt 

# hours_studied = [ 1,2,3,4,5]
# exam_scores = [20,40,60,70,90]

# plt.scatter(hours_studied, exam_scores , color = "green" , marker = '*', label = "Student Data")
# plt.xlabel ("hours studied")
# plt.ylabel("exam score")
# plt.title("Relationship bw studied hours & exam score")
# plt.legend()
# plt.grid(True)

# plt.show()

#for 2 groups :

plt.scatter([1,2,3,4,5],[50,55,60,70,85] ,color = "green" , marker = 'o', label = "Class A") #g1
plt.scatter([1,2,3,4,5],[70,75,80,90,95] ,color = "blue" , marker = 'o', label = "Class B") #g2

plt.xlabel ("hours studied")
plt.ylabel("exam score")
plt.title("Comparison of two classes")
plt.legend()
plt.grid(True)

plt.show()