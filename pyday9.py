import pandas as pd

# Sample Dataset
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, 35, 28, 22],
    "Salary": [60000, 45000, 70000, 48000]
}

df = pd.DataFrame(data)

# Filter Conditions
filtered_df = df[(df["Salary"] > 50000) & (df["Age"] < 30)]

# Display Results
print("\n📊 Filtered Data:\n")
print(filtered_df)

# BONUS: Save filtered data to new file
filtered_df.to_csv("filtered_data.csv", index=False)

print("\n✅ Filtered data saved to 'filtered_data.csv'")