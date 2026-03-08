"""
04 - Choosing the Right Data Structure
======================================
When to use lists, tuples, or dictionaries?

Run this file: python 04_choosing_data_structures.py
"""

print("=== When to Use Each Data Structure ===")
print()

# Lists: Ordered collection that can change
print("--- LISTS ---")
print("Use when:")
print("  - Order matters")
print("  - You need to add/remove items")
print("  - You'll access items by position")
print()

# Example: Task list
todo_list = ["Buy groceries", "Study Python", "Exercise"]
print(f"Todo list: {todo_list}")
todo_list.append("Call mom")
print(f"After adding task: {todo_list}")
completed = todo_list.pop(0)
print(f"Completed '{completed}': {todo_list}")

# Tuples: Ordered collection that can't change
print()
print("--- TUPLES ---")
print("Use when:")
print("  - Order matters")
print("  - Data should NOT change")
print("  - Returning multiple values from function")
print()

# Example: Geographic coordinates
location = (59.3293, 18.0686)  # Stockholm
print(f"Stockholm coordinates: {location}")
print("These shouldn't change - tuple is perfect!")

def get_student_info():
    """Return student data that shouldn't be modified."""
    return "Alice", 20, "CS"  # Returns tuple

name, age, major = get_student_info()
print(f"Student: {name}, {age}, {major}")

# Dictionaries: Key-value lookups
print()
print("--- DICTIONARIES ---")
print("Use when:")
print("  - You need fast lookup by name/key")
print("  - Data is best described as key-value pairs")
print("  - Order doesn't matter (or Python 3.7+ preserves it)")
print()

# Example: Student records
students = {
    "S001": {"name": "Alice", "grade": 92},
    "S002": {"name": "Bob", "grade": 85}
}

print("Student records:")
for student_id, info in students.items():
    print(f"  {student_id}: {info['name']} - {info['grade']}")

# Quick lookup
print(f"\nLookup S001: {students['S001']['name']}")

# Comparison example
print()
print("=== Same Data, Different Structures ===")
print()

# Student data as list (access by position)
student_list = ["Alice", 20, "Computer Science", 3.8]
print(f"As list: {student_list}")
print(f"Name (position 0): {student_list[0]}")

# Student data as tuple (immutable)
student_tuple = ("Alice", 20, "Computer Science", 3.8)
print(f"As tuple: {student_tuple}")
print(f"Name (position 0): {student_tuple[0]}")

# Student data as dictionary (descriptive keys)
student_dict = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"As dict: {student_dict}")
print(f"Name (by key): {student_dict['name']}")

print()
print("Dict is most readable and flexible!")

# Combining data structures
print()
print("=== Combining Data Structures ===")
print()

# List of dictionaries - common pattern!
class_roster = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 88}
]

print("Class roster (list of dicts):")
for student in class_roster:
    print(f"  {student['name']}: {student['grade']}")

# Calculate average
total = sum(student["grade"] for student in class_roster)
average = total / len(class_roster)
print(f"Class average: {average:.1f}")
