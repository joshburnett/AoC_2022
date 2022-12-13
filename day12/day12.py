#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path
from collections import namedtuple

from colorama import Fore, Style


#%% Part 1, test
def letter_2_height(char):
    if char == 'S':
        return 1
    elif char == 'E':
        return 26
    else:
        return ord(char) - ord('a') + 1


Position = namedtuple('Position', ('coordinates', 'before', 'direction', 'order', 'height'))


def check_ascent(rownum: int, colnum: int, from_height: int) -> bool:
    if not (0 <= rownum < numrows) or not (0 <= colnum < numcols) or ((rownum, colnum) in all_visited)\
            or (from_height + 1 < heightmap[rownum][colnum]):
        return False
    else:
        return True


def check_descent(rownum: int, colnum: int, from_height: int) -> bool:
    if not (0 <= rownum < numrows) or not (0 <= colnum < numcols) or ((rownum, colnum) in all_visited)\
            or (from_height - heightmap[rownum][colnum] > 1):
        return False
    else:
        return True


#%%
lines = [i.strip() for i in Path('day12_test.txt').read_text().splitlines()]
heightmap = []
for rownum, line in enumerate(lines):
    row = []
    for colnum, letter in enumerate(line):
        height = letter_2_height(letter)
        row.append(height)
        if letter == 'S':
            start = rownum, colnum
        elif letter == 'E':
            end = rownum, colnum
    heightmap.append(row)

numrows = len(heightmap)
numcols = len(heightmap[0])

#%%
order = 0
start_position = Position(coordinates=start, before=None, direction=None, order=order, height=1)
all_visited = {start: start_position}
visited_this_round = [start_position]
end_found = False
rounds = [visited_this_round]

while not end_found:
    order += 1
    # print(f'Round: {order}')
    last_round = visited_this_round
    visited_this_round = []
    for old_position in last_round:
        new_coords = ((old_position.coordinates[0], old_position.coordinates[1] + 1),
                      (old_position.coordinates[0], old_position.coordinates[1] - 1),
                      (old_position.coordinates[0] + 1, old_position.coordinates[1]),
                      (old_position.coordinates[0] - 1, old_position.coordinates[1]))
        directions = ('right', 'left', 'down', 'up')
        height = heightmap[old_position.coordinates[0]][old_position.coordinates[1]]
        for direction, coords in zip(directions, new_coords):
            if check_ascent(coords[0], coords[1], height):
                new_position = Position(coordinates=coords, before=old_position.coordinates,
                                        direction=direction, order=order, height=heightmap[coords[0]][coords[1]])
                visited_this_round.append(new_position)
                all_visited[coords] = new_position
                if coords == end:
                    end_position = new_position
                    end_found = True
                    pp(visited_this_round)
                    # print('Found it!')
                    break
        if end_found:
            # print('Found it (2)')
            break

    # pp(visited_this_round)

    rounds.append(visited_this_round)

if end_found:
    print(f'Found it: Round {order}')

# %% Retrace path
path = [end_position.coordinates]
while position := all_visited[path[-1]].before:
    if position == path[-1]:
        print('Duplicate!')
    path.append(position)

# %% Print colored path
special = False
for row, (row_heights, row_chars) in enumerate(zip(heightmap, lines)):
    for col, (height, char) in enumerate(zip(row_heights, row_chars)):
        if char in 'SE':
            print(Fore.BLUE, end='')
            special = True
        elif (row, col) in path:
            print(Fore.RED, end='')
            special = True

        print(char, end='')

        if special:
            print(Style.RESET_ALL, end='')
            special = False
    print('')

#%% Part 2, test
lines = [i.strip() for i in Path('day12_test.txt').read_text().splitlines()]
heightmap = []
for rownum, line in enumerate(lines):
    row = []
    for colnum, letter in enumerate(line):
        height = letter_2_height(letter)
        row.append(height)
        if letter == 'S':
            start = rownum, colnum
        elif letter == 'E':
            end = rownum, colnum
    heightmap.append(row)

numrows = len(heightmap)
numcols = len(heightmap[0])

order = 0
end_position = Position(coordinates=end, before=None, direction=None, order=order, height=1)
all_visited = {end: end_position}
visited_this_round = [end_position]
start_found = False
rounds = [visited_this_round]

while not start_found:
    order += 1
    # print(f'Round: {order}')
    last_round = visited_this_round
    visited_this_round = []
    for old_position in last_round:
        new_coords = ((old_position.coordinates[0], old_position.coordinates[1] + 1),
                      (old_position.coordinates[0], old_position.coordinates[1] - 1),
                      (old_position.coordinates[0] + 1, old_position.coordinates[1]),
                      (old_position.coordinates[0] - 1, old_position.coordinates[1]))
        directions = ('right', 'left', 'down', 'up')
        height = heightmap[old_position.coordinates[0]][old_position.coordinates[1]]
        for direction, coords in zip(directions, new_coords):
            if check_descent(coords[0], coords[1], height):
                new_position = Position(coordinates=coords, before=old_position.coordinates,
                                        direction=direction, order=order, height=heightmap[coords[0]][coords[1]])
                visited_this_round.append(new_position)
                all_visited[coords] = new_position
                if heightmap[coords[0]][coords[1]] == 1:
                    start_position = new_position
                    start_found = True
                    pp(visited_this_round)
                    # print('Found it!')
                    break
        if start_found:
            # print('Found it (2)')
            break

    # pp(visited_this_round)

    rounds.append(visited_this_round)

if start_found:
    print(f'Found it: Round {order}')

# %% Retrace path
path = [end_position.coordinates]
while position := all_visited[path[-1]].before:
    if position == path[-1]:
        print('Duplicate!')
    path.append(position)

# %% Print colored path
special = False
for row, (row_heights, row_chars) in enumerate(zip(heightmap, lines)):
    for col, (height, char) in enumerate(zip(row_heights, row_chars)):
        if char in 'SE':
            print(Fore.BLUE, end='')
            special = True
        elif (row, col) in path:
            print(Fore.RED, end='')
            special = True

        print(char, end='')

        if special:
            print(Style.RESET_ALL, end='')
            special = False
    print('')


#%% Part 1, puzzle
lines = [i.strip() for i in Path('day12.txt').read_text().splitlines()]
heightmap = []
for rownum, line in enumerate(lines):
    row = []
    for colnum, letter in enumerate(line):
        height = letter_2_height(letter)
        row.append(height)
        if letter == 'S':
            start = rownum, colnum
        elif letter == 'E':
            end = rownum, colnum
    heightmap.append(row)

numrows = len(heightmap)
numcols = len(heightmap[0])

order = 0
start_position = Position(coordinates=start, before=None, direction=None, order=order, height=1)
all_visited = {start: start_position}
visited_this_round = [start_position]
end_found = False
rounds = [visited_this_round]

while not end_found:
    order += 1
    # print(f'Round: {order}')
    last_round = visited_this_round
    visited_this_round = []
    for old_position in last_round:
        new_coords = ((old_position.coordinates[0], old_position.coordinates[1] + 1),
                      (old_position.coordinates[0], old_position.coordinates[1] - 1),
                      (old_position.coordinates[0] + 1, old_position.coordinates[1]),
                      (old_position.coordinates[0] - 1, old_position.coordinates[1]))
        directions = ('right', 'left', 'down', 'up')
        height = heightmap[old_position.coordinates[0]][old_position.coordinates[1]]
        for direction, coords in zip(directions, new_coords):
            if check_ascent(coords[0], coords[1], height):
                new_position = Position(coordinates=coords, before=old_position.coordinates,
                                        direction=direction, order=order, height=heightmap[coords[0]][coords[1]])
                visited_this_round.append(new_position)
                all_visited[coords] = new_position
                if coords == end:
                    end_position = new_position
                    end_found = True
                    pp(visited_this_round)
                    # print('Found it!')
                    break
        if end_found:
            # print('Found it (2)')
            break

    # pp(visited_this_round)

    rounds.append(visited_this_round)

if end_found:
    print(f'Found it: Round {order}')

path = [end_position.coordinates]
while position := all_visited[path[-1]].before:
    path.append(position)


# %% Print colored path
special = False
for row, (row_heights, row_chars) in enumerate(zip(heightmap, lines)):
    for col, (height, char) in enumerate(zip(row_heights, row_chars)):
        if char in 'SE':
            print(Fore.BLUE, end='')
            special = True
        elif (row, col) in path:
            print(Fore.RED, end='')
            special = True

        print(char, end='')

        if special:
            print(Style.RESET_ALL, end='')
            special = False
    print('')


# %% Part 2, puzzle
lines = [i.strip() for i in Path('day12.txt').read_text().splitlines()]
heightmap = []
for rownum, line in enumerate(lines):
    row = []
    for colnum, letter in enumerate(line):
        height = letter_2_height(letter)
        row.append(height)
        if letter == 'S':
            start = rownum, colnum
        elif letter == 'E':
            end = rownum, colnum
    heightmap.append(row)

numrows = len(heightmap)
numcols = len(heightmap[0])

order = 0
end_position = Position(coordinates=end, before=None, direction=None, order=order, height=1)
all_visited = {end: end_position}
visited_this_round = [end_position]
start_found = False
rounds = [visited_this_round]

while not start_found:
    order += 1
    # print(f'Round: {order}')
    last_round = visited_this_round
    visited_this_round = []
    for old_position in last_round:
        new_coords = ((old_position.coordinates[0], old_position.coordinates[1] + 1),
                      (old_position.coordinates[0], old_position.coordinates[1] - 1),
                      (old_position.coordinates[0] + 1, old_position.coordinates[1]),
                      (old_position.coordinates[0] - 1, old_position.coordinates[1]))
        directions = ('right', 'left', 'down', 'up')
        height = heightmap[old_position.coordinates[0]][old_position.coordinates[1]]
        for direction, coords in zip(directions, new_coords):
            if check_descent(coords[0], coords[1], height):
                new_position = Position(coordinates=coords, before=old_position.coordinates,
                                        direction=direction, order=order, height=heightmap[coords[0]][coords[1]])
                visited_this_round.append(new_position)
                all_visited[coords] = new_position
                if heightmap[coords[0]][coords[1]] == 1:
                    start_position = new_position
                    start_found = True
                    pp(visited_this_round)
                    # print('Found it!')
                    break
        if start_found:
            # print('Found it (2)')
            break

    # pp(visited_this_round)

    rounds.append(visited_this_round)

if start_found:
    print(f'Found it: Round {order}')