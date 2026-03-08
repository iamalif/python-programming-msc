"""
utils/calculations.py - Business calculation functions
======================================================
"""

def calculate_tax(amount, rate=0.25):
    """Calculate tax on an amount."""
    return amount * rate

def calculate_discount(price, percent):
    """Calculate discounted price."""
    discount = price * (percent / 100)
    return price - discount

def calculate_profit_margin(revenue, cost):
    """Calculate profit margin as a decimal."""
    if revenue == 0:
        return 0
    profit = revenue - cost
    return profit / revenue
