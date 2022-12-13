#%% Imports for solving puzzle
import time
from pprint import pp
from pathlib import Path
from collections import deque
from copy import copy


#%% Part 1, test
class Monkey:
    def __init__(self, id, items, operation, operand,
                 divisor, true_monkey: int, false_monkey: int, worry_reduction=3):
        print(f'Creating Monkey {id}')
        self.count = 0
        self.id = id
        self.q = deque(items)
        if operation == '*':
            if operand == 'old':
                self.operation = lambda x: x*x
            else:
                num = int(operand)
                self.operation = lambda x: x*num
        else:
            num = int(operand)
            self.operation = lambda x: x+num
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.worry_reduction = worry_reduction

    def __repr__(self):
        return f'<Monkey {self.id}>'

    def inspect_item(self, item):
        # breakpoint()
        item = self.operation(item) // self.worry_reduction
        # print(f'New value: {item}')
        if not item % self.divisor:
            # print(f'Throwing to {self.true_monkey}')
            monkeys[self.true_monkey].q.append(item)
        else:
            # print(f'Throwing to {self.false_monkey}')
            monkeys[self.false_monkey].q.append(item)

    def inspect_all(self):
        # print(f'\n\nMonkey {self.id} inspecting all...')
        while True:
            num_items = len(self.q)
            if num_items:
                self.count += num_items
                self.inspect_item(self.q.popleft())
            else:
                break


#%% Part 1, test
lines = [i.strip() for i in Path('day11_test.txt').read_text().splitlines()]

monkeys = []

for line in lines:
    print(line)
    if line.startswith('Monkey'):
        monkey_num = int(line[-2])
    elif line.startswith('Starting'):
        items = [int(i) for i in line[16:].split(', ')]
    elif line.startswith('Operation'):
        op, num = line.rsplit(maxsplit=2)[1:]
    elif line.startswith('Test'):
        divisor = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If true'):
        true_monkey = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If false'):
        false_monkey = int(line.rsplit(maxsplit=1)[1])
        monkeys.append(Monkey(id=monkey_num, items=items, operation=op, operand=num,
                              divisor=divisor, true_monkey=true_monkey, false_monkey=false_monkey))

for _ in range(20):
    for monkey in monkeys:
        monkey.inspect_all()

counts = sorted([m.count for m in monkeys])

print(counts[-1] * counts[-2])


#%% Part 1, puzzle
lines = [i.strip() for i in Path('day11.txt').read_text().splitlines()]

monkeys = []

for line in lines:
    print(line)
    if line.startswith('Monkey'):
        monkey_num = int(line[-2])
    elif line.startswith('Starting'):
        items = [int(i) for i in line[16:].split(', ')]
    elif line.startswith('Operation'):
        op, num = line.rsplit(maxsplit=2)[1:]
    elif line.startswith('Test'):
        divisor = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If true'):
        true_monkey = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If false'):
        false_monkey = int(line.rsplit(maxsplit=1)[1])
        monkeys.append(Monkey(id=monkey_num, items=items, operation=op, operand=num,
                              divisor=divisor, true_monkey=true_monkey, false_monkey=false_monkey))

for _ in range(20):
    for monkey in monkeys:
        monkey.inspect_all()

counts = sorted([m.count for m in monkeys])

print(counts[-1] * counts[-2])


# %% Part 2, test
lines = [i.strip() for i in Path('day11_test.txt').read_text().splitlines()]

monkeys = []

for line in lines:
    print(line)
    if line.startswith('Monkey'):
        monkey_num = int(line[-2])
    elif line.startswith('Starting'):
        items = [int(i) for i in line[16:].split(', ')]
    elif line.startswith('Operation'):
        op, num = line.rsplit(maxsplit=2)[1:]
    elif line.startswith('Test'):
        divisor = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If true'):
        true_monkey = int(line.rsplit(maxsplit=1)[1])
    elif line.startswith('If false'):
        false_monkey = int(line.rsplit(maxsplit=1)[1])
        monkeys.append(Monkey(id=monkey_num, items=items, operation=op, operand=num,
                              divisor=divisor, true_monkey=true_monkey, false_monkey=false_monkey,
                              worry_reduction=1))

num_rounds = 1, 20, 50, 100, 200, 500, 600, 700, 750, 800
rounds_so_far = 0
inspections_so_far = 0

for n in num_rounds:
    t0 = time.perf_counter()
    for _ in range(n-rounds_so_far):
        for monkey in monkeys:
            monkey.inspect_all()
    t1 = time.perf_counter()
    print(f'== After round {n} ==')
    for m in monkeys:
        print(f'Monkey {m.id}: {m.count}')
    inspections = sum([m.count for m in monkeys])
    print(f'{inspections-inspections_so_far/(n-rounds_so_far):.1f} inspections/round')
    print(f'{(t1-t0)/(n-rounds_so_far):.2}s/round\n')
    rounds_so_far = n

#%%
num_rounds = 600, 700, 800

for n in num_rounds:
    t0 = time.perf_counter()
    for _ in range(n-rounds_so_far):
        for monkey in monkeys:
            monkey.inspect_all()
    t1 = time.perf_counter()
    print(f'== After round {n} ==')
    for m in monkeys:
        print(f'Monkey {m.id}: {m.count}')
    print(f'{(t1-t0)/(n-rounds_so_far):.2}s/round\n')
    rounds_so_far = n


#%%
counts = sorted([m.count for m in monkeys])

print(counts[-1] * counts[-2])


# %% Part 2, test 2

# %% Part 2, puzzle
