import matplotlib.pyplot as plt
import numpy as np

# Bar Chart
students = ["AMIT", "RIYA", "JOHN"]
marks = [85, 92, 78]

plt.figure()
plt.bar(students, marks)

# Add values on bars
for i in range(len(students)):
    plt.text(students[i], marks[i], marks[i], ha='center')

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")

plt.show()


# ------------------ BONUS (Grouped Bar Chart) ------------------
math = [80, 90, 70]
science = [85, 92, 78]

x = np.arange(len(students))
width = 0.3

plt.figure()
plt.bar(x - width/2, math, width, label="Math")
plt.bar(x + width/2, science, width, label="Science")

plt.xticks(x, students)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Comparison")
plt.legend()

plt.show()