from day01_circuitpython import part1, part2


def total_calories_by_elf(input_file_path: str):
    calories = [0]
    line_num = -1
    with open(input_file_path, 'r') as f:
        while (line := f.readline()) != '':
            line_num += 1
            line = line.strip()
            if line == '':
                calories.append(0)
            else:
                calories[-1] += int(line)

    print(f'{line_num} lines (CPython)')
    return calories
