
# Magic numbers

# Magic numbers are numbers that are used in a program without explanation.
# They are called magic numbers because they seem to appear out of thin air,
# without any context or explanation. Magic numbers make code harder to read
# and understand, and they can lead to errors if the number is changed in one
# place but not in another.

# For example, consider the following code snippet:

# Calculate the area of a circle
radius = 5
area = 3.14159 * radius ** 2
print("The area of the circle is", area)

# In this code snippet, the number 3.14159 is a magic number. It is not clear
# where this number comes from or what it represents. To make the code more
# readable and maintainable, it is better to define this number as a constant
# with a meaningful name, like this:

# Define a constant for pi
PI = 3.141

# Calculate the area of a circle
radius = 5
area = PI * radius ** 2

# Display the area of the circle
print("The area of the circle is", area)