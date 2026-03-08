"""
Exercise 01: Student Grade Manager
==================================
Create a program to manage student grades using lists.

Your task:
1. Create a list of student names
2. Create a list of their grades
3. Add a new student
4. Calculate and display the class average
5. Find the highest and lowest grades

Expected output:
----------------
=== Class Grades ===

Alice: 92
Bob: 85
Charlie: 88
Diana: 95

After adding Emma (grade: 90):

Alice: 92
Bob: 85
Charlie: 88
Diana: 95
Emma: 90

Class average: 90.0
Highest grade: 95
Lowest grade: 85
"""

# TODO: Create a list of student names
students = ["Alif", "Upoma", "Rahib"]  # Replace with actual names

# TODO: Create a list of grades (in same order as students)
grades = [66, 77, 88]  # Replace with actual grades

# TODO: Print header
print("=== Class Grades ===")

# TODO: Display each student and their grade using a loop
# Hint: Use zip(students, grades) or range(len(students))
for student, grade in zip(students, grades):
    print(student, grade)

# TODO: Add a new student named "Emma" with grade 90
students.append("Emma")
grades.append(90)

# TODO: Print updated list
print(students)
print(grades)

# TODO: Calculate and print class average
# Hint: average = sum(grades) / len(grades)
average = sum(grades) / len(grades)
print(f"{average:.1f}")

# TODO: Find and print highest and lowest grades
# Hint: Use max() and min()
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest grade: {highest_grade}\nLowest grade: {lowest_grade}")

