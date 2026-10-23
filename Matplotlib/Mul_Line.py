import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 120, 150, 170, 200]
sales_2026 = [120, 140, 160, 190, 230]

plt.plot(months, sales_2025, marker="o", label="2025")
plt.plot(months, sales_2026, marker="s", label="2026")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison")

plt.legend()

plt.show()
#Siddhesh_67