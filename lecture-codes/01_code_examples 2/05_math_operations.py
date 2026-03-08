
# Math operations in Python

# Python supports several math operations that can be performed on numbers.

# Addition
x = 10
y = 20

# Add x and y
result = x + y

# Display the result
print("Addition:", result)

# Subtraction
x = 20
y = 10

# Subtract y from x
result = x - y

# Display the result
print("Subtraction:", result)

# Multiplication
x = 10
y = 20

# Multiply x and y
result = x * y

# Display the result
print("Multiplication:", result)

# Division
x = 20
y = 10

# Divide x by y
result = x / y

# Display the result
print("Division:", result)

# Floor division
x = 20
y = 10

# Divide x by y and round down to the nearest whole number
result = x // y

# Display the result
print("Floor division:", result)

# Modulus
x = 5
y = 2

# Get the remainder when x is divided by y
result = x % y

# Display the result
print("Modulus:", result) # Expected output: 1 since 5 divided by 2 is 2 with a remainder of 1

# Exponentiation
x = 2
y = 3

# Raise x to the power of y
result = x ** y

# Display the result
print("Exponentiation:", result) # Expected output: 8 since 2 raised to the power of 3 is
# 2 * 2 * 2 = 8

# Multi-line math operations

# You can perform multi-line math operations by breaking them up into multiple lines.

# Example: Calculate the area of a cone

# The formula for the area of a cone is:

# area = πr(r + s)

# where:
# - area is the area of the cone
# - π is the mathematical constant pi (approximately 3.14159)
# - r is the radius of the base of the cone
# - s is the slant height of the cone

# Given the values of r and s, we can calculate the area of the cone.

# Define the values of r and s
r = 5
s = 10

# Calculate the area of the cone
area = 3.14159 * \
    r * \
    (r + s)
    
# Display the area of the cone
print("Area of the cone:", area) # Expected output: 235.61925

# We can do the same with parentheses

# Calculate the area of the cone
area = 3.14159 * (
    r * (r + s)
)
