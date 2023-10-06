# =============================================================================
# Basic If Statement
# =============================================================================
# Checks if x is greater than 5 and prints a message if true.
x = 10
if x > 5:
    print("x is greater than 5")

# =============================================================================
# If-Elif-Else Statement
# =============================================================================
# Tests multiple conditions and executes the block where the first true 
# condition is encountered.
y = 20
if y > 30:
    print("y is greater than 30")
elif y > 10:
    print("y is greater than 10 but less than or equal to 30")
else:
    print("y is less than or equal to 10")

# =============================================================================
# Multiple Conditions in If
# =============================================================================
# Demonstrates using multiple conditions in a single if statement using 'or'.
if y == 20 or x == 10:
    print("Either y is 20 or x is 10 or both")
if y == 20 and x == 30: 
    print("Now y is 20 and x = 30 so this is printed")
# =============================================================================
# Nested If Statements
# =============================================================================
# Checks if z is greater than 10; if true, another if-else block inside checks 
# for an additional condition.
z = 15
if z > 10:
    print("z is greater than 10")
    if z > 20:
        print("z is also greater than 20")
    else:
        print("but, z is not greater than 20")

# =============================================================================
# Using Logical Operators
# =============================================================================
# 'and', 'or', and 'not' are used to compound or invert conditions.
a, b, c = 5, 10, 15
if a < b and b < c:
    print("Both conditions are True")

if a < b or b > c:
    print("At least one condition is True")

if not a > b:
    print("not reverses the result")

# =============================================================================
# Ternary Conditional Operator
# =============================================================================
# A shorthand for an if-else condition in a single line.
d = 30
result = "Even" if d % 2 == 0 else "Odd"
print(f"{d} is {result}")

# =============================================================================
# Chained Comparisons
# =============================================================================
# Python allows chained comparison, which is more readable.
if 0 < a < 10:
    print("a is a positive single-digit number")

# =============================================================================
# Nested Ternary Conditional Operator
# =============================================================================
# You can nest ternary conditional operators for more complex conditions.
e = 45
classification = "Positive" if e > 0 else "Negative" if e < 0 else "Zero"
print(f"{e} is {classification}")

# =============================================================================
# Using 'in' with If
# =============================================================================
# The 'in' keyword checks for membership in a list, tuple, set, or string.
if 'a' in 'apple':
    print("a is in apple")

# =============================================================================
# Pass Statement
# =============================================================================
# Sometimes you want an empty block; 'pass' allows you to do that.
if x > 100:
    pass  # TODO: implement this block

# =============================================================================
# Using Enumerate in Loop with If
# =============================================================================
# Enumerate can be used to get the index and the value in a loop.
my_list = [10, 20, 30, 40, 50]
for index, value in enumerate(my_list):
    if value == 30:
        print(f"Value 30 found at index {index}")

# =============================================================================
# Using 'break' and 'continue' with If
# =============================================================================
# 'break' exits the loop, 'continue' skips to the next iteration.
for value in my_list:
    if value == 30:
        break  # This will exit the loop immediately
    print(value)

for value in my_list:
    if value == 30:
        continue  # This will skip printing 30
    print(value)
