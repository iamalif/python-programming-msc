"""
Exercise 01: Grade Classifier - SOLUTION
========================================
"""

# Get the score from the user
score = int(input("Enter score (0-100): "))

# Determine the grade using if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Score: {score}")
print(f"Grade: {grade}")
