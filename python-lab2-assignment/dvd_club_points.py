# DVD Club Points Program
# This program calculates the points awarded to a customer based on the number of DVDs purchased in a month.
# Points are awarded as follows:
# - 0 DVDs: 0 points
# - 1 DVD: 2 points
# - 2 DVDs: 5 points
# - 3 DVDs: 10 points
# - 4 or more DVDs: 25 points

# Prompting the user to enter the number of DVDs purchased with input validations
while True:
    try:
        total_dvds = int(input("Enter the number of DVDs purchased this month: "))
        if total_dvds < 0:
            print("Number of DVDs cannot be negative. Please try again.")
        else:
            break  # Breaking only if the input is valid (non-negative integer)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Determining the points based on the total number of DVDs
if total_dvds == 0:
    points = 0  # No points for 0 purchases
elif total_dvds == 1:
    points = 2  # 2 points for 1 DVD
elif total_dvds == 2:
    points = 5  # 5 points for 2 DVDs
elif total_dvds == 3:
    points = 10  # 10 points for 3 DVDs
else:
    points = 25  # 25 points for 4 or more DVDs

# Displaying the points earned
print(f"You have earned {points} points.")