
# Recreate the flowchart example from the lecture slides

# Flowchart for the pay calculating program

# Start

# Get the number of hours worked
hours_worked = float(input("Enter the number of hours worked: "))

# Get the hourly pay rate
hourly_pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate the pay
pay = hours_worked * hourly_pay_rate

# Display the gross pay
print("The gross pay is $", pay)

# The print function is used to display output to the user. It can display
# strings, numbers, and other data types. In this example, the print function is
# used to display the gross pay to the user. The output is formatted as a string
# with the text "The gross pay is $" followed by the value of the pay variable.
# The print function can also be used to display multiple values by separating
# them with commas.

# Here are a few more advanced examples of using the print function:

# Display multiple values
x = 10
y = 20

# Display the values of x and y
print("The value of x is", x, "and the value of y is", y)

# Display the sum of x and y
print("The sum of x and y is", x + y)

# There is also a way to format the output using the format method. This allows
# you to insert variables into a string using curly braces {} and then pass the
# variables to the format method. Here is an example:

# Display the sum of x and y using the format method
print("The sum of x and y is {}. It is also possible to write like this!".format(x + y))

# End