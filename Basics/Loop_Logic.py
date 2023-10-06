# Python Loop Summary Data Sheet

# =============================================================================
# For Loop
# =============================================================================
# Basic for loop with a list
for i in [1, 2, 3]:
    print(f"i: {i}")

# Using range function
for i in range(3):  # 0, 1, 2
    print(f"i: {i}")

# With start and end
for i in range(1, 4):  # 1, 2, 3
    print(f"i: {i}")

# With start, end, and step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"i: {i}")

# Loop through string characters
for char in "hello":
    print(f"char: {char}")

# Loop through dictionary
for key, value in {'a': 1, 'b': 2}.items():
    print(f"key: {key}, value: {value}")

# Loop with index using enumerate
for idx, val in enumerate([4, 5, 6]):
    print(f"index: {idx}, value: {val}")

# Nested for loops
for i in range(2):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# =============================================================================
# While Loop
# =============================================================================
# Basic while loop
count = 0
while count < 3:
    print(f"count: {count}")
    count += 1  # Increment count

# While loop with else
count = 0
while count < 3:
    print(f"count: {count}")
    count += 1
else:
    print("Loop ended")

# Using 'break' to exit loop
count = 0
while True:
    if count >= 3:
        break
    print(f"count: {count}")
    count += 1

# Using 'continue' to skip iteration
count = 0
while count < 3:
    if count == 1:
        count += 1
        continue
    print(f"count: {count}")
    count += 1

# =============================================================================
# Loop Control Statements
# =============================================================================
# 'break' exits the loop
for i in range(3):
    if i == 1:
        break
    print(f"i: {i}")

# 'continue' skips the rest of the loop body for the current iteration
for i in range(3):
    if i == 1:
        continue
    print(f"i: {i}")

# 'pass' does nothing, can be used as a placeholder
for i in range(3):
    if i == 1:
        pass
    print(f"i: {i}")