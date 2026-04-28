import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Style
sns.set_style("whitegrid")

# -----------------------------
# DATASET
# -----------------------------
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [200, 250, 300, 280, 350],
    "Students": ["Amit", "Riya", "John"],
    "Marks": [85, 92, 78]
}

df_sales = pd.DataFrame({
    "Day": data["Day"],
    "Sales": data["Sales"]
})

df_marks = pd.DataFrame({
    "Students": data["Students"],
    "Marks": data["Marks"]
})

# -----------------------------
# CREATE SUBPLOTS
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(18,5))

# -----------------------------
# 1. LINE CHART (Trend)
# -----------------------------
axes[0].plot(df_sales["Day"], df_sales["Sales"], marker='o')
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Sales")

# -----------------------------
# 2. BAR CHART (Comparison)
# -----------------------------
axes[1].bar(df_marks["Students"], df_marks["Marks"])
axes[1].set_title("Student Performance")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Marks")

# Add values on bars
for i in range(len(df_marks)):
    axes[1].text(df_marks["Students"][i], df_marks["Marks"][i], df_marks["Marks"][i], ha='center')

# -----------------------------
# 3. HISTOGRAM (Distribution)
# -----------------------------
sns.histplot(df_marks["Marks"], bins=5, kde=True, ax=axes[2])
axes[2].set_title("Marks Distribution")
axes[2].set_xlabel("Marks")

# -----------------------------
# FINAL TOUCH
# -----------------------------
plt.suptitle("Mini EDA Dashboard", fontsize=16)
plt.tight_layout()

plt.show()