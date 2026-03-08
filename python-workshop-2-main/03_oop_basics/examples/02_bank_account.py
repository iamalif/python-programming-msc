"""
02 - Practical Example: Bank Account
====================================
A real-world example of using classes.

Run this file: python 02_bank_account.py
"""

class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, owner, balance=0):
        """
        Create a new bank account.

        Args:
            owner: Account owner's name
            balance: Starting balance (default 0)
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance:.2f}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive!")

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def display_info(self):
        """Display account information."""
        print(f"Account Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")


# Using the BankAccount class
print("=== Bank Account Demo ===")
print()

# Create two accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob")  # Using default balance of 0

# Display initial state
print("Initial accounts:")
alice_account.display_info()
print()
bob_account.display_info()

# Perform transactions
print()
print("=== Transactions ===")
print()

alice_account.deposit(500)
alice_account.withdraw(200)
alice_account.withdraw(2000)  # Not enough funds

print()

bob_account.deposit(1000)
bob_account.withdraw(300)

# Final state
print()
print("=== Final Balances ===")
print()

print(f"Alice: ${alice_account.get_balance():.2f}")
print(f"Bob: ${bob_account.get_balance():.2f}")
