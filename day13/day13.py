#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path
from itertools import zip_longest
from functools import cmp_to_key


#%% Part 1 functions
def compare(item1, item2):
    print(f'{item1}, {item2}: ', end='')
    match item1, item2:
        case int(a), int(b):
            print('Two ints')
            if a < b:
                return True
            if a > b:
                return False
            else:
                return None
        case left, None:
            print('Any, None')
            return False
        case None, right:
            print('None, any')
            return True
        case list(left), list(right):
            print('Two lists')
            for a, b in zip_longest(left, right, fillvalue=None):
                result = compare(a, b)
                if result is not None:
                    return result
            return None
        case list(left), int(right):
            return compare(left, [right])
        case int(left), list(right):
            return compare([left], right)
        case _:
            raise ValueError(f'Unmatched case: {item1, item2}')


def check_pairs(input_path):
    lines = [i.strip() for i in Path(input_path).read_text().splitlines()]

    total = 0
    for pairnum, (line1, line2) in enumerate(zip(lines[::3], lines[1::3])):
        item1 = eval(line1)
        item2 = eval(line2)

        if compare(item1, item2):
            total += pairnum + 1
    return total


#%% Part 1, test
print(f"Total: {check_pairs('day13_test.txt')}")


#%% Part 1, puzzle
print(f"Total: {check_pairs('day13.txt')}")


#%% Part 2 functions
def compare2(item1, item2):
    match item1, item2:
        case int(a), int(b):
            if a < b:
                return -1
            if a > b:
                return 1
            else:
                return None
        case left, None:
            return 1
        case None, right:
            return -1
        case list(left), list(right):
            for a, b in zip_longest(left, right, fillvalue=None):
                result = compare2(a, b)
                if result is not None:
                    return result
            return None
        case list(left), int(right):
            return compare2(left, [right])
        case int(left), list(right):
            return compare2([left], right)
        case _:
            raise ValueError(f'Unmatched case: {item1, item2}')


#%% Part 2, test
input_path = 'day13_test.txt'

packets = [eval(i.strip()) for i in Path(input_path).read_text().splitlines() if i.strip()]
dividers = [[[2]], [[6]]]
packets.extend(dividers)
s = sorted(packets, key=cmp_to_key(compare2))

print(f'Decoder key: {(s.index(dividers[0]) + 1) * (s.index(dividers[1]) + 1)}')


# %% Part 2, puzzle
input_path = 'day13.txt'

packets = [eval(i.strip()) for i in Path(input_path).read_text().splitlines() if i.strip()]
dividers = [[[2]], [[6]]]
packets.extend(dividers)
s = sorted(packets, key=cmp_to_key(compare2))

print(f'Decoder key: {(s.index(dividers[0]) + 1) * (s.index(dividers[1]) + 1)}')
