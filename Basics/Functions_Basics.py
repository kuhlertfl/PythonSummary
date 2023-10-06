# Python Functions Data Sheet with Detailed Explanations

# =============================================================================
# Normal Functions
# =============================================================================

# Basic Function
# A function that prints a string when called.
def basic_function():
    print("Hello, World!")

# Call the basic function
basic_function()

# -----------------------------------------------------------------------------

# Function with Parameters
# Takes 'name' as a parameter and prints a greeting.
def greet(name):
    print(f"Hello, {name}!")

# Call function with parameters
greet("Alice")

# -----------------------------------------------------------------------------

# Function with Default Parameters
# 'language' has a default value of "English".
def greet_with_language(name, language="English"):
    print(f"Hello, {name}! Language is {language}")

# Call function with default parameters
greet_with_language("Alice")  # Uses default language
greet_with_language("Alice", language="Spanish")  # Overrides default language

# -----------------------------------------------------------------------------

# Function with Return Value
# Takes two numbers, adds them, and returns the sum.
def add(a, b):
    return a + b

# Call function with return value
result = add(1, 2)
print(f"Result: {result}")

# -----------------------------------------------------------------------------

# Function with Multiple Return Values
# Takes two numbers, performs addition and subtraction, and returns both.
def calculate(a, b):
    return a + b, a - b

# Call function with multiple return values
sum_result, diff_result = calculate(5, 3)
print(f"Sum: {sum_result}, Difference: {diff_result}")

# -----------------------------------------------------------------------------

# Variable-Length Arguments (*args)
# Takes an arbitrary number of arguments and returns their sum.
def sum_all(*args):
    return sum(args)

# Call function with variable-length arguments
print(sum_all(1, 2, 3, 4))

# -----------------------------------------------------------------------------

# Variable-Length Keyword Arguments (**kwargs)
# Takes an arbitrary number of keyword arguments and prints them.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call function with variable-length keyword arguments
print_info(name="Alice", age=30)

# =============================================================================
# Lambda Functions
# =============================================================================

# Basic Lambda Function
# An anonymous function that squares its argument.
square = lambda x: x * x

# Use the lambda function
print(square(4))

# -----------------------------------------------------------------------------

# Lambda with Multiple Parameters
# Adds two numbers.
add_lambda = lambda a, b: a + b

# Use lambda with multiple parameters
print(add_lambda(1, 2))

# -----------------------------------------------------------------------------

# Lambda in List Comprehensions
# Squares each number in the range.
squared_numbers = [(lambda x: x * x)(x) for x in range(5)]
print(squared_numbers)

# -----------------------------------------------------------------------------

# Lambda in Higher-Order Functions (map, filter, reduce)
from functools import reduce

nums = [1, 2, 3, 4]

# Map: Applies the lambda to each element in 'nums'.
squared_nums = list(map(lambda x: x * x, nums))
print(squared_nums)

# Filter: Filters 'nums' to only include even numbers.
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

# Reduce: Aggregates 'nums' by summing them.
total = reduce(lambda x, y: x + y, nums)
print(total)

# =============================================================================
# Nested and Higher-Order Functions
# =============================================================================

# Nested Function
# 'outer_function' takes 'x' and defines 'inner_function' that takes 'y'.
# It returns 'inner_function'.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Use nested function
# 'new_func' now behaves like 'inner_function' with 'x' set to 10.
new_func = outer_function(10)
print(new_func(5))  # Output will be 15 (10 + 5)

# -----------------------------------------------------------------------------

# Higher-Order Function
# Takes a function ('func') and a value ('value'), and applies the function.
def apply_function(func, value):
    return func(value)

# Use higher-order function
# Applies 'square' function to 4.
print(apply_function(square, 4))

