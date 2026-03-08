"""
Exercise 01: Student Grade Manager - SOLUTION
=============================================
"""

# Create lists
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [92, 85, 88, 95]

# Print header
print("=== Class Grades ===")
print()

# Display each student and grade
for student, grade in zip(students, grades):
    print(f"{student}: {grade}")

# Add new student
students.append("Emma")
grades.append(90)

print()
print("After adding Emma (grade: 90):")
print()

for student, grade in zip(students, grades):
    print(f"{student}: {grade}")

# Calculate average
average = sum(grades) / len(grades)
print(f"\nClass average: {average:.1f}")

# Find highest and lowest
highest = max(grades)
lowest = min(grades)
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
