import matplotlib.pyplot as plt

# Dataset
categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

# Highlight highest category
explode = [0.1 if i == max(expenses) else 0 for i in expenses]

# Create Pie Chart
plt.figure()
plt.legend(title="Categories", loc="best")
plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',   # percentage labels
    explode=explode,     # highlight highest
    startangle=90
)

# Title
plt.title("Expense Distribution")

# Equal aspect ratio for perfect circle
plt.axis('equal')

plt.show()