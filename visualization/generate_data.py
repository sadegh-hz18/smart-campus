import csv
import random
import os

# اگر پوشه data نبود، بساز
os.makedirs("data", exist_ok=True)

# ساخت فایل CSV
with open("data/students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "grade"])
    for i in range(100):
        writer.writerow([i + 1, random.randint(10, 20)])

print("students.csv created successfully")