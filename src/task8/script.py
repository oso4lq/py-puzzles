# Script to run the calculation
# python src\\task8\\script.py

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
screen_width = 50
screen_height = 6
screen = [[0 for _ in range(screen_width)] for _ in range(screen_height)]
instructions_list = instructions.strip().split('\n')

# Follow instructions
for instruction in instructions_list:

    # rect AxB
    if instruction.startswith('rect'):
        params = instruction[5:]
        A_str, B_str = params.split('x')
        A = int(A_str)
        B = int(B_str)
        # Turn on the specified rectangle
        for y in range(B):
            for x in range(A):
                screen[y][x] = 1
    
    # rotate row y=A by B
    elif instruction.startswith('rotate row'):
        parts = instruction.split()
        y = int(parts[2][2:])
        B = int(parts[4])
        B %= screen_width
        screen[y] = screen[y][-B:] + screen[y][:-B]

    # rotate column x=A by B
    elif instruction.startswith('rotate column'):
        parts = instruction.split()
        x = int(parts[2][2:])
        B = int(parts[4])
        B %= screen_height
        column = [screen[y][x] for y in range(screen_height)]
        column = column[-B:] + column[:-B]
        for y in range(screen_height):
            screen[y][x] = column[y]
            
    else:
        print("error")

# Calculate the pixel(1) number
num_on = sum(sum(row) for row in screen)

# Output
print(num_on)
