# Script to run the calculation
# python src\\task7\\script.py

import os
from datetime import datetime
import re
from collections import defaultdict, Counter

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
records = instructions.strip().split('\n')
entries = []
current_guard_ID = None
selected_guard_ID = None
sleep_start_time = None
max_sleep_minute = None
max_sleep_count = 0
guard_sleep_minutes = defaultdict(Counter)

# Follow instructions
for record in records:
    timeraw = record[1:17]
    note = record[19:]
    time = datetime.strptime(timeraw, '%Y-%m-%d %H:%M') # handle time
    entries.append((time, note))
entries.sort() # sort by date

# Handle the sorted entries
for time, note in entries:
    if "Guard" in note:
        m = re.match(r'Guard #(\d+) begins shift', note) # ID
        if m:
            current_guard_ID = int(m.group(1))
    elif note == "falls asleep":
        sleep_start_time = time
    elif note == "wakes up":
        sleep_end_time = time
        if current_guard_ID is not None and sleep_start_time is not None:
            sleep_minutes = range(sleep_start_time.minute, sleep_end_time.minute)
            guard_sleep_minutes[current_guard_ID].update(sleep_minutes)
    else:
        print("error")

# Calculate minutes and guard ID
for guard_id, minutes_counter in guard_sleep_minutes.items():
    if minutes_counter:
        minute, count = minutes_counter.most_common(1)[0]
        if count > max_sleep_count:
            max_sleep_count = count
            max_sleep_minute = minute
            selected_guard_ID = guard_id

# Output
print(f"guard {selected_guard_ID} slept {max_sleep_count} times on minute {max_sleep_minute}")
print(f"guard ID * minute = {selected_guard_ID * max_sleep_minute}")
