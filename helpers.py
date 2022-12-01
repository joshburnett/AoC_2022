def parse_test_input(day: int):
    lines = open(f'AOC inputs/day{day:02d}_test.txt', 'r').readlines()

    test_inputs = []

    inputs_done = False
    for line in lines:
        if not inputs_done:
            if not line.startswith('~'):
                test_inputs.append(line.strip())  # strip off the ending '\n' or '\r\n'
            else:
                inputs_done = True
        else:
            test_answer = int(line.split(' ')[1])

    return test_inputs, test_answer
