# Section 01: Python Basics

Learn the fundamental building blocks of Python programming.

## Learning Objectives

After this section, you will be able to:
- Display output using `print()`
- Store data in variables
- Get input from users
- Perform arithmetic calculations
- Format strings professionally using f-strings

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_hello_python.py](examples/01_hello_python.py) | First program | `print()`, comments, `sep`, `end` |
| [02_variables.py](examples/02_variables.py) | Storing data | Variables, types, naming conventions |
| [03_user_input.py](examples/03_user_input.py) | Getting input | `input()`, `int()`, `float()` |
| [04_arithmetic.py](examples/04_arithmetic.py) | Calculations | Operators, order of operations |
| [05_string_formatting.py](examples/05_string_formatting.py) | Formatted output | f-strings, decimal places, alignment |

## Exercises

Work on these in `exercises/starter/`. Check `exercises/solutions/` when done.

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_sales_report.py](exercises/starter/ex01_sales_report.py) | Create formatted sales summary | Variables, f-strings |
| [ex02_currency_converter.py](exercises/starter/ex02_currency_converter.py) | Convert SEK to EUR | Input, arithmetic |
| [ex03_profit_calculator.py](exercises/starter/ex03_profit_calculator.py) | Calculate profit metrics | All basics |
| [ex04_invoice_generator.py](exercises/starter/ex04_invoice_generator.py) | Generate an invoice | All basics combined |

## Key Concepts Summary

### print()
```python
print("Hello")                    # Basic output
print("A", "B", "C", sep="-")    # Custom separator: A-B-C
print("Same", end=" ")           # No newline at end
print("line")                    # Continues on same line
```

### Variables
```python
name = "Alice"        # String (text)
age = 25              # Integer (whole number)
price = 19.99         # Float (decimal)
is_active = True      # Boolean (True/False)

TAX_RATE = 0.25       # Constant (UPPERCASE by convention)
```

### User Input
```python
name = input("Enter name: ")           # Always returns string
age = int(input("Enter age: "))        # Convert to integer
price = float(input("Enter price: "))  # Convert to float
```

### f-strings
```python
name = "Alice"
price = 1234.567

print(f"Hello, {name}!")           # Hello, Alice!
print(f"Price: ${price:.2f}")      # Price: $1234.57
print(f"Big: ${price:,.2f}")       # Big: $1,234.57
print(f"{'Title':^20}")            # Center in 20 chars
```

---

*Next: [02_control_flow](../02_control_flow/) - Learn to make decisions and repeat actions*
