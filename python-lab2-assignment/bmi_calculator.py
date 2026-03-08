# BMI Calculator Program
# This program calculates the Body Mass Index (BMI) for a user.
# It uses the math module's pow method in the formula.
# BMI = weight / (height ** 2)
# Categories:
# - Underweight: BMI < 18.5
# - Normal weight: 18.5 <= BMI < 25
# - Overweight: 25 <= BMI < 30
# - Obesity: BMI >= 30

# Importing math module's pow method
import math

# Prompting the user to enter weight in kg with input validations
while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight <= 0:
            print("Weight must be positive. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")

# Prompting the user to enter height in meters with input validations
while True:
    try:
        height = float(input("Enter your height in meters: "))
        if height <= 0:
            print("Height must be positive. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for height.")

# Calculating BMI using math.pow
bmi = weight / math.pow(height, 2)

# Determining the category
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

# Displaying the BMI and category
print(f"Your BMI is {bmi:.2f}. You are {category}.")