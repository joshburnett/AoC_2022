#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path
from copy import copy


#%% Part 1, test
instructions = [i.strip() for i in Path('day10_test.txt').read_text().splitlines()]
register_vals = [1]
for i in instructions:
    register_vals.append(register_vals[-1])
    if i != 'noop':
        register_vals.append(register_vals[-1]+int(i.split(' ')[1]))

print(sum([register_vals[n-1]*n for n in range(20, 221, 40)]))


# %% Part 2, test
# pixels = [abs(val - (n % 40)) < 2 for n, val in enumerate(register_vals)]
# n = 0
# abs(register_vals[0])
pixels = ['#' if abs(val - (n % 40)) < 2 else '.' for n, val in enumerate(register_vals)]

for offset in range(0, 220, 40):
    print(''.join(pixels[offset:offset+40]))


#%% Part 1, puzzle
instructions = [i.strip() for i in Path('day10.txt').read_text().splitlines()]
register_vals = [1]
for i in instructions:
    register_vals.append(register_vals[-1])
    if i != 'noop':
        register_vals.append(register_vals[-1]+int(i.split(' ')[1]))

print(sum([register_vals[n-1]*n for n in range(20, 221, 40)]))


# %% Part 2, puzzle
pixels = ['#' if abs(val - (n % 40)) < 2 else '.' for n, val in enumerate(register_vals)]

for offset in range(0, 220, 40):
    print(''.join(pixels[offset:offset+40]))
