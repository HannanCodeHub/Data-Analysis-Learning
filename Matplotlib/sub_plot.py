import matplotlib.pyplot as plt 

# x = [1,2,3,4]
# y = [10,15,20,25]

# plt.subplot(1,2,1) #1row , 2col , 1st subplot
# plt.plot(x,y)
# plt.title("Line chart")

# plt.subplot(1,2,2) #1row , 2col , 1st subplot
# plt.bar(x,y)
# plt.title("pie chart")

# plt.show()

#Another method - Professional:

fig , ax = plt.subplots(1,2,figsize = (10,5), sharex= True)

x = [1,2,3,4]
y = [10,15,20,25]

ax[0].plot(x,y, color = 'blue')
ax[0].set_title("line plot")

ax[1].bar(x,y, color = 'green')
ax[1].set_title("bar plot")

fig.suptitle("Comparison of line and barchart")
plt.tight_layout()
plt.show()