import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000,1500,1300,1800]

plt.plot(months, sales, color = "Blue", linestyle = "--" , linewidth = 2,marker = 'o', label = "2025 Sales Data")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Data Report")
plt.legend(loc = "upper left", fontsize = 12) #whats happening in data.
plt.grid(color = 'gray', linestyle = ':', linewidth = 1)
plt.xlim(1,4)
plt.ylim(0,2000)
plt.xticks([1,2,3,4], ["M1","M2","M3","M4"])

plt.show()