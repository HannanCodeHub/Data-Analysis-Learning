import matplotlib.pyplot as plt

regions = ["north", "west", "south" , "east"]
revenue = [1000,1450,390,1700]

plt.pie(revenue , labels = regions , autopct ='%1.1f%%' ,colors = ["lightgreen","gold", "skyblue", "coral"])
plt.title("contribution by region")
plt.show()
