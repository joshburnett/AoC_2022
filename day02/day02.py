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


DAY = 2

#%% Run test for Part 1
print(f'\n\n\n\nRunning test for Day {DAY}, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

play_scores = {'X': 1, 'Y': 2, 'Z': 3}

outcome_scores = {'A X': 3,  # draw
                  'A Y': 6,  # win
                  'A Z': 0,
                  'B X': 0,  # lose
                  'B Y': 3,  # draw
                  'B Z': 6,  # win
                  'C X': 6,  # win
                  'C Y': 0,  # lose
                  'C Z': 3,  # draw
                  }

score = 0
with open('day02_test.txt', 'r') as f:
    while (line := f.readline()):
        line = line.strip()
        score += outcome_scores[line] + play_scores[line[-1]]

t1 = monotonic_ns()

print(f'\nTotal score: {score}')

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


# %% Run puzzle for Part 1
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

score = 0
with open('day02.txt', 'r') as f:
    while (line := f.readline()):
        line = line.strip()
        # line_score = outcome_scores[line] + play_scores[line[-1]]
        # print(f'Round: {line}, score: {line_score}')
        # score += line_score
        score += outcome_scores[line] + play_scores[line[-1]]

t1 = monotonic_ns()

print(f'\nTotal score: {score}')

print('\n' + '~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


# %% Run test for Part 2
print(f'\n\n\n\nRunning test for Day {DAY}, Part 2:')
print('~' * 40)

t0 = monotonic_ns()

outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}
play_scores = {'A': 1, 'B': 2, 'C': 3}


play_required = {'A X': 'C',  # lose against A
                 'A Y': 'A',  # draw against A
                 'A Z': 'B',  # win against A
                 'B X': 'A',
                 'B Y': 'B',
                 'B Z': 'C',
                 'C X': 'B',
                 'C Y': 'C',
                 'C Z': 'A',
                 }

score = 0
with open('day02_test.txt', 'r') as f:
    while (line := f.readline()):
        line = line.strip()
        # line_score = outcome_scores[line[-1]] + play_scores[play_required[line]]
        # print(f'Round: {line}, score: {line_score}')
        # score += line_score
        score += outcome_scores[line[-1]] + play_scores[play_required[line]]


t1 = monotonic_ns()

print(f'\nTotal score: {score}')

if score == 12:
    print('Test passed')
else:
    print('Incorrect result')

print('~' * 40)
print(f'Elapsed time: {(t1 - t0) / 1e9:.03e}s')


#%% Run puzzle for Part 2
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 2:')
print('~'*40)

t0 = monotonic_ns()

outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}
play_scores = {'A': 1, 'B': 2, 'C': 3}


play_required = {'A X': 'C',  # lose against A
                 'A Y': 'A',  # draw against A
                 'A Z': 'B',  # win against A
                 'B X': 'A',
                 'B Y': 'B',
                 'B Z': 'C',
                 'C X': 'B',
                 'C Y': 'C',
                 'C Z': 'A',
                 }

score = 0
with open('day02.txt', 'r') as f:
    while (line := f.readline()):
        line = line.strip()
        # line_score = outcome_scores[line[-1]] + play_scores[play_required[line]]
        # print(f'Round: {line}, score: {line_score}')
        # score += line_score
        score += outcome_scores[line[-1]] + play_scores[play_required[line]]


t1 = monotonic_ns()

print(f'Total score: {score}')

print('~' * 40)
print(f'Elapsed time: {(t1 - t0) / 1e9:.03e}s')

