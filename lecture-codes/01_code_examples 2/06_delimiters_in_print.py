
# Delimiters in print function

# The print function can display multiple values by separating them with commas.
# By default, the print function separates the values with a space character.
# You can change the delimiter by passing the sep parameter to the print function.

# Example: Using different delimiters in the print function

# Define the values of x, y, and z

x = 10
y = 20
z = 30

# Display the values of x, y, and z with a space delimiter
print(x, y, z)

# Display the values of x, y, and z with a comma delimiter
print(x, y, z, sep=",")
# Expected output: 10,20,30

# Display the values of x, y, and z with a dash delimiter
print(x, y, z, sep="-")

# Display the values of x, y, and z with a newline delimiter
print(x, y, z, sep="\n")

# Display the values of x, y, and z with a tab delimiter
print(x, y, z, sep="\t")

# Display the values of x, y, and z with a custom delimiter
print(x, y, z, sep="***")