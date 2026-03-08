# Modules: Organizing Code into Files

A **module** is simply a Python file (`.py`) that contains code you want to reuse.

## Why Use Modules?

1. **Organization** - Split large programs into manageable files
2. **Reusability** - Write once, import anywhere
3. **Maintainability** - Changes in one place affect all uses

## Examples

### Basic Import
See [example_basic/](./example_basic/) - Import a module from the same folder

### Importing from Subfolders
See [example_with_subfolders/](./example_with_subfolders/) - Import modules from nested folders

## Key Syntax

```python
# Import entire module
import my_module
my_module.my_function()

# Import with alias (shorter name)
import my_module as m
m.my_function()

# Import specific function
from my_module import my_function
my_function()

# Import from subfolder
import utils.helpers
utils.helpers.some_function()

# Import from subfolder with alias
import utils.helpers as h
h.some_function()
```
