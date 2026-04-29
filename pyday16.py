import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# SAMPLE DATASET
# -----------------------------
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
             "2024-01-06", "2024-01-07"],
    "Product": ["A", "B", "A", "C", "B", "A", "C"],
    "Region": ["North", "South", "East", "West", "North", "South", "East"],
    "Sales": [200, 150, None, 300, 250, 400, None]
}
df = pd.DataFrame(data)
# -----------------------------
# DATA CLEANING
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])
# Handle missing values (fill with mean)
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
# -----------------------------
# AGGREGATION
# -----------------------------
# Total sales per product
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
# Sales trend
daily_sales = df.groupby("Date")["Sales"].sum()
# -----------------------------
# VISUALIZATION
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(12,5))

# Line Chart (Sales Trend)
axes[0].plot(daily_sales.index, daily_sales.values, marker='o')
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Sales")

# Bar Chart (Top Products)
axes[1].bar(product_sales.index, product_sales.values)
axes[1].set_title("Top Products")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Total Sales")

plt.tight_layout()
plt.show()

# -----------------------------
# BONUS ANALYSIS
# -----------------------------
# Monthly Growth
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

# Best Performing Region
best_region = region_sales.idxmax()

# -----------------------------
# INSIGHTS
# -----------------------------
print("\n📊 Key Insights:\n")

print("1. Best Selling Product:", product_sales.idxmax())
print("2. Best Performing Region:", best_region)
print("3. Total Sales:", round(df["Sales"].sum(), 2))

print("\nMonthly Sales:\n", monthly_sales)