# Script to run the calculation
# python src\\task4\\script.py

import os

# Set the correct path for data.txt - used in every file for convenience
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data.txt')
try:
    with open(data_file_path, 'r') as file:
        instructions = file.read()
except FileNotFoundError:
    print("no data txt file")
    exit(1)


# Set initial values
garbage_count = 0
inside_garbage = False
skip_next = False

# Sort out the useful data
for c in instructions:
    if skip_next:
        skip_next = False
        continue
    if inside_garbage:
        if c == '!':
            skip_next = True
        elif c == '>':
            inside_garbage = False
        else:
            garbage_count += 1
    else:
        if c == '<':
            inside_garbage = True

# Output
print(garbage_count)
