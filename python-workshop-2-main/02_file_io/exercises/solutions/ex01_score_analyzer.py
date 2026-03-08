"""
Exercise 01: Test Score Analyzer - SOLUTION
===========================================
"""

# Read and parse the file
scores = {}

with open("scores.txt", "r") as file:
    for line in file:
        # Split by ':' and strip whitespace
        name, score_str = line.strip().split(":")
        scores[name.strip()] = int(score_str.strip())

# Display all scores
print("=== Test Scores ===")
print()
for name, score in scores.items():
    print(f"{name}: {score}")

# Calculate statistics
average = sum(scores.values()) / len(scores)

highest_score = max(scores.values())
highest_name = [name for name, score in scores.items() if score == highest_score][0]

lowest_score = min(scores.values())
lowest_name = [name for name, score in scores.items() if score == lowest_score][0]

passing = sum(1 for score in scores.values() if score >= 60)
pass_rate = (passing / len(scores)) * 100

# Print statistics
print()
print("Statistics:")
print(f"  Average: {average:.1f}")
print(f"  Highest: {highest_name} ({highest_score})")
print(f"  Lowest: {lowest_name} ({lowest_score})")
print(f"  Pass rate (>=60): {pass_rate:.1f}%")
