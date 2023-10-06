# =============================================================================
# Comprehensive Python Dictionary, defaultdict, and OrderedDict Data Sheet
# =============================================================================

# =============================================================================
# Basic Dictionary Operations
# =============================================================================

# Declare a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Access values using keys
value1 = my_dict['key1']  # Output: 'value1'

# Update a value
my_dict['key1'] = 'new_value1'

# =============================================================================
# Dictionary Methods (At least 10)
# =============================================================================

# 1. .keys() - returns a view object displaying all keys.
keys = my_dict.keys()

# 2. .values() - returns a view object displaying all values.
values = my_dict.values()

# 3. .items() - returns a view object displaying all key-value tuple pairs.
items = my_dict.items()

# 4. .get(key, default) - returns the value for the specified key, if it exists. Otherwise, returns default.
value = my_dict.get('key3', 'default_value')

# 5. .setdefault(key, default) - returns the value of the specified key. If key does not exist, insert key with default value.
my_dict.setdefault('key3', 'default_value')

# 6. .pop(key) - removes the value of the specified key and returns it.
popped_value = my_dict.pop('key1')

# 7. .popitem() - removes and returns the last key-value pair as a tuple.
last_item = my_dict.popitem()

# 8. .update(other_dict) - merges a dictionary with another dictionary or with an iterable of key-value pairs.
my_dict.update({'key4': 'value4'})

# 9. .clear() - removes all items from the dictionary.
my_dict.clear()

# 10. .copy() - returns a shallow copy of the dictionary.
dict_copy = my_dict.copy()

# 11. fromkeys(sequence, value) - Create a new dictionary with keys from sequence and values set to value
new_dict = dict.fromkeys(['key1', 'key2'], 'default_value')

#=============================================================================
# Dictionary Comprehension
# =============================================================================

# Basic Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional Dictionary Comprehension
even_squared_dict = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# Output: {2: 4, 4: 16}

# Using lambda functions in Dictionary Comprehension
transform_dict = {(lambda x: f'key_{x}')(x): x**2 for x in range(1, 6)}
# Output: {'key_1': 1, 'key_2': 4, 'key_3': 9, 'key_4': 16, 'key_5': 25}

# =============================================================================
# Explanations
# =============================================================================

# Dictionary Comprehension: A concise way to create dictionaries using a single line of code.

# 1. Basic Dictionary Comprehension: Provides a simple way to create dictionaries dynamically.
# 2. Conditional Dictionary Comprehension: Adds conditions for key-value pair inclusion.
# 3. Using Lambda: Enables customization of keys or values through lambda functions.


# =============================================================================
# defaultdict
# =============================================================================

from collections import defaultdict

# Initialize a defaultdict with a default factory (int)
dd = defaultdict(int)

# Access a non-existing key, returns default value (int: 0)
value = dd['non_exist']  # Output: 0

# Functions (At least 5)
# 1-5: Inherits all methods from dict
# 6. .default_factory - The factory function for generating default values.
dd.default_factory = list

# =============================================================================
# OrderedDict
# =============================================================================

from collections import OrderedDict

# Initialize an OrderedDict
od = OrderedDict([('key1', 'value1'), ('key2', 'value2')])

# Functions (At least 5)
# 1-5: Inherits all methods from dict
# 6. .move_to_end(key, last=True) - Move a key-value pair to either end of an OrderedDict.
od.move_to_end('key1')

# =============================================================================
# Iterating through Dictionaries
# =============================================================================

# Iterating through a regular dictionary
for key, value in my_dict.items():
    print(key, value)

# Iterating through a nested dictionary
nested_dict = {'outer_key': {'inner_key': 'value'}}
for outer_key, inner_dict in nested_dict.items():
    for inner_key, value in inner_dict.items():
        print(outer_key, inner_key, value)

# =============================================================================
# Explanations
# =============================================================================

# Dictionary: Key-value pair storage. Great for data retrieval and structuring data.
# defaultdict: Extends dict, returns default value for missing keys.
# OrderedDict: Extends dict, maintains key insertion order.

# =============================================================================
# Use Cases
# =============================================================================

# Dictionary: General-purpose, key-value storage. High-speed data retrieval.
# defaultdict: When you want a dict with default values for missing keys.
# OrderedDict: When insertion order matters (especially prior to Python 3.7 where dict did not maintain order).

