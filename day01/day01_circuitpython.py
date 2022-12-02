python_runtime = {'name': None}


#%%
def total_calories_by_elf(input_file_path: str):
    calories = [0]
    line_num = -1
    with open(input_file_path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                line_num += 1
                line = line.strip()
                if line == '':
                    calories.append(0)
                else:
                    calories[-1] += int(line)

    print(f'{line_num} lines ({python_runtime["name"]})')
    return calories


#%%
def part1(calories_list):
    max_cals = max(calories_list)
    max_elf = calories_list.index(max_cals)
    print(f'Max calories: {max_cals}, carried by elf #{max_elf+1}')
    return max_cals


#%%
def part2(calories_list):
    top_3_cals_total = sum(sorted(calories_list)[-3:])
    print(f'Total calories of top 3 elves: {top_3_cals_total}')
    return top_3_cals_total
