# from helpers import parse_test_input
import gc

try:
    from time import perf_counter_ns as monotonic_ns
    # from day01_cpython import total_calories_by_elf, part1, part2
    from day01_circuitpython import total_calories_by_elf, part1, part2

except ImportError:
    from time import monotonic_ns
    from day01_circuitpython import total_calories_by_elf, part1, part2

DAY = 1


#%% Run test for Day 1, Part 1
print(f'\n\n\n\nRunning test for Day {DAY}, Part 1:')
print('~'*40)

t0 = monotonic_ns()

calories_list = total_calories_by_elf(input_file_path='AOC inputs/day01_test.txt')
max_cals = part1(calories_list)

t1 = monotonic_ns()

if max_cals == 24_000:
    print('Test passed')
else:
    print('Incorrect result')

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')

# gc.collect()


# %% Run test for Day 1, Part 2
print(f'\n\n\n\nRunning test for Day {DAY}, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

top_3_cals_total = part2(calories_list)

t1 = monotonic_ns()

if top_3_cals_total == 45_000:
    print('Test passed')
else:
    print('Incorrect result')

print('~' * 40)
print(f'Elapsed time: {(t1 - t0) / 1e9:.03e}s')
# gc.collect()


#%% Run puzzle for Day 1, Part 1
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 1:')
print('~'*40)

t0 = monotonic_ns()

calories_list = total_calories_by_elf(input_file_path='AOC inputs/day01.txt')
max_cals = part1(calories_list)

t1 = monotonic_ns()
print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


# gc.collect()


#%% Run puzzle for Day 1, Part 1
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 2:')
print('~'*40)

t0 = monotonic_ns()

top_3_cals_total = part2(calories_list)

t1 = monotonic_ns()
print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


#%%

