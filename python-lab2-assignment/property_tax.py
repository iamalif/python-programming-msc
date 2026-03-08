# Property Tax Calculator Program
# This program calculates the assessment value and property tax for a piece of property.
# Assessment value is 60% of the actual value.
# Property tax is 72¢ for each $100 of the assessment value. (Had to take this character "¢" from a Google search.)

# Declaring the constants using Python conventions
ASSESSMENT_RATE = 0.6  # 60% of the actual value
TAX_RATE = 0.0072  # 72 cents per $100 of the assessment value

# Prompting the user to enter the actual value of the property with input validations
while True:
    try:
        actual_value = float(input("Enter the actual value of the property: $"))
        if actual_value <= 0:
            print("Property value must be greater than zero. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the property value.")

# Calculating the assessment value (60% of actual value)
assessment_value = actual_value * ASSESSMENT_RATE

# Calculating the property tax (72¢ per $100 of assessment value)
property_tax = assessment_value * TAX_RATE

# Displaying the results
print(f"Assessment value: ${assessment_value:.2f}")
print(f"Property tax: ${property_tax:.2f}")