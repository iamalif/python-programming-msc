"""
01 - Reading Files
==================
Learn how to read text files in Python.

Run this file: python 01_reading_files.py
"""

import os

# Get the directory where this script is located
script_dir = os.path.dirname(__file__)
# Build path to the data file
data_file = os.path.join(script_dir, "sample_data.txt")

# Method 1: Read entire file at once
print("=== Method 1: Read Entire File ===")
print()

file = open(data_file, "r")  # "r" = read mode
content = file.read()
file.close()  # Always close files!

print(content)

# Method 2: Read line by line
print()
print("=== Method 2: Read Line by Line ===")
print()

file = open(data_file, "r")
for line in file:
    print(line.strip())  # strip() removes newline characters
file.close()

# Method 3: Read all lines into a list
print()
print("=== Method 3: Read into List ===")
print()

file = open(data_file, "r")
lines = file.readlines()
file.close()

print(f"Total lines: {len(lines)}")
print(f"First line: {lines[0].strip()}")
print(f"Last line: {lines[-1].strip()}")

# Method 4: Using 'with' statement (RECOMMENDED!)
# Automatically closes the file
print()
print("=== Method 4: Using 'with' (Best Practice) ===")
print()

with open(data_file, "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here

# Practical example: Count words in file
print()
print("=== Practical: Word Count ===")
print()

with open(data_file, "r") as file:
    content = file.read()
    words = content.split()
    print(f"Total words: {len(words)}")
    print(f"Total characters: {len(content)}")

# Finding specific information
print()
print("=== Finding Specific Lines ===")
print()

with open(data_file, "r") as file:
    for line_num, line in enumerate(file, start=1):
        if "Python" in line:
            print(f"Line {line_num}: {line.strip()}")
