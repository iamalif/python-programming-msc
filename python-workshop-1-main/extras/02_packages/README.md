# Packages: Nested Module Structures

A **package** is a folder containing Python modules, organized hierarchically.

## Package vs Module

- **Module** = A single `.py` file
- **Package** = A folder with `__init__.py` and one or more modules

## Structure

```
my_package/
├── __init__.py      # Makes this folder a package (can be empty)
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

## Example: Science Package

This example shows a nested package structure:

```
science/
├── __init__.py
├── physics/
│   ├── __init__.py
│   └── display.py
├── chemistry/
│   ├── __init__.py
│   └── display.py
└── biology/
    ├── __init__.py
    └── display.py
```

## Import Syntax

```python
# Full path (verbose)
import science.physics.display
science.physics.display.show_info()

# With alias (cleaner)
import science.physics.display as phys
phys.show_info()

# Import specific function
from science.physics.display import show_info
show_info()
```

## Run the Example

```bash
cd extras/02_packages
python main.py
```
