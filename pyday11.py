import matplotlib.pyplot as plt

# Dataset
dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Plot line chart
plt.figure()
plt.plot(dates, sales, marker='o')

# Highlight highest and lowest
max_sale = max(sales)
min_sale = min(sales)

max_day = dates[sales.index(max_sale)]
min_day = dates[sales.index(min_sale)]

plt.scatter(max_day, max_sale)
plt.scatter(min_day, min_sale)

# Labels & Title
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Trend Over the Week")

# Show plot
plt.show()