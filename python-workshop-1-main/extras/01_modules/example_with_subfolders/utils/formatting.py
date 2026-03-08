"""
utils/formatting.py - Formatting helper functions
=================================================
"""

def format_currency(amount, symbol="$"):
    """Format a number as currency."""
    return f"{symbol}{amount:,.2f}"

def format_percentage(value):
    """Format a decimal as percentage."""
    return f"{value:.1%}"

def format_header(title, width=40):
    """Create a centered header."""
    return f"{'=' * width}\n{title:^{width}}\n{'=' * width}"
