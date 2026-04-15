import pandas as pd

# Create DataFrame
data = {
    "Name": ["AMAN", "BHAVESH", "CHETAN", "DIPESH"],
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

# 1. Average Salary per Department
avg_salary = df.groupby("Dept")["Salary"].mean()

# 2. Highest Paid Employee per Department
highest_paid = df.loc[df.groupby("Dept")["Salary"].idxmax()]

# BONUS 1: Count Employees per Department
emp_count = df.groupby("Dept")["Name"].count()

# BONUS 2: Sort Departments by Average Salary
sorted_avg_salary = avg_salary.sort_values(ascending=False)

# Output
print("\n📊 Employee Salary Insights:\n")
print(df)

print("\n💰 Average Salary per Department:")
print(avg_salary)

print("\n🏆 Highest Paid Employee per Department:")
print(highest_paid)

print("\n👥 Employee Count per Department:")
print(emp_count)

print("\n📈 Departments Sorted by Avg Salary:")
print(sorted_avg_salary)