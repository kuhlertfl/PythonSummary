# Python f-strings Example Data Sheet

# Basic Usage
basic_example = f"Hello, {5 + 2}"  # Output: "Hello, 7"
print(f"Basic Usage: {basic_example}")

# Alignment and Padding
left_align = f"{42:<5}"  # Output: "42   "
print(f"Left-align: {left_align}")

right_align = f"{42:>5}"  # Output: "   42"
print(f"Right-align: {right_align}")

center_align = f"{42:^5}"  # Output: " 42  "
print(f"Center-align: {center_align}")

with_sign_and_zeros = f"{42:=+5}"  # Output: "+  42"
print(f"Sign with zeros: {with_sign_and_zeros}")

# Numeric Formatting
always_sign = f"{42:+}"  # Output: "+42"
print(f"Always sign: {always_sign}")

negative_only = f"{-42:-}"  # Output: "-42"
print(f"Negative only: {negative_only}")

leading_space = f"{42: }"  # Output: " 42"
print(f"Leading space: {leading_space}")

# Width and Precision
width = f"{42:5}"  # Output: "   42"
print(f"Width: {width}")

precision = f"{3.14159:.2f}"  # Output: "3.14"
print(f"Precision: {precision}")

# Type Specifiers
integer_type = f"{42:d}"  # Output: "42"
print(f"Integer Type: {integer_type}")

float_type = f"{3.14159:f}"  # Output: "3.141590"
print(f"Float Type: {float_type}")

binary_type = f"{42:b}"  # Output: "101010"
print(f"Binary Type: {binary_type}")

hex_lower = f"{255:x}"  # Output: "ff"
print(f"Hex Lowercase: {hex_lower}")

hex_upper = f"{255:X}"  # Output: "FF"
print(f"Hex Uppercase: {hex_upper}")

octal_type = f"{64:o}"  # Output: "100"
print(f"Octal Type: {octal_type}")

exp_notation = f"{42:e}"  # Output: "4.200000e+01"
print(f"Exponential Notation: {exp_notation}")

# Complex Example
complex_example = f"{3.14159:+10.2f}"  # Output: "     +3.14"
print(f"Complex Example: {complex_example}")
