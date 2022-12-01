from helpers import parse_test_input

try:
    from time import perf_counter_ns as monotonic_ns
except ImportError:
    from time import monotonic_ns

test_inputs, test_answer = parse_test_input(day=1)


def part1(input_list):
    # t0 = time.perf_counter()
    t0 = monotonic_ns()
    calories = [0]

    for n, line in enumerate(input_list):
        if line == '':
            calories.append(0)
        else:
            calories[-1] += int(line)

    max_cals = max(calories)
    max_elf = calories.index(max_cals)
    # print(f'Elapsed time: {(time.perf_counter()-t0):.3g}s')
    print(f'Elapsed time: {(monotonic_ns()-t0)/1e9:.03e}s')
    print(f'Max calories: {max_cals}, carried by elf #{max_elf+1}')
    return max_cals


max_cals = part1(test_inputs)

if max_cals == test_answer:
    print('Test passed')
else:
    print('Incorrect result')
