"""
Exercise 01: Test Score Analyzer
================================
Read test scores from a file and analyze them.

Your task:
1. Read scores from 'scores.txt'
2. Parse each line into name and score
3. Store in a dictionary
4. Calculate and display statistics

The file format is:
Name: Score

Expected output:
----------------
=== Test Scores ===

Alice: 92
Bob: 85
Charlie: 88
Diana: 95
Emma: 90

Statistics:
  Average: 90.0
  Highest: Diana (95)
  Lowest: Bob (85)
  Pass rate (>=60): 100.0%
"""

# TODO: Open and read the file 'scores.txt'
# Hint: Use 'with open("scores.txt", "r") as file:'

scores = {}

with open("scores.txt", "r") as file:
    for line in file:
        name, score_str = line.strip().split(":")
        scores[name.strip()] = int(score_str.strip())

#print(scores)

# TODO: Create a dictionary to store name:score pairs


# TODO: Parse each line
# Hint: Split by ':' and strip whitespace
# Example: "Alice: 92" -> name="Alice", score=92


# TODO: Display all scores
print("=== Test Scores ===")
print()

for name, score in scores.items():
    print(f"{name}: {score}")
print()

# TODO: Calculate statistics
# - Average score
# - Highest score with name
# - Lowest score with name
# - Pass rate (scores >= 60)


# TODO: Print statistics

'''
Statistics:
  Average: 90.0
  Highest: Diana (95)
  Lowest: Bob (85)
  Pass rate (>=60): 100.0%
'''

print("Statistics:")

all_scores = []
for name, score in scores.items():
    all_scores.append(score)

average = sum(all_scores) / len(all_scores)
sorted_all_scores = sorted(all_scores)

for name, score in scores.items():
    if score == sorted_all_scores[0]:
        lowest_scorer = name
    
    if score == sorted_all_scores[-1]:
        highest_scorer = name

passes = 0
for score in all_scores:
    if score >= 60:
        passes += 1

pass_rate = (passes*100)/len(all_scores)

print(f"Average: {average:.1f}")
print(f"Highest: {highest_scorer}: ({sorted_all_scores[-1]})")
print(f"Lowest: {lowest_scorer}: ({sorted_all_scores[0]})")
print(f"Pass rate (>=60): {pass_rate}%")