# Script to run the calculation
# python src\\task3\\script.py

import os

# Set the correct path for data.txt - used in every file for convenience
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data.txt')
try:
    with open(data_file_path, 'r') as file:
        instructions = file.read().splitlines()
except FileNotFoundError:
    print("no data txt file")
    exit(1)


# Set initial values
wires = {}
computed = {}

for line in instructions:
    lhs, rhs = line.split('->')
    lhs = lhs.strip()
    rhs = rhs.strip()
    wires[rhs] = lhs

