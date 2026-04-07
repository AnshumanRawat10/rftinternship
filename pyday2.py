# Import libraries
import numpy as np
import pandas as pd

# Function to calculate average
def calculate_average(data):
    return np.mean(data)


# Function to find highest and lowest marks
def find_min_max(data):
    return np.max(data), np.min(data)


# Function to count students above average
def count_above_average(data, avg):
    return np.sum(data > avg)


# Function to calculate grade distribution
def grade_distribution(data):
    grades = {"A": 0, "B": 0, "C": 0, "Fail": 0}

    for mark in data:
        if mark >= 90:
            grades["A"] += 1
        elif mark >= 75:
            grades["B"] += 1
        elif mark >= 50:
            grades["C"] += 1
        else:
            grades["Fail"] += 1

    return grades

# Main Program
marks = np.array([85, 90, 78, 92, 88, 76, 95, 45, 67, 82])

# Create DataFrame
df = pd.DataFrame(marks, columns=["Marks"])

# Calculate average
avg = calculate_average(marks)
print("Average Marks:", avg)

# Find highest and lowest
highest, lowest = find_min_max(marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Count above average
above_avg = count_above_average(marks, avg)
print("Students Above Average:", above_avg)

# Grade distribution
grades = grade_distribution(marks)
print("Grade Distribution:", grades)