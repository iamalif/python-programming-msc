"""
02 - Writing Files
==================
Learn how to write data to text files.

Run this file: python 02_writing_files.py
"""

# Method 1: Write (overwrites existing file)
print("=== Writing to a File ===")
print()

with open("output.txt", "w") as file:  # "w" = write mode
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")
    file.write("Python file I/O is easy!\n")

print("Created 'output.txt'")

# Read it back to verify
with open("output.txt", "r") as file:
    print(file.read())

# Method 2: Append (adds to existing file)
print("=== Appending to a File ===")
print()

with open("output.txt", "a") as file:  # "a" = append mode
    file.write("This line was appended.\n")
    file.write("So was this one.\n")

print("Appended to 'output.txt'")

# Read again
with open("output.txt", "r") as file:
    print(file.read())

# Writing multiple lines at once
print("=== Writing Multiple Lines ===")
print()

lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("multi_line.txt", "w") as file:
    file.writelines(lines)

print("Created 'multi_line.txt'")

# Practical example: Save a list to file
print("=== Practical: Save Shopping List ===")
print()

shopping_list = ["Milk", "Bread", "Eggs", "Butter", "Coffee"]

with open("shopping_list.txt", "w") as file:
    file.write("=== Shopping List ===\n\n")
    for i, item in enumerate(shopping_list, start=1):
        file.write(f"{i}. {item}\n")

print("Created 'shopping_list.txt'")

# Read it back
with open("shopping_list.txt", "r") as file:
    print(file.read())
