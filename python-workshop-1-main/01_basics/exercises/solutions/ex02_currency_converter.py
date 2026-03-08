"""
Exercise 02: Currency Converter - SOLUTION
==========================================
"""

# Define the exchange rate as a constant
EXCHANGE_RATE = 11.50  # 1 EUR = 11.50 SEK

# Print a header
print("=== SEK to EUR Converter ===")
print()

# Get the amount in SEK from the user
amount_sek = float(input("Enter amount in SEK: "))

# Calculate the amount in EUR
amount_eur = amount_sek / EXCHANGE_RATE

# Print the result with 2 decimal places
print(f"{amount_sek:.2f} SEK = {amount_eur:.2f} EUR")
