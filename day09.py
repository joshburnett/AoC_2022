#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path


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
    for num_num in range(int(distance)):
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
def move_head2(direction):
    new_tail_pos = tail_visited[-1]
    match direction:
        case 'R':
            head_pos[0] += 1
            if head_pos[0] - tail_visited[-1][0] == 2:
                if head_pos[1] - tail_visited[-1][1] == 2:
                    new_tail_pos = (head_pos[0]-1, head_pos[1]-1)
                elif head_pos[1] - tail_visited[-1][1] == -2:
                    new_tail_pos = (head_pos[0]-1, head_pos[1]+1)
                else:
                    new_tail_pos = (head_pos[0]-1, head_pos[1])
        case 'L':
            head_pos[0] -= 1
            if head_pos[0] - tail_visited[-1][0] == -2:
                if head_pos[1] - tail_visited[-1][1] == 2:
                    new_tail_pos = (head_pos[0]+1, head_pos[1]-1)
                elif head_pos[1] - tail_visited[-1][1] == 2:
                    new_tail_pos = (head_pos[0]+1, head_pos[1]+1)
                else:
                    new_tail_pos = (head_pos[0]+1, head_pos[1])
        case 'U':
            head_pos[1] += 1
            if head_pos[1] - tail_visited[-1][1] == 2:
                if head_pos[0] - tail_visited[-1][0] == 2:
                    new_tail_pos = (head_pos[0]+1, head_pos[1] - 1)
                elif head_pos[0] - tail_visited[-1][0] == -2:
                    new_tail_pos = (head_pos[0]-1, head_pos[1] - 1)
                else:
                    new_tail_pos = (head_pos[0], head_pos[1]-1)
        case 'D':
            head_pos[1] -= 1
            if head_pos[1] - tail_visited[-1][1] == -2:
                if head_pos[0] - tail_visited[-1][0] == 2:
                    new_tail_pos = (head_pos[0]+1, head_pos[1] + 1)
                elif head_pos[0] - tail_visited[-1][0] == 2:
                    new_tail_pos = (head_pos[0]-1, head_pos[1] + 1)
                else:
                    new_tail_pos = (head_pos[0], head_pos[1]+1)

    tail_visited.append(new_tail_pos)

tail_visited = [(0, 0)]
head_pos = [0, 0]

moves = Path('day09_test.txt').read_text().splitlines()

for move in moves:
    move_dir, distance = move.strip().split(' ')
    for num_num in range(int(distance)):
        move_head2(move_dir)

print(f'Total places tail went: {len(set(tail_visited))}')

#%%
tail_visited = [(0, 0)]
head_pos = [0, 0]

moves = Path('day09.txt').read_text().splitlines()

for move in moves:
    move_dir, distance = move.strip().split(' ')
    for num_num in range(int(distance)):
        move_head2(move_dir)

print(f'Total places tail went: {len(set(tail_visited))}')
