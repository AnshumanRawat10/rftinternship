# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Style (makes graph look better)
sns.set_style("whitegrid")

# -----------------------------
# DATASET: Student Marks
# -----------------------------
marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 87, 90, 92, 95, 97, 100]

df = pd.DataFrame(marks, columns=['Marks'])

# -----------------------------
# HISTOGRAM WITH KDE CURVE
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(
    df['Marks'],
    bins=10,
    kde=True
)

# Mean & Median lines (this is what adds real value)
mean_val = df['Marks'].mean()
median_val = df['Marks'].median()

plt.axvline(mean_val, linestyle='--', label=f"Mean: {mean_val:.1f}")
plt.axvline(median_val, linestyle='-', label=f"Median: {median_val}")

# Labels and Title
plt.title("Distribution Analysis of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()

# -----------------------------
# IDENTIFY SKEWNESS
# -----------------------------
skewness = df['Marks'].skew()

print("\n📊 Skewness of Data:", round(skewness, 2))

# Better Interpretation
if skewness > 0:
    print("➡️ Positively Skewed (Right Tail Longer)")
elif skewness < 0:
    print("⬅️ Negatively Skewed (Left Tail Longer)")
else:
    print("⚖️ Approximately Symmetrical Distribution")