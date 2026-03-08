"""
Exercise 01: Grade Classifier
=============================
Convert a numeric score to a letter grade.

Your task:
1. Ask the user for a score (0-100)
2. Determine the letter grade based on the scale below
3. Display the result

Grading scale:
- 90-100: A
- 80-89:  B
- 70-79:  C
- 60-69:  D
- Below 60: F

Example:
--------
Enter score (0-100): 85
Score: 85
Grade: B
"""

# TODO: Get the score from the user
score = int(input("Please share your score: "))


# TODO: Determine the grade using if-elif-else
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


# TODO: Print the result
print(f"Score = {score}")
print(f"Grade = {grade}")
