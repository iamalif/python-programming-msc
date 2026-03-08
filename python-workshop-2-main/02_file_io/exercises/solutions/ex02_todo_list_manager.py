"""
Exercise 02: Todo List Manager - SOLUTION
=========================================
"""

# Create initial todo list
todos = [
    "Buy groceries",
    "Study Python",
    "Exercise",
    "Call mom"
]

# Display original list
print("=== Original Todo List ===")
for i, task in enumerate(todos, start=1):
    print(f"{i}. {task}")

# Save to file
with open("todos.txt", "w") as file:
    for i, task in enumerate(todos, start=1):
        file.write(f"{i}. {task}\n")

print("\nSaved to 'todos.txt'")

# Read back from file
print("\n=== Reading from File ===")
with open("todos.txt", "r") as file:
    content = file.read()
    print(content)

# Add more tasks
todos.append("Finish homework")
todos.append("Clean room")

# Display updated list
print("=== After Adding Tasks ===")
for i, task in enumerate(todos, start=1):
    print(f"{i}. {task}")

# Save updated list
with open("todos.txt", "w") as file:
    for i, task in enumerate(todos, start=1):
        file.write(f"{i}. {task}\n")

print("\nUpdated 'todos.txt'")
