"""
Exercise 03: Student Database - SOLUTION
========================================
"""

# Create list of student dictionaries
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "gpa": 3.8},
    {"name": "Bob", "age": 21, "major": "Mathematics", "gpa": 3.6},
    {"name": "Charlie", "age": 19, "major": "Physics", "gpa": 3.9}
]

# Display all students
print("=== Student Database ===")
print()
for i, student in enumerate(students, start=1):
    print(f"{i}. {student['name']} ({student['age']}) - {student['major']} - GPA: {student['gpa']}")

# Find student named 'Bob'
print("\nLooking up 'Bob':")
for student in students:
    if student["name"] == "Bob":
        print(f"  Name: {student['name']}")
        print(f"  Age: {student['age']}")
        print(f"  Major: {student['major']}")
        print(f"  GPA: {student['gpa']}")
        break

# Calculate average GPA
total_gpa = sum(student["gpa"] for student in students)
average_gpa = total_gpa / len(students)
print(f"\nAverage GPA: {average_gpa:.2f}")

# Find top student
top_student = max(students, key=lambda s: s["gpa"])
print(f"Top student: {top_student['name']} (GPA: {top_student['gpa']})")
