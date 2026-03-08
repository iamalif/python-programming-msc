"""
04 - Practical: Activity Log
============================
Create a simple activity logging system.

Run this file: python 04_practical_log_file.py
"""

from datetime import datetime

def log_activity(activity, log_file="activity_log.txt"):
    """Add a timestamped activity to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {activity}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)

    print(f"Logged: {activity}")

def read_log(log_file="activity_log.txt"):
    """Read and display the activity log."""
    try:
        with open(log_file, "r") as file:
            print("=== Activity Log ===")
            print(file.read())
    except FileNotFoundError:
        print("No log file found yet.")

# Demo: Log some activities
print("=== Logging Activities ===")
print()

log_activity("Program started")
log_activity("User logged in")
log_activity("Data processed successfully")
log_activity("Report generated")
log_activity("Program ended")

print()

# Read the log
read_log()

# Bonus: Count total activities
print()
print("=== Log Statistics ===")
print()

with open("activity_log.txt", "r") as file:
    lines = file.readlines()
    print(f"Total activities logged: {len(lines)}")
    print(f"Most recent: {lines[-1].strip()}")
