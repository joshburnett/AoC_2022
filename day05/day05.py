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
from collections import defaultdict, deque
from pprint import pp


#%%
stacks = defaultdict(deque)
stack_section_finished = False
with open('day05_test.txt', 'r') as f:
    while line := f.readline():
        # print(line.strip())
        if not stack_section_finished:
            if line[1] == '1':
                stack_section_finished = True
                f.readline()
                pp(stacks)
                continue
            else:
                for stack_index, crate_id in enumerate(line[1:-2:4]):
                    if crate_id != ' ':
                        stacks[str(stack_index + 1)].appendleft(crate_id)
        else:
            print(line.strip())
            _, num_moves, __, from_stack, ___, to_stack = line.strip().split(' ')
            for _ in range(int(num_moves)):
                stacks[to_stack].append(stacks[from_stack].pop())

pp(stacks)

print(''.join([stacks[crate_id][-1] for crate_id in sorted(stacks.keys())]))


#%%
print(f'\n\n\n\nRunning puzzle, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

stacks = defaultdict(deque)
stack_section_finished = False
with open('day05.txt', 'r') as f:
    while line := f.readline():
        # print(line.strip())
        if not stack_section_finished:
            if line[1] == '1':
                stack_section_finished = True
                f.readline()
                # pp(stacks)
                continue
            else:
                for stack_index, crate_id in enumerate(line[1:-2:4]):
                    if crate_id != ' ':
                        stacks[str(stack_index + 1)].appendleft(crate_id)
        else:
            # print(line.strip())
            _, num_moves, __, from_stack, ___, to_stack = line.strip().split(' ')
            for _ in range(int(num_moves)):
                stacks[to_stack].append(stacks[from_stack].pop())

t1 = monotonic_ns()

pp(stacks)
print(''.join([stacks[crate_id][-1] for crate_id in sorted(stacks.keys())]))

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


#%%
stacks = defaultdict(deque)
stack_section_finished = False
working_queue = deque()
with open('day05_test.txt', 'r') as f:
    while line := f.readline():
        # print(line.strip())
        if not stack_section_finished:
            if line[1] == '1':
                stack_section_finished = True
                f.readline()
                # pp(stacks)
                continue
            else:
                for stack_index, crate_id in enumerate(line[1:-2:4]):
                    if crate_id != ' ':
                        stacks[str(stack_index + 1)].appendleft(crate_id)
        else:
            # print(line.strip())
            _, num_moves, __, from_stack, ___, to_stack = line.strip().split(' ')
            for _ in range(int(num_moves)):
                working_queue.appendleft(stacks[from_stack].pop())
            stacks[to_stack].extend(working_queue)
            working_queue.clear()

pp(stacks)


#%%
print(f'\n\n\n\nRunning puzzle, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

stacks = defaultdict(deque)
stack_section_finished = False
working_queue = deque()
with open('day05.txt', 'r') as f:
    while line := f.readline():
        if not stack_section_finished:
            if line[1] == '1':
                stack_section_finished = True
                f.readline()
                continue
            else:
                for stack_index, crate_id in enumerate(line[1:-2:4]):
                    if crate_id != ' ':
                        stacks[str(stack_index + 1)].appendleft(crate_id)
        else:
            _, num_moves, __, from_stack, ___, to_stack = line.strip().split(' ')
            for _ in range(int(num_moves)):
                working_queue.appendleft(stacks[from_stack].pop())
            stacks[to_stack].extend(working_queue)
            working_queue.clear()

t1 = monotonic_ns()

pp(stacks)
print(''.join([stacks[crate_id][-1] for crate_id in sorted(stacks.keys())]))

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')
