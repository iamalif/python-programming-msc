# Maximum of Two Values Program
# This program defines a function to find the maximum among two user-provided numbers.

def evaluate_max(num1, num2):
    # Returning the greater of the two number values.
    if num1 > num2:
        return num1
    else:
        return num2

# Prompting the user to enter the first value with input validations
while True:
    try:
        value1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompting the user to enter the second value with input validations
while True:
    try:
        value2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Finding the maximum using the function
maximum = evaluate_max(value1, value2)

# Displaying the result
if value1 == value2:
    print(f"Both values are equal: {value1}")
else:
    print(f"The greater value is: {maximum}")