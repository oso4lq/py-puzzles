# Script to run the calculation
# python src\\task1\\script.py

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
x, y = 0, 0
visited_houses = set()
visited_houses.add((x, y))

# Calculate the number of unique houses visited
for move in instructions:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    elif move == '<':
        x -= 1
    visited_houses.add((x, y))

# Output
print(len(visited_houses))
