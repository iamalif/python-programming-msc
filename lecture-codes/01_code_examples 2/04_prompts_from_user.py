
# Prompts from user

# The input function is used to get input from the user. It displays a prompt to
# the user and waits for the user to enter a value. The value entered by the
# user is returned as a string. You can convert the string to a different data
# type using the int, float, or other functions.

# Get the user's name
name = input("Enter your name: ")

# Print the user's name
print("Hello, " + name + "!") # Concatenation

# Get the user's age
age = int(input("Enter your age: ")) # Convert the input to an integer

# Print the user's age
print("You are", age, "years old.")

# Get the user's height
height = float(input("Enter your height in meters: ")) # Convert the input to a float

# Print the user's height
print("You are", height, "meters tall.")

# A whole sentance using all input above
print("Hello, " + name + "! You are " + str(age) + " years old and " + str(height) + " meters tall.")