import matplotlib.pyplot as plt

product = ["A", "B", "C", "D"]
sales = [100,800,1500,450]

plt.hbar(product,sales, color = "Orange", label = "Sales 2026")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title('Product Sale Comparison')
plt.legend()
plt.show()