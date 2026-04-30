#DAY 17 - CUSTOMER SEGMENTATION ANALYSIS
import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------
# DATASET
# -----------------------------
data = {
    "Customer_ID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [22, 25, 30, 35, 28, 40, 50, 23, 31, 45],
    "Spending": [200, 500, 300, 700, 400, 1000, 1200, 150, 350, 900],
    "Visits": [5, 8, 6, 10, 7, 12, 15, 3, 6, 11]
}

df = pd.DataFrame(data)

# -----------------------------
# CREATE SPENDING SEGMENTS
# -----------------------------
def segment(spend):
    if spend >= 800:
        return "High"
    elif spend >= 400:
        return "Medium"
    else:
        return "Low"

df["Segment"] = df["Spending"].apply(segment)
print("\nCustomer Data:\n", df)

# -----------------------------
# IDENTIFY CUSTOMERS
# -----------------------------
high_value = df[df["Segment"] == "High"]
low_engagement = df[df["Visits"] < 5]

print("\nHigh Value Customers:\n", high_value)
print("\nLow Engagement Customers:\n", low_engagement)

# -----------------------------
# VISUALIZATION 1: Spending Distribution
# -----------------------------
plt.figure()
plt.hist(df["Spending"], bins=5)
plt.title("Spending Distribution")
plt.xlabel("Spending")
plt.ylabel("Count")
plt.show()

# -----------------------------
# VISUALIZATION 2: Segment Count
# -----------------------------
segment_counts = df["Segment"].value_counts()

plt.figure()
segment_counts.plot(kind='bar')
plt.title("Customer Segments")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.show()

# -----------------------------
# INSIGHTS
# -----------------------------
print("\nINSIGHTS:")
print("- High spending customers are fewer but contribute more revenue.")
print("- Low engagement users visit less and may need marketing attention.")
print("- Majority customers fall in Medium segment.")

# -----------------------------
# BONUS: BUSINESS STRATEGY
# -----------------------------
print("\nSUGGESTED STRATEGIES:")
print("- Offer premium services to High-value customers.")
print("- Give discounts/notifications to Low-engagement users.")
print("- Upsell Medium segment customers to increase revenue.")