"""
Exercise 03: Student Database
=============================
Create a student database using a list of dictionaries.

Your task:
1. Create a list containing student dictionaries
2. Display all students
3. Find a student by name
4. Calculate average GPA
5. Find student with highest GPA

Each student should have: name, age, major, gpa

Expected output:
----------------
=== Student Database ===

1. Alice (20) - Computer Science - GPA: 3.8
2. Bob (21) - Mathematics - GPA: 3.6
3. Charlie (19) - Physics - GPA: 3.9

Looking up 'Bob':
  Name: Bob
  Age: 21
  Major: Mathematics
  GPA: 3.6

Average GPA: 3.77
Top student: Charlie (GPA: 3.9)
"""

# TODO: Create list of student dictionaries
students = [
    # Add student dictionaries here
    # Each dict should have: name, age, major, gpa
    {
        "Name": "Alice",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.8
    },
    {
        "Name": "Bob",
        "Age": 21,
        "Major": "Mathematics",
        "GPA": 3.6
    },
    {
        "Name": "Charlie",
        "Age": 19,
        "Major": "Physics",
        "GPA": 3.9
    }
]

# TODO: Display all students with numbering
print("=== Student Database ===")
print()

'''
1. Alice (20) - Computer Science - GPA: 3.8
2. Bob (21) - Mathematics - GPA: 3.6
3. Charlie (19) - Physics - GPA: 3.9
'''

for i, student in enumerate(students, start=1):
    print(f"{i}. {student["Name"]} ({student["Age"]}) - {student["Major"]} - GPA: {student["GPA"]}")
print()

# TODO: Find and display student named 'Bob'
# Hint: Loop through students, check if name matches
'''
Looking up 'Bob':
  Name: Bob
  Age: 21
  Major: Mathematics
  GPA: 3.6
'''
print("Looking up 'Bob':")
for student in students:
    if student["Name"] == "Bob":
        print(f"Name: {student["Name"]}")
        print(f"Age: {student["Age"]}")
        print(f"Major: {student["Major"]}")
        print(f"GPA: {student["GPA"]}")
        break
print()

# TODO: Calculate average GPA
# Hint: Sum all GPAs and divide by number of students
sum_GPA = 0
for student in students:
    sum_GPA = sum_GPA + student["GPA"]

ave_GPA = sum_GPA / len(students)

print(f"Average GPA: {ave_GPA:.2f}")
print()


# TODO: Find student with highest GPA
# Hint: Use max() with a key parameter or loop through
highest_student = ""
highest_GPA = 0
for student in students:
    if student["GPA"] > highest_GPA:
        highest_GPA = student["GPA"]
        highest_student = student["Name"]
print(f"Top student: {highest_student} (GPA: {highest_GPA})")
