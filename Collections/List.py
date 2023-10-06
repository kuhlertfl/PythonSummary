# =============================================================================
# Python List Data Sheet
# =============================================================================

# Lists in Python are ordered, mutable, and versatile data structures
# capable of storing multiple items of different data types.

# =============================================================================
# Basic List Declaration and Operations
# =============================================================================

# Declare a list
my_list = [1, 2, 3, 4]

# Access list elements
first_element = my_list[0]  # Output will be 1

# Modify a list element
my_list[1] = 20  # The list becomes [1, 20, 3, 4]

# Declare a list with mixed data types
mixed_list = [1, 'apple', 3.14]

# =============================================================================
# Common List Methods
# =============================================================================

# 1. append(item)
# Adds an item to the end of the list.
my_list.append(5)  # List becomes [1, 20, 3, 4, 5]

# 2. extend(iterable)
# Extends the list by appending elements from an iterable.
my_list.extend([6, 7])  # List becomes [1, 20, 3, 4, 5, 6, 7]

# 3. insert(index, item)
# Inserts an item at the given index.
my_list.insert(0, 0)  # List becomes [0, 1, 20, 3, 4, 5, 6, 7]

# 4. remove(item)
# Removes the first occurrence of the item.
my_list.remove(20)  # List becomes [0, 1, 3, 4, 5, 6, 7]

# 5. pop(index)
# Removes and returns the item at the given index.
removed_item = my_list.pop(2)  # removed_item will be 3, list becomes [0, 1, 4, 5, 6, 7]

# 6. index(item)
# Returns the index of the first occurrence of the item.
index = my_list.index(4)  # index will be 2

# 7. count(item)
# Returns the number of occurrences of an item.
count = my_list.count(1)  # count will be 1

# 8. sort()
# Sorts the items.
my_list.sort()  # List becomes [0, 1, 4, 5, 6, 7]

# 9. reverse()
# Reverses the list.
my_list.reverse()  # List becomes [7, 6, 5, 4, 1, 0]

# 10. clear()
# Removes all elements from the list.
my_list.clear()  # List becomes []

# 11. copy()
# Returns a shallow copy of the list.
new_list = mixed_list.copy()  # new_list becomes [1, 'apple', 3.14]

# 12. sum(iterable)
# Sum all items in the list (only for numerical lists).
total = sum([1, 2, 3])  # total will be 6

# 13. len(list)
# Returns the length of the list.
length = len(mixed_list)  # length will be 3

# 14. min(list) and max(list)
# Returns the smallest and largest item in the list (only for comparable lists).
min_val = min([1, 2, 3])  # min_val will be 1
max_val = max([1, 2, 3])  # max_val will be 3

# 15. any(list) and all(list)
# Checks if any or all items in list are True.
any_result = any([0, None, 2])  # any_result will be True
all_result = all([1, 2, 3])     # all_result will be True

# 16. .join()
# Concatenate list elements into a single string (only for lists of strings).
separator = ', '
joined_str = separator.join(['apple', 'banana', 'cherry'])  # Output will be 'apple, banana, cherry'

# =============================================================================
# Slicing
# =============================================================================
# List slicing allows you to obtain sub-lists.

# Extract elements from index 1 to 4
sub_list = my_list[1:5]  # sub_list becomes [6, 5, 4, 1]


# =============================================================================
# List Comprehensions
# =============================================================================

# Create a list of squares from 0 to 9
squares = [x*x for x in range(10)]  # squares will be [0, 1, 4, 9, ... , 81]

# Get all even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]  # Output: [0, 2, 4, 6, 8]

# Nested List Comprehensions
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [elem for row in matrix for elem in row]  # Output: [1, 2, 3, 4, 5, 6]

# Using Lambda Functions
# Note: While not common, you can use lambda functions in list comprehensions
lambda_squares = [(lambda x: x*x)(x) for x in range(10)]  # Output: [0, 1, 4, 9, ..., 81]

# Example: Get all positive numbers from a list
positives = [x for x in [-1, 0, 1, 2, -2] if x > 0]  # Output: [1, 2]

# 2. Data Transformation: Apply a transformation to each element in a list.
# Example: Convert all strings in a list to uppercase
upper_strings = [x.upper() for x in ['a', 'b', 'c']]  # Output: ['A', 'B', 'C']

# 3. Generating Test Data: Easily generate test data sets.
# Example: Generate a list of random numbers
import random
random_numbers = [random.randint(0, 100) for _ in range(10)]

# =============================================================================
# Nested Lists
# =============================================================================

# A list can also contain other lists.
nested_list = [[1, 2], [3, 4]]

# Access nested elements
nested_element = nested_list[0][1]  # nested_element will be 2


# =============================================================================
# When to Use Lists
# =============================================================================
# 1. When you need an ordered collection of items.
# 2. When items may need to be modified.
# 3. When you require various functionalities like sort, reverse, etc.

# =============================================================================
# Use Cases
# =============================================================================

# 1. Data Collection: Collect data from different sources into a single list.
# 2. Dynamic Modification: Add or remove elements dynamically during runtime.
# 3. Sorting and Searching: Use Python's built-in list methods to easily sort or find elements.
# 4. Multidimensional Data: Represent matrices or grids using nested lists.
# 5. Stack and Queues: Use `append()` and `pop()` for stack, and `insert(0, item)` and `pop()` for queues.
