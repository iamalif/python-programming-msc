"""
Exercise 02: Currency Converter
===============================
Create a program that converts between SEK (Swedish Krona) and EUR.

Your task:
1. Ask the user for an amount in SEK
2. Convert it to EUR using the exchange rate
3. Display both amounts formatted nicely

Exchange rate: 1 EUR = 11.50 SEK

Example interaction:
--------------------
=== SEK to EUR Converter ===

Enter amount in SEK: 500
500.00 SEK = 43.48 EUR
"""

# TODO: Define the exchange rate as a constant
EXCHANGE_RATE = 11.50  # 1 EUR = 11.50 SEK

# TODO: Print a header
print("=== SEK to EUR Converter ===")
print()


# TODO: Get the amount in SEK from the user (remember to convert to float!)
amount_sek = float(input("Enter amount in SEK: "))


# TODO: Calculate the amount in EUR
amount_eur = amount_sek / EXCHANGE_RATE

# TODO: Calculate the amount in USD
EXCHANGE_RATE_USD = 8.92  # 1 EUR = 8.92 USD
amount_usd = amount_sek / EXCHANGE_RATE_USD


# TODO: Print the result with 2 decimal places
print(f"{amount_sek:.2f} SEK = {amount_eur:.2f} EUR")

print(f"{amount_sek:.2f} SEK = {amount_usd:.2f} USD")

