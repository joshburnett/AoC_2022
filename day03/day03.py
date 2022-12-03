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


DAY = 3


#%%
total_score = 0
score_offset = ord('a') - 1

with open('day03_test.txt', 'r') as f:
    while line := f.readline():
        line = line.strip()
        sack1 = set(line[:len(line) // 2])
        sack2 = set(line[len(line) // 2:])
        letter = sack1.intersection(sack2).pop()
        score = (ord(letter.lower()) - score_offset) + letter.isupper() * 26
        total_score += score
        print(f'Letter: {letter}, score: {score}')

print(total_score)

#%%
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

total_score = 0
score_offset = ord('a') - 1

with open('day03.txt', 'r') as f:
    while line := f.readline():
        line = line.strip()
        sack1 = set(line[:len(line) // 2])
        sack2 = set(line[len(line) // 2:])
        letter = sack1.intersection(sack2).pop()
        total_score += (ord(letter.lower()) - score_offset) + letter.isupper() * 26

t1 = monotonic_ns()

print(total_score)

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


#%%
score_offset = ord('a') - 1

f = open('day03_test2.txt', 'r')
line = f.readline()
if line:
    sack1 = set(line.strip())
    sack2 = set(f.readline().strip())
    sack3 = set(f.readline().strip())
    letter = sack1.intersection(sack2).intersection(sack3).pop()
    score = (ord(letter.lower()) - score_offset) + letter.isupper() * 26
    print(f'Letter: {letter}, score: {score}')


line = f.readline()
if line:
    sack1 = set(line.strip())
    sack2 = set(f.readline().strip())
    sack3 = set(f.readline().strip())
    letter = sack1.intersection(sack2).intersection(sack3).pop()
    score = (ord(letter.lower()) - score_offset) + letter.isupper() * 26
    print(f'Letter: {letter}, score: {score}')



#%%
score_offset = ord('a') - 1
total_score = 0

with open('day03_test2.txt', 'r') as f:
    while line := f.readline():
        if line:
            sack1 = set(line.strip())
            sack2 = set(f.readline().strip())
            sack3 = set(f.readline().strip())
            letter = set.intersection(sack1, sack2, sack3).pop()
            score = (ord(letter.lower()) - score_offset) + letter.isupper() * 26
            print(f'Letter: {letter}, score: {score}')
            total_score += score

print(total_score)

#%%
print(f'\n\n\n\nRunning puzzle for Day {DAY}, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

score_offset = ord('a') - 1
total_score = 0

with open('day03.txt', 'r') as f:
    while line := f.readline():
        if line:
            sack1 = set(line.strip())
            sack2 = set(f.readline().strip())
            sack3 = set(f.readline().strip())
            letter = set.intersection(sack1, sack2, sack3).pop()
            total_score += (ord(letter.lower()) - score_offset) + letter.isupper() * 26

t1 = monotonic_ns()

print(total_score)

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')
