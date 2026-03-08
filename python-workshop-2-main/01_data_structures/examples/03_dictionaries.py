"""
03 - Dictionaries: Key-Value Pairs
==================================
Dictionaries store data as key-value pairs for fast lookup.

Run this file: python 03_dictionaries.py
"""

# Creating dictionaries
print("=== Creating Dictionaries ===")
print()

# Empty dictionary
empty = {}

# Student record
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Product inventory
inventory = {
    "laptop": 15,
    "mouse": 45,
    "keyboard": 32
}

print(f"Student: {student}")
print(f"Inventory: {inventory}")

# Accessing values
print()
print("=== Accessing Values ===")
print()

print(f"Student name: {student['name']}")
print(f"Laptops in stock: {inventory['laptop']}")

# Safe access with .get() (doesn't crash if key missing)
print(f"Age: {student.get('age')}")
print(f"Phone: {student.get('phone', 'Not provided')}")  # Default value

# Adding and modifying
print()
print("=== Modifying Dictionaries ===")
print()

print(f"Before: {student}")

# Add new key
student["email"] = "alice@university.edu"
print(f"After adding email: {student}")

# Modify existing
student["gpa"] = 3.9
print(f"After GPA update: {student}")

# Remove key
del student["email"]
print(f"After removing email: {student}")

# Dictionary methods
print()
print("=== Dictionary Methods ===")
print()

grades = {"Alice": 92, "Bob": 85, "Charlie": 88, "Diana": 95}

print(f"Grades: {grades}")
print(f"Students: {list(grades.keys())}")
print(f"Scores: {list(grades.values())}")
print(f"All items: {list(grades.items())}")

# Looping through dictionaries
print()
print("=== Looping Through Dictionaries ===")
print()

print("Student grades:")
for name, grade in grades.items():
    print(f"  {name}: {grade}")

# Check if key exists
print()
print("=== Checking Keys ===")
print()

print(f"'Alice' in grades: {'Alice' in grades}")
print(f"'Eve' in grades: {'Eve' in grades}")

# Nested dictionaries
print()
print("=== Nested Dictionaries ===")
print()

students = {
    "student1": {
        "name": "Alice",
        "scores": [92, 88, 95]
    },
    "student2": {
        "name": "Bob",
        "scores": [85, 90, 87]
    }
}

print(f"All students: {students}")
print(f"Alice's scores: {students['student1']['scores']}")
print(f"Bob's name: {students['student2']['name']}")

# Practical example: Game inventory
print()
print("=== Practical Example: Game Inventory ===")
print()

player_inventory = {
    "gold": 1500,
    "health_potions": 3,
    "weapons": ["sword", "bow"],
    "armor": "iron_chest"
}

print("=== Player Inventory ===")
for item, value in player_inventory.items():
    print(f"{item}: {value}")

# Buy a health potion
player_inventory["health_potions"] += 1
player_inventory["gold"] -= 50
print(f"\nAfter buying potion:")
print(f"Gold: {player_inventory['gold']}")
print(f"Potions: {player_inventory['health_potions']}")
