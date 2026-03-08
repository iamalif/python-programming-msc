# Extra Task: Code Analysis - Solve the Mystery

# String declared with seemingly random characters
s = "aPxytlthyonlfqunb"

# The slices below extract specific letters from string s
mystery = (
    s[1:4:2]                          # Slice with a step: start=1, stop=4, step=2: picks indices 1 and 3 which ends up as "Py"
    + s[6:8]                          # Simple slice: picks indices 6 and 7 which ends up as "th"
    + ('x' if not s else s[9:11])     # Conditional expression: if s were empty, use 'x'; since s is not empty, use s[9:11]: indices 9 and 10 which ends up as "on"
    + '\'s '                          # Literal string with an escaped apostrophe: "'s "
    + s[12:-1:2]                      # Slice with a negative stop and step: start=12, stop=-1 (i.e. index 16), step=2: picks indices 12 and 14 which ends up as "fu"
    + s[15]                           # Single character at index 15: "n"
)
# Concatenated result: "Py" + "th" + "on" + "'s " + "fu" + "n" → "Python's fun"

# Printing the final result — "Svaret är" is Swedish for "The answer is"
print(f'Svaret är: "{mystery}"')