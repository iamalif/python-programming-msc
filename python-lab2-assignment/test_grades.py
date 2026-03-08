# Test Average and Grade Program
# This program calculates the average of five test scores, as well as assign letter grades accordingly.

def calc_average(score1, score2, score3, score4, score5):
    # Accepting five test scores as arguments and returning the average.
    return (score1 + score2 + score3 + score4 + score5) / 5

def determine_grade(score):
    # Accepting a test score and returning the letter grade accordingly.
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Creating an empty list to store the scores
scores = []

# Prompting the user to enter five test scores with validations
for i in range(1, 6):
    while True:
        try:
            score = float(input(f"Enter test score {i}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Please try again.")
                continue
            scores.append(score)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Displaying each score and its grade.
for i, score in enumerate(scores, 1): # Index starting from 1 as defined in the second argument. This is for display purposes.
    grade = determine_grade(score)
    print(f"Test {i}: Score = {score}, Grade = {grade}")

# Calculating and displaying the average
average = calc_average(scores[0], scores[1], scores[2], scores[3], scores[4])
print(f"Average test score: {average:.2f}")