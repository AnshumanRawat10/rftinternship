import pandas as pd

# Create DataFrame
data = {
    "Name": ["AMIT", "RIYA", "JOHN"],
    "Math": [80, 90, 60],
    "Science": [70, 88, 65],
    "English": [85, 92, 70]
}

df = pd.DataFrame(data)

# 1. Calculate Average Marks per Student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 2. Find Topper
topper = df.loc[df["Average"].idxmax()]

# 3. Count Students Above Overall Average
overall_avg = df["Average"].mean()
above_avg_count = df[df["Average"] > overall_avg].shape[0]

# BONUS 1: Add Grade Column
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

# BONUS 2: Subject-wise Average
subject_avg = df[["Math", "Science", "English"]].mean()

# Output
print("\n📊 Student Performance Dashboard:\n")
print(df)

print("\n🏆 Topper:")
print(topper["Name"], "with average =", topper["Average"])

print("\n📈 Students above average:", above_avg_count)

print("\n📚 Subject-wise Average:")
print(subject_avg)