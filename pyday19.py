#DAY 19 - STOCK / TIME-SERIES ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# DATASET
# -----------------------------
data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq='D'),
    "Price": [100, 102, 101, 105, 110, 108, 115, 120, 118, 125]
}

df = pd.DataFrame(data)

# -----------------------------
# MOVING AVERAGE (3-day)
# -----------------------------
df["Moving_Avg"] = df["Price"].rolling(window=3).mean()

print("\nDataset with Moving Average:\n", df)

# -----------------------------
# IDENTIFY PEAKS & DROPS
# -----------------------------
max_price = df["Price"].max()
min_price = df["Price"].min()

peak_day = df[df["Price"] == max_price]
drop_day = df[df["Price"] == min_price]

print("\nPeak Price Day:\n", peak_day)
print("\nLowest Price Day:\n", drop_day)

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure()

plt.plot(df["Date"], df["Price"], marker='o', label="Price")
plt.plot(df["Date"], df["Moving_Avg"], linestyle='--', label="Moving Average")

plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# BONUS: VOLATILITY
# -----------------------------
volatility = df["Price"].std()
print("\nVolatility (Std Dev):", volatility)