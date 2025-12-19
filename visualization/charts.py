import csv
import matplotlib.pyplot as plt

grades = []

with open("data/students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        grades.append(int(row["grade"]))

plt.hist(grades)
plt.title("Student Grades Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()