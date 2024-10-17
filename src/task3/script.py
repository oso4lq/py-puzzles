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

# Follow instructions
for line in instructions:
    lhs, rhs = line.split('->')
    lhs = lhs.strip()
    rhs = rhs.strip()
    wires[rhs] = lhs

def evaluate(wire):
    
    operation = wires[wire]
    tokens = operation.split()

    if wire.isdigit():
        return int(wire)
    
    if wire in computed:
        return computed[wire]
    
    if len(tokens) == 1:
        value = evaluate(tokens[0])

    elif len(tokens) == 2:
        op, x = tokens
        if op == 'NOT':
            value = ~evaluate(x) & 0xFFFF
            
    elif len(tokens) == 3:
        x, op, y = tokens
        if op == 'AND':
            value = evaluate(x) & evaluate(y)
        elif op == 'OR':
            value = evaluate(x) | evaluate(y)
        elif op == 'LSHIFT':
            value = (evaluate(x) << int(y)) & 0xFFFF
        elif op == 'RSHIFT':
            value = evaluate(x) >> int(y)

    computed[wire] = value
    return value

signal_a = evaluate('a')

print(signal_a)
