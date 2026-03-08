"""
01 - Hello Python: Your First Program
======================================
Learn how to display output and write comments.

Run this file: python 01_hello_python.py
"""

# This is a comment - Python ignores everything after #
# Comments help explain your code to others (and yourself!)

# The print() function displays text on the screen
print("Welcome to Python Programming!")

# You can print multiple lines
print("=================================")
print("Monthly Sales Report")
print("=================================")

# Print blank lines to add spacing
print()

# Print multiple items separated by spaces (default)
print("Report Date:", "January 2025")

# Use the 'sep' parameter to change the separator
print("Q1", "Q2", "Q3", "Q4", sep=" | ")

# Use the 'end' parameter to stay on the same line
print("Status:", end=" ")
print("Complete")

# Multi-line strings use triple quotes
print("""
This is a multi-line string.
Useful for longer text blocks.
Each line break is preserved.
""")
