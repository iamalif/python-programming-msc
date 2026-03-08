"""
Exercise 02: Login System
=========================
Create a simple login system with limited attempts.

Your task:
1. Define the correct username and password (as constants)
2. Give the user 3 attempts to log in
3. After each failed attempt, show remaining attempts
4. Lock the account after 3 failed attempts

Correct credentials:
- Username: admin
- Password: secret123

Example (successful login):
---------------------------
=== Login System ===

Enter username: admin
Enter password: secret123
Login successful! Welcome, admin.

Example (failed attempts):
--------------------------
=== Login System ===

Enter username: admin
Enter password: wrong
Incorrect credentials. 2 attempts remaining.

Enter username: admin
Enter password: wrong
Incorrect credentials. 1 attempt remaining.

Enter username: admin
Enter password: wrong
Account locked. Too many failed attempts.
"""

# Constants
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "secret123"
MAX_ATTEMPTS = 3

# TODO: Print header
print("=== Login System ===")


# TODO: Initialize attempt counter
attempts = 0


# TODO: Create a while loop for login attempts
# Hint: Loop while attempts < MAX_ATTEMPTS
while attempts < MAX_ATTEMPTS:

    # TODO: Get username and password from user
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    # TODO: Check if credentials are correct
    # If correct: print success message and break
    # If wrong: increment attempts and show remaining
    if (username == CORRECT_USERNAME and password == CORRECT_PASSWORD):
        print("Login successful! Welcome, admin.")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. {MAX_ATTEMPTS-attempts} attempts remaining.")

# TODO: After the loop, check if account was locked (all attempts used)
if attempts == MAX_ATTEMPTS:
    print("Account locked. Too many failed attempts.")

