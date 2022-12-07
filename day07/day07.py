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
from pprint import pp


#%% Part 1, test
def process_listing(logfile_handle) -> dict:
    contents = {}
    line = logfile_handle.readline()
    while line:
        if line == '$ cd ..\n':
            return contents
        elif line.startswith('$ cd'):
            new_dir = line[5:-1]
            contents[new_dir] = process_listing(logfile_handle)
        elif line == '$ ls\n':
            pass
        elif line.startswith('dir'):
            pass
        else:
            size, file_name = line.strip().split()
            contents[file_name] = int(size)
        line = logfile_handle.readline()
    return contents


def calc_sizes1(contents) -> int:
    dirsize = 0
    for label, value in contents.items():
        if isinstance(value, int):
            dirsize += value
        else:
            dirsize += calc_sizes1(value)
    if dirsize <= 100_000:
        small_dirs.append(dirsize)
    return dirsize


#%%
with open('day07_test.txt', 'r') as f:
    listing = process_listing(f)
    pp(listing)

small_dirs = []
calc_sizes1(listing)

print(sum(small_dirs))


#%%
dir_sizes = []


def calc_sizes2(contents) -> int:
    dirsize = 0
    for label, value in contents.items():
        if isinstance(value, int):
            dirsize += value
        else:
            subdirsize = calc_sizes2(value)
            dirsize += subdirsize
            dir_sizes.append((label, subdirsize))
    return dirsize


calc_sizes2(listing)

dir_sizes.sort(key=lambda item: item[1])

print(dir_sizes)

disk_size = 70_000_000
print(f'Space available: {disk_size-dir_sizes[-1][1]}')
need_to_clear = 30_000_000 - (disk_size-dir_sizes[-1][1])
print(f'{need_to_clear=}')

for dirname, size in dir_sizes:
    if size >= need_to_clear:
        break

print(f'Smallest dir to delete: {dirname}: {size}')


#%%
with open('day07.txt', 'r') as f:
    listing = process_listing(f)

small_dirs = []
calc_sizes1(listing)

print(sum(small_dirs))


#%%
dir_sizes = []

calc_sizes2(listing)

dir_sizes.sort(key=lambda item: item[1])

print(dir_sizes)

disk_size = 70_000_000
print(f'Space available: {disk_size-dir_sizes[-1][1]}')
need_to_clear = 30_000_000 - (disk_size-dir_sizes[-1][1])
print(f'{need_to_clear=}')

for dirname, size in dir_sizes:
    if size >= need_to_clear:
        break

print(f'Smallest dir to delete: {dirname}: {size}')
