# Script to run the calculation
# python src\\task2\\script.py

import os
import numpy as np

# Set the correct path for data.txt - used in every file for covenience
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data.txt')
try:
    with open(data_file_path, 'r') as file:
        instructions = file.read()
except FileNotFoundError:
    print("no data txt file")
    exit(1)


# Set initial values
lines = instructions.strip().split('\n')
grid = np.zeros((1000, 1000), dtype=bool) # bulbs grid

# Follow instructions
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('turn on'):
        action = 'turn on'
        rest = line[len('turn on '):]
    elif line.startswith('turn off'):
        action = 'turn off'
        rest = line[len('turn off '):]
    elif line.startswith('toggle'):
        action = 'toggle'
        rest = line[len('toggle '):]
    else:
        continue

    # Coordinates
    parts = rest.split(' through ')
    coord1 = parts[0].split(',')
    coord2 = parts[1].split(',')
    x1, y1 = int(coord1[0]), int(coord1[1])
    x2, y2 = int(coord2[0]), int(coord2[1])
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    # Apply changes
    if action == 'turn on':
        grid[y1:y2+1, x1:x2+1] = True
    elif action == 'turn off':
        grid[y1:y2+1, x1:x2+1] = False
    elif action == 'toggle':
        grid[y1:y2+1, x1:x2+1] = ~grid[y1:y2+1, x1:x2+1]

# Count the number of bulbs that are on
num_on = np.sum(grid)

print(num_on)
