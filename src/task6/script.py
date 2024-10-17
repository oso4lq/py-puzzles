# Script to run the calculation
# python src\\task6\\script.py

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


frequencies = instructions.strip().splitlines()
changes = [int(frequency.strip()) for frequency in frequencies if frequency.strip()]

# Calculate the sum
resulting_frequency = sum(changes)

# Output
print(resulting_frequency)
