# Script to run the calculation
# python src\\task5\\script.py

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
position = (0, 0)
direction = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] # directions N, E, S, W
visited = set()
visited.add(position)
first_revisited = None
navigations = [navigation.strip() for navigation in instructions.strip().split(',')] # instructions

# Follow instructions
for navigation in navigations:
    turn = navigation[0]
    distance = int(navigation[1:])

    # Turn right or left
    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4

    # Move +1 forward, check if already visited (and stop if so)
    dx, dy = delta[direction]
    for _ in range(distance):
        x, y = position
        position = (x + dx, y + dy)

        if position in visited and first_revisited is None:
            first_revisited = position
            break
        visited.add(position)

    if first_revisited:
        break

# Calculate the distance to the revisited location
if first_revisited:
    distance = abs(first_revisited[0]) + abs(first_revisited[1])
    print(distance)
else:
    print("no revisited locations")
