"""
Exercise 02: Login System - SOLUTION
====================================
"""

# Constants
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "secret123"
MAX_ATTEMPTS = 3

# Print header
print("=== Login System ===")
print()

# Initialize attempt counter
attempts = 0
logged_in = False

# Create a while loop for login attempts
while attempts < MAX_ATTEMPTS:
    # Get username and password from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if credentials are correct
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print(f"Login successful! Welcome, {username}.")
        logged_in = True
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Incorrect credentials. {remaining} attempt(s) remaining.")
            print()

# Check if account was locked
if not logged_in:
    print("Account locked. Too many failed attempts.")
