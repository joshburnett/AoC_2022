# Imports for timing functions
try:
    from time import perf_counter_ns as monotonic_ns
    # from day01_cpython import total_calories_by_elf, part1, part2
    # from day01_circuitpython import total_calories_by_elf, part1, part2, python_runtime
    # python_runtime['name'] = 'CPython'

except ImportError:
    try:
        from time import monotonic_ns
        # from day01_circuitpython import total_calories_by_elf, part1, part2, python_runtime
        # python_runtime['name'] = 'CircuitPython'
    except ImportError:
        from time import ticks_us
        # from day01_circuitpython import total_calories_by_elf, part1, part2, python_runtime
        # python_runtime['name'] = 'MicroPython'

        def monotonic_ns():
            return ticks_us()*1000


#%% Imports for solving puzzle
from collections import deque

#%% Part 1, test
q = deque(maxlen=4)

with open('day06_test.txt', 'r') as f:
    while chars := f.readline():
        q.clear()
        for n, char in enumerate(chars):
            q.append(char)
            if len(set(q)) == 4:
                break

        print(f'n: {n + 1}    {chars.strip()}')


# %% Part 2, test
q = deque(maxlen=14)

with open('day06_test.txt', 'r') as f:
    while chars := f.readline():
        q.clear()
        for n, char in enumerate(chars):
            q.append(char)
            if len(set(q)) == 14:
                print(''.join(q))
                break

        print(f'n: {n + 1}    {chars.strip()}\n')

# %% Part 1
print(f'\n\n\n\nRunning puzzle, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

q = deque(maxlen=4)

with open('day06.txt', 'r') as f:
    chars = f.readline()
    for n, char in enumerate(chars):
        q.append(char)
        if len(set(q)) == 4:
            break

    t1 = monotonic_ns()

print(f'n: {n + 1}')

print('~' * 40)
print(f'Elapsed time: {(t1 - t0) / 1e9:.03e}s')


# %% Part 2
print(f'\n\n\n\nRunning puzzle, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

q = deque(maxlen=14)

with open('day06.txt', 'r') as f:
    chars = f.readline()
    for n, char in enumerate(chars):
        q.append(char)
        if len(set(q)) == 14:
            break

    t1 = monotonic_ns()

print(f'n: {n + 1}')

print('~' * 40)
print(f'Elapsed time: {(t1 - t0) / 1e9:.03e}s')

