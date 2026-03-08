# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.

a = int(input('Give a number: '))
b = int(input('Give a number: '))

for number in range(a, b):
    square = number**2
    print(number, '\t', square)


