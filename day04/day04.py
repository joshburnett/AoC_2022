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


#%%
count = 0
with open('day04_test.txt', 'r') as f:
    while line := f.readline():
        start1, stop1, start2, stop2 = (int(s) for s in line.strip().replace(',', '-').split('-'))
        print(line)
        if (start1 <= start2) and (stop2 <= stop1) or (start2 <= start1) and (stop1 <= stop2):
            count += 1
            print('  Contained')
        else:
            print('  Not contained')

print(count)

#%%
print(f'\n\n\n\nRunning puzzle, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

count = 0
with open('day04.txt', 'r') as f:
    while line := f.readline():
        start1, stop1, start2, stop2 = (int(s) for s in line.strip().replace(',', '-').split('-'))
        # print(line)
        if ((start1 <= start2) and (stop2 <= stop1)) or ((start2 <= start1) and (stop1 <= stop2)):
            count += 1
            # print('  Contained')
        # else:
        #     print('  Not contained')

t1 = monotonic_ns()

print(count)

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


#%%
count = 0
with open('day04_test.txt', 'r') as f:
    while line := f.readline():
        start1, stop1, start2, stop2 = (int(s) for s in line.strip().replace(',', '-').split('-'))
        print(line.strip())
        if not ((stop1 < start2) or (stop2 < start1)):
            count += 1
            print('  Overlap')
        else:
            print('  No overlap')

print(count)


#%%
print(f'\n\n\n\nRunning puzzle, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

count = 0
with open('day04.txt', 'r') as f:
    while line := f.readline():
        start1, stop1, start2, stop2 = (int(s) for s in line.strip().replace(',', '-').split('-'))
        if not ((stop1 < start2) or (stop2 < start1)):
            count += 1

t1 = monotonic_ns()

print(count)

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')

#%% Minimal implementation for part 2
count = 0
with open('day04.txt', 'r') as f:
    while line := f.readline():
        start1, stop1, start2, stop2 = (int(s) for s in line.strip().replace(',', '-').split('-'))
        if not ((stop1 < start2) or (stop2 < start1)):
            count += 1
