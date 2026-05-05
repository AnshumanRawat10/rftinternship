"""
DAY 20 - CAPSTONE PROJECT (FULL EDA PIPELINE)
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: CREATE DATASET
# -----------------------------
data = {
    "Date": pd.date_range(start="2024-01-01", periods=12, freq='ME'),
    "Product": ["A","B","C","A","B","C","A","B","C","A","B","C"],
    "Region": ["North","South","East","West","North","South","East","West","North","South","East","West"],
    "Sales": [200, 150, 300, 250, 400, 350, 450, 500, 550, 600, 650, 700]
}

df = pd.DataFrame(data)

print("\nOriginal Data:\n", df)

# -----------------------------
# STEP 2: DATA CLEANING
# -----------------------------
# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# (No missing here, but example)
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# -----------------------------
# STEP 3: ANALYSIS
# -----------------------------

# Total Sales per Product
product_sales = df.groupby("Product")["Sales"].sum()

# Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum()

# Monthly Trend
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nSales by Product:\n", product_sales)
print("\nSales by Region:\n", region_sales)

# -----------------------------
# STEP 4: VISUALIZATION
# -----------------------------

# Line Chart (Trend)
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Chart (Top Products)
plt.figure()
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Bar Chart (Region-wise)
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# -----------------------------
# STEP 5: INSIGHTS
# -----------------------------
print("\nINSIGHTS:")
print("- Sales are increasing over time (positive trend).")
print("- Product C generates highest revenue.")
print("- Certain regions perform better than others.")
print("- Business can focus on high-performing products & regions.")

# -----------------------------
# BONUS: BEST REGION
# -----------------------------
best_region = region_sales.idxmax()
print("\nBest Performing Region:", best_region)