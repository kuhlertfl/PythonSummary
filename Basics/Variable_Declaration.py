# Python Types and Declarations Data Sheet

# =============================================================================
# Basic Types
# =============================================================================

# Integer
x_int = 1

# Float
x_float = 1.0

# String
x_str = "hello"

#Adding Strings Work
x_str = x_str + " world"

# Boolean
x_bool = True  # or False

# NoneType
x_none = None

# =============================================================================
# Collection Types each type will have its own data sheet 
# =============================================================================

# List (Ordered, Mutable)
x_list = [1, 2, 3]

# Tuple (Ordered, Immutable)
x_tuple = (1, 2, 3)

# Set (Unordered, Mutable, Unique Elements)
x_set = {1, 2, 3}

# Dictionary (Unordered, Mutable, Key-Value Pairs)
x_dict = {"key1": "value1", "key2": "value2"}

# =============================================================================
# Type Conversion
# =============================================================================

# To Integer
int_val = int(1.0)

# To Float
float_val = float(1)

# To String
str_val = str(1)

# To Boolean
bool_val = bool(1)  # 0 becomes False, non-zero becomes True

# To List
list_val = list((1, 2, 3))

# To Tuple
tuple_val = tuple([1, 2, 3])

# To Set
set_val = set([1, 1, 2, 3])

# To Dictionary
dict_val = dict(key1="value1", key2="value2")

# =============================================================================
# Checking Type
# =============================================================================

# Using type()
type_of_x = type(x_int)  # Output: <class 'int'>

# Using isinstance()
check_type = isinstance(x_int, int)  # Output: True

# =============================================================================
# Specialized Data Types (from the standard library) for more info check the collections folder 
# =============================================================================

from collections import namedtuple, deque
from typing import List, Dict, Tuple, Any

# Namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

# Deque (Double-Ended Queue)
d = deque([1, 2, 3])

# Typed List
x_typed_list: List[int] = [1, 2, 3]

# Typed Dictionary
x_typed_dict: Dict[str, int] = {"key1": 1}

# Typed Tuple
x_typed_tuple: Tuple[int, float] = (1, 2.0)

# Any Type
x_any: Any = "can be any type"
