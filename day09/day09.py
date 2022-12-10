#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path
from copy import copy


#%% Part 1, test
def move_head(direction):
    new_tail_pos = tail_visited[-1]
    match direction:
        case 'R':
            head_pos[0] += 1
            if head_pos[0] - tail_visited[-1][0] == 2:
                new_tail_pos = (head_pos[0]-1, head_pos[1])
        case 'L':
            head_pos[0] -= 1
            if head_pos[0] - tail_visited[-1][0] == -2:
                new_tail_pos = (head_pos[0]+1, head_pos[1])
        case 'U':
            head_pos[1] += 1
            if head_pos[1] - tail_visited[-1][1] == 2:
                new_tail_pos = (head_pos[0], head_pos[1]-1)
        case 'D':
            head_pos[1] -= 1
            if head_pos[1] - tail_visited[-1][1] == -2:
                new_tail_pos = (head_pos[0], head_pos[1]+1)

    tail_visited.append(new_tail_pos)


tail_visited = [(0, 0)]
head_pos = [0, 0]

moves = Path('day09_test.txt').read_text().splitlines()

for move in moves:
    move_dir, distance = move.strip().split(' ')
    for _ in range(int(distance)):
        move_head(move_dir)

print(f'Total places tail went: {len(set(tail_visited))}')


#%% Part 1, puzzle
tail_visited = [(0, 0)]
head_pos = [0, 0]

moves = Path('day09.txt').read_text().splitlines()

for move in moves:
    move_dir, distance = move.strip().split(' ')
    for num_num in range(int(distance)):
        move_head(move_dir)

print(f'Total places tail went: {len(set(tail_visited))}')


#%%
def move_head(direction, head_pos: tuple):
    match direction:
        case 'R':
            # print('\nmove right')
            return head_pos[0] + 1, head_pos[1]
        case 'L':
            # print('\nmove left')
            return head_pos[0] - 1, head_pos[1]
        case 'U':
            # print('\nmove up')
            return head_pos[0], head_pos[1] + 1
        case 'D':
            # print('\nmove down')
            return head_pos[0], head_pos[1] - 1


def propogate_move(lead_pos: tuple, follow_pos: tuple):
    new_lead_pos = list(lead_pos)
    new_follow_pos = copy(follow_pos)

    if new_lead_pos[0] - follow_pos[0] == 2:
        if new_lead_pos[1] - follow_pos[1] == 2:
            new_follow_pos = (new_lead_pos[0]-1, new_lead_pos[1]-1)
        elif new_lead_pos[1] - follow_pos[1] == -2:
            new_follow_pos = (new_lead_pos[0]-1, new_lead_pos[1]+1)
        else:
            new_follow_pos = (new_lead_pos[0]-1, new_lead_pos[1])
    elif new_lead_pos[0] - follow_pos[0] == -2:
        if new_lead_pos[1] - follow_pos[1] == 2:
            new_follow_pos = (new_lead_pos[0]+1, new_lead_pos[1]-1)
        elif new_lead_pos[1] - follow_pos[1] == 2:
            new_follow_pos = (new_lead_pos[0]+1, new_lead_pos[1]+1)
        else:
            new_follow_pos = (new_lead_pos[0]+1, new_lead_pos[1])
    elif new_lead_pos[1] - follow_pos[1] == 2:
        if new_lead_pos[0] - follow_pos[0] == 2:
            new_follow_pos = (new_lead_pos[0]+1, new_lead_pos[1] - 1)
        elif new_lead_pos[0] - follow_pos[0] == -2:
            new_follow_pos = (new_lead_pos[0]-1, new_lead_pos[1] - 1)
        else:
            new_follow_pos = (new_lead_pos[0], new_lead_pos[1]-1)
    elif new_lead_pos[1] - follow_pos[1] == -2:
        if new_lead_pos[0] - follow_pos[0] == 2:
            new_follow_pos = (new_lead_pos[0]+1, new_lead_pos[1] + 1)
        elif new_lead_pos[0] - follow_pos[0] == 2:
            new_follow_pos = (new_lead_pos[0]-1, new_lead_pos[1] + 1)
        else:
            new_follow_pos = (new_lead_pos[0], new_lead_pos[1]+1)

    return tuple(new_lead_pos), new_follow_pos


def display_knots():
    xs = [pos[0] for pos in knot_positions + tail_visited]
    xmax = max(xs)
    xmin = min(xs)
    x_size = xmax - xmin + 1
    ys = [pos[1] for pos in knot_positions + tail_visited]
    ymax = max(ys)
    ymin = min(ys)
    y_size = ymax - ymin + 1

    grid = [['-'] * x_size for _ in range(y_size)]
    grid[-ymin][-xmin] = 's'

    for knot_num in range(len(knot_positions)-1, -1, -1):
        knot_position = knot_positions[knot_num]
        if knot_num == 0:
            knot_id = 'H'
        else:
            knot_id = str(knot_num)
        try:
            grid[knot_position[1]-ymin][knot_position[0]-xmin] = knot_id
        except IndexError:
            breakpoint()

    print('')
    for row in reversed(grid):
        print(''.join(row))


# %% Part 2, test 1
knot_positions = [(0, 0)] * 10
tail_visited = [(0, 0)]

moves = Path('day09_test.txt').read_text().splitlines()

for move in moves:
    print(f'\n== {move} ==\n')
    move_dir, distance = move.strip().split(' ')
    for _ in range(int(distance)):
        knot_positions[0] = move_head(move_dir, knot_positions[0])
        for knot_num in range(9):
            lead_pos = knot_positions[knot_num]
            follow_pos = knot_positions[knot_num + 1]
            knot_positions[knot_num], knot_positions[knot_num + 1] = propogate_move(lead_pos, follow_pos)
        tail_visited.append(knot_positions[-1])

        display_knots()

print(f'Total places tail went: {len(set(tail_visited))}')

# %% Part 2, test 2
knot_positions = [(0, 0)] * 10
tail_visited = [(0, 0)]

moves = Path('day09_test2.txt').read_text().splitlines()

for move in moves:
    print(f'\n== {move} ==')
    move_dir, distance = move.strip().split(' ')
    for _ in range(int(distance)):
        knot_positions[0] = move_head(move_dir, knot_positions[0])
        for knot_num in range(9):
            lead_pos = knot_positions[knot_num]
            follow_pos = knot_positions[knot_num + 1]
            knot_positions[knot_num], knot_positions[knot_num + 1] = propogate_move(lead_pos, follow_pos)
        tail_visited.append(knot_positions[-1])

    display_knots()

print(f'Total places tail went: {len(set(tail_visited))}')

# %% Part 2, puzzle
knot_positions = [(0, 0)] * 10
tail_visited = [(0, 0)]

moves = Path('day09.txt').read_text().splitlines()

for move in moves:
    # print(f'\n== {move} ==')
    move_dir, distance = move.strip().split(' ')
    for _ in range(int(distance)):
        knot_positions[0] = move_head(move_dir, knot_positions[0])
        for knot_num in range(9):
            lead_pos = knot_positions[knot_num]
            follow_pos = knot_positions[knot_num + 1]
            knot_positions[knot_num], knot_positions[knot_num + 1] = propogate_move(lead_pos, follow_pos)
        tail_visited.append(knot_positions[-1])

    # display_knots()

print(f'Total places tail went: {len(set(tail_visited))}')
