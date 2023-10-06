# =============================================================================
# Comprehensive Python Tuple Data Sheet
# =============================================================================

# =============================================================================
# Basic Tuple Declaration and Operations
# =============================================================================

# Declare a tuple with integers
my_tuple = (1, 2, 3, 4)

# Declare a tuple with mixed data types
mixed_tuple = (1, 'apple', 3.14)

# Access elements via index
first_elem = my_tuple[0]  # Output: 1

# Unpacking a tuple
first_elem, second_elem , third_elem , forth_elem = my_tuple  # first_elem = 1, second_elem = 2
#print(first_elem)

# =============================================================================
# Tuple Methods
# =============================================================================

# 1. .count()
# Count occurrences of a value
count_two = my_tuple.count(2)  # Output: 1

# 2. .index()
# Find the index of the first occurrence of a value
index_two = my_tuple.index(2)  # Output: 1

# =============================================================================
# Tuple Comprehensions? No, but...
# =============================================================================

# Tuples do not support comprehensions but you can use a list comprehension and convert it
evens = tuple(x for x in my_tuple if x % 2 == 0)  # Output: (2, 4)

# =============================================================================
# Use Cases
# =============================================================================

# 1. Immutable Data: Use tuples when you want an immutable list of items.
# 2. Packing and Unpacking: Useful for multiple returns from functions.

# =============================================================================
# Explanations
# =============================================================================

# 1. Immutable: Unlike lists, tuples are immutable. Once declared, they cannot be modified.
# 2. Methods: Tuples offer fewer methods compared to lists; commonly used are .count() and .index().
# 3. Tuple Comprehensions: Python does not offer tuple comprehensions, but you can achieve similar results using list comprehensions and converting to a tuple.

# =============================================================================
# =============================================================================
# namedtuple
# =============================================================================
# =============================================================================

from collections import namedtuple

# Define a namedtuple type
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create instances of Person namedtuple
john = Person('John', 30, 'Male')
jane = Person('Jane', 25, 'Female')

# Access fields by name
john_name = john.name  # Output: 'John'
john_age = john.age    # Output: 30

# Access fields by index (like regular tuples)
john_name = john[0]  # Output: 'John'

# =============================================================================
# namedtuple Methods
# =============================================================================

# 1. ._fields
# Get the names of fields
fields = john._fields  # Output: ('name', 'age', 'gender')

# 2. ._asdict()
# Convert to an OrderedDict
john_dict = john._asdict()  # Output: OrderedDict([('name', 'John'), ('age', 30), ('gender', 'Male')])

# 3. ._replace()
# Create a new instance with some fields replaced
jane_new = jane._replace(age=26)  # Output: Person(name='Jane', age=26, gender='Female')

# 4. namedtuple._make(iterable)
# Create a new instance from an iterable
new_person = Person._make(['Alex', 40, 'Male'])  # Output: Person(name='Alex', age=40, gender='Male')

# 5. namedtuple._field_defaults
# Get or set default values for fields (Python 3.7+)
PersonWithDefaults = namedtuple('PersonWithDefaults', ['name', 'age', 'gender'], defaults=['N/A', 'N/A'])
default_person = PersonWithDefaults('Alex')  # Output: PersonWithDefaults(name='Alex', age='N/A', gender='N/A')

# =============================================================================
# Use Cases for namedtuple
# =============================================================================

# 1. Readable Code: namedtuples make the code self-documenting.
# 2. Data Integrity: Immutable, ensuring data is consistent.
# 3. Packing & Unpacking: Useful for returning multiple values from a function with meaningful names.

# =============================================================================
# Explanations
# =============================================================================

# 1. namedtuple: A subclass of tuple, more readable and self-documenting.
# 2. Methods: Several useful methods such as ._fields, ._asdict(), and ._replace().
# 3. Use Cases: namedtuples are ideal for storing data records, making code more readable, and ensuring data integrity.
# 4. ._make(): 
# Creates a namedtuple from an iterable. It's equivalent to the namedtuple constructor but more readable when 
# the data source is an iterable.

# 5. ._field_defaults:
# Available in Python 3.7+, this allows you to set default field values for a namedtuple. It makes namedtuple
# more versatile in dealing with optional fields.