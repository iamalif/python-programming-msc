"""
01 - Lists: Ordered Collections
================================
Lists are mutable (changeable) sequences that can hold any type of data.

Run this file: python 01_lists.py
"""

# Creating lists
print("=== Creating Lists ===")
print()

# Empty list
empty = []

# List of student names
students = ["Alice", "Bob", "Charlie", "Diana"]

# List of test scores
scores = [85, 92, 78, 95, 88]

# Mixed types (though usually avoid this)
mixed = ["Alice", 25, True, 3.14]

print(f"Students: {students}")
print(f"Scores: {scores}")

# Accessing elements (zero-indexed!)
print()
print("=== Accessing Elements ===")
print()

print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")  # Negative index from end
print(f"Second score: {scores[1]}")

# Slicing - get a range of elements
print()
print("=== Slicing ===")
print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"All numbers: {numbers}")
print(f"First 3: {numbers[0:3]}")      # Index 0, 1, 2 (not including 3)
print(f"Last 3: {numbers[-3:]}")       # Last 3 elements
print(f"Middle: {numbers[3:7]}")       # Index 3, 4, 5, 6
print(f"Every 2nd: {numbers[::2]}")    # Step by 2

# Modifying lists
print()
print("=== Modifying Lists ===")
print()

grades = ["A", "B", "C", "B", "A"]
print(f"Original: {grades}")

# Change an element
grades[2] = "A"
print(f"After changing index 2: {grades}")

# Add to end
grades.append("B")
print(f"After append: {grades}")

# Insert at position
grades.insert(1, "A+")
print(f"After insert at index 1: {grades}")

# Remove by value
grades.remove("B")  # Removes first occurrence
print(f"After removing 'B': {grades}")

# Remove by index
removed = grades.pop(2)
print(f"Removed '{removed}' at index 2: {grades}")

# Common list operations
print()
print("=== List Operations ===")
print()

inventory = ["laptop", "mouse", "keyboard", "monitor"]

print(f"Inventory: {inventory}")
print(f"Number of items: {len(inventory)}")
print(f"'mouse' in stock: {'mouse' in inventory}")
print(f"'printer' in stock: {'printer' in inventory}")

# Sorting
numbers = [42, 17, 98, 5, 33]
print(f"\nOriginal numbers: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# List comprehension (bonus - creates new list)
print()
print("=== List Comprehension ===")
print()

original = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in original]
print(f"Original: {original}")
print(f"Doubled: {doubled}")

# Practical example: Student roster
print()
print("=== Practical Example: Class Roster ===")
print()

roster = []
roster.append("Emma")
roster.append("Liam")
roster.append("Olivia")
roster.extend(["Noah", "Ava"])  # Add multiple at once

print(f"Class roster ({len(roster)} students):")
for i, student in enumerate(roster, start=1):
    print(f"  {i}. {student}")
