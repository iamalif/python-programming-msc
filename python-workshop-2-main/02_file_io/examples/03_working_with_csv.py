"""
03 - Working with CSV Data
===========================
Reading structured data from comma-separated files.

Run this file: python 03_working_with_csv.py
"""

# Reading CSV manually (without csv module)
print("=== Reading CSV Data ===")
print()

with open("students.csv", "r") as file:
    # Read header
    header = file.readline().strip().split(",")
    print(f"Columns: {header}")
    print()

    # Read data rows
    students = []
    for line in file:
        values = line.strip().split(",")
        student = {
            "name": values[0],
            "age": int(values[1]),
            "major": values[2],
            "gpa": float(values[3])
        }
        students.append(student)

# Display students
print("Student Records:")
for student in students:
    print(f"  {student['name']}: {student['major']}, GPA {student['gpa']}")

# Calculate average GPA
average_gpa = sum(s["gpa"] for s in students) / len(students)
print(f"\nAverage GPA: {average_gpa:.2f}")

# Writing CSV data
print()
print("=== Writing CSV Data ===")
print()

# New students to add
new_students = [
    {"name": "Emma", "age": 19, "major": "Biology", "gpa": 3.85},
    {"name": "Frank", "age": 22, "major": "Chemistry", "gpa": 3.65}
]

with open("students_updated.csv", "w") as file:
    # Write header
    file.write("name,age,major,gpa\n")

    # Write all students (original + new)
    all_students = students + new_students
    for student in all_students:
        file.write(f"{student['name']},{student['age']},{student['major']},{student['gpa']}\n")

print("Created 'students_updated.csv' with 6 students")

# Verify
with open("students_updated.csv", "r") as file:
    print(file.read())
