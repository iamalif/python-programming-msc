"""
02 - Tuples: Immutable Collections
===================================
Tuples are like lists, but cannot be changed after creation.
Use tuples for data that shouldn't be modified.

Run this file: python 02_tuples.py
"""

# Creating tuples
print("=== Creating Tuples ===")
print()

# Tuple with parentheses
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Tuple without parentheses (also valid)
dimensions = 1920, 1080

# Single element tuple (note the comma!)
single = (42,)

print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Dimensions: {dimensions}")
print(f"Single element: {single}")

# Accessing tuple elements (same as lists)
print()
print("=== Accessing Elements ===")
print()

student_record = ("Alice", 20, "Computer Science", 3.8)
print(f"Student: {student_record}")
print(f"Name: {student_record[0]}")
print(f"Age: {student_record[1]}")
print(f"Major: {student_record[2]}")
print(f"GPA: {student_record[3]}")

# Tuple unpacking - assign to variables
name, age, major, gpa = student_record
print(f"\nUnpacked: {name}, {age} years old")

# Immutability - tuples cannot be changed
print()
print("=== Immutability ===")
print()

point = (5, 10)
print(f"Original point: {point}")

# This would cause an error:
# point[0] = 7  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
point = (7, 10)
print(f"New point (reassigned variable): {point}")

# Why use tuples?
print()
print("=== When to Use Tuples ===")
print()

# 1. Function returns multiple values
def get_min_max(numbers):
    """Return minimum and maximum as a tuple."""
    return min(numbers), max(numbers)

data = [45, 23, 67, 89, 12]
min_val, max_val = get_min_max(data)
print(f"Data: {data}")
print(f"Min: {min_val}, Max: {max_val}")

# 2. Fixed data structures
print()
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(f"Weekdays: {weekdays}")
print("These shouldn't change, so tuple is perfect!")

# 3. Dictionary keys (lists can't be keys, tuples can)
print()
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}
print(f"Location at (10, 20): {locations[(10, 20)]}")

# Common operations
print()
print("=== Tuple Operations ===")
print()

scores = (85, 92, 78, 95, 88)
print(f"Scores: {scores}")
print(f"Length: {len(scores)}")
print(f"Highest: {max(scores)}")
print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Count of 92: {scores.count(92)}")
print(f"Index of 78: {scores.index(78)}")

# Converting between lists and tuples
print()
print("=== Conversion ===")
print()

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_list} → {my_tuple}")

back_to_list = list(my_tuple)
print(f"Tuple to list: {my_tuple} → {back_to_list}")
