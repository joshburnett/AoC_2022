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
from pathlib import Path


#%% Part 1
def count_visible_trees(input_path, debug=True):
    treemap = Path(input_path).read_text().splitlines()
    treemap = [[int(char) for char in row] for row in treemap]
    numrows = len(treemap)
    numcols = len(treemap[0])
    visible_trees = []

    # View from left
    for rownum, row in enumerate(treemap):
        tallest = -1
        for colnum, tree in enumerate(row):
            if tree > tallest:
                visible_trees.append((rownum, colnum))
                tallest = tree

    # View from right
    for rownum, row in enumerate(treemap):
        tallest = -1
        for colnum in range(numcols-1, -1, -1):
            tree = row[colnum]
            if tree > tallest:
                visible_trees.append((rownum, colnum))
                tallest = tree

    # View from top
    for colnum in range(numcols):
        tallest = -1
        for rownum in range(numrows):
            tree = treemap[rownum][colnum]
            if tree > tallest:
                visible_trees.append((rownum, colnum))
                tallest = tree

    # View from bottom
    for colnum in range(numcols):
        tallest = -1
        for rownum in range(numrows-1, -1, -1):
            tree = treemap[rownum][colnum]
            if tree > tallest:
                visible_trees.append((rownum, colnum))
                tallest = tree

    visible_trees_set = set(visible_trees)
    if debug:
        pp(visible_trees)
        pp(visible_trees_set)

    return visible_trees_set


visible_trees = count_visible_trees('day08_test.txt', debug=True)
print(f'Test: Num visible trees: {len(visible_trees)}')

print(f'\n\n\n\nRunning puzzle, Part 1:')
print('~' * 40)

t0 = monotonic_ns()

visible_trees = count_visible_trees('day08.txt', debug=False)
t1 = monotonic_ns()

print(f'\n\nPuzzle: Num visible trees: {len(visible_trees)}')

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')


#%% Part 2, test
treemap = Path('day08_test.txt').read_text().splitlines()
treemap = [[int(char) for char in row] for row in treemap]
numrows = len(treemap)
numcols = len(treemap[0])


def calc_viewing_score(tree_row, tree_col):
    base_tree = treemap[tree_row][tree_col]

    # Look up
    up_dist = 0
    for rownum in range(tree_row-1, -1, -1):
        up_dist += 1
        if treemap[rownum][tree_col] >= base_tree:
            break

    # Look down
    down_dist = 0
    for rownum in range(tree_row+1, numrows):
        down_dist += 1
        if treemap[rownum][tree_col] >= base_tree:
            break

    # Look right
    right_dist = 0
    for colnum in range(tree_col+1, numcols):
        right_dist += 1
        if treemap[tree_row][colnum] >= base_tree:
            break

    # Look left
    left_dist = 0
    for colnum in range(tree_col-1, -1, -1):
        left_dist += 1
        if treemap[tree_row][colnum] >= base_tree:
            break

    return up_dist*down_dist*right_dist*left_dist


calc_viewing_score(tree_row=1, tree_col=2)
calc_viewing_score(tree_row=3, tree_col=2)

scores = []
for rownum in range(numrows):
    for colnum in range(numcols):
        scores.append(calc_viewing_score(tree_row=rownum, tree_col=colnum))

max(scores)


#%% Part 2, puzzle
print(f'\n\n\n\nRunning puzzle, Part 2:')
print('~' * 40)

t0 = monotonic_ns()
treemap = Path('day08.txt').read_text().splitlines()
treemap = [[int(char) for char in row] for row in treemap]
numrows = len(treemap)
numcols = len(treemap[0])

scores = []
for rownum in range(numrows):
    for colnum in range(numcols):
        scores.append(calc_viewing_score(tree_row=rownum, tree_col=colnum))

t1 = monotonic_ns()

print(f'\n\nMax possible viewing score: {max(scores)}')

print('~'*40)
print(f'Elapsed time: {(t1-t0)/1e9:.03e}s')

