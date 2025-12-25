# advent of code day 6

from collections import defaultdict
import operator

sample_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def map_operators(op_str):
    if op_str == '+':
        return operator.add
    elif op_str == '*':
        return operator.mul
    else:
        raise ValueError(f"Unknown operator: {op_str}")
        
def parse_input_right_to_left(input_str):
    lines = input_str.strip().splitlines()
    ops = list(map(map_operators, lines[-1].split()))
    # find common blanks in all lines
    blank_indices = [[i for i, ch in enumerate(line) if ch == ' '] for line in lines[:-1]]
    common_blanks = set(blank_indices[0])
    for blanks in blank_indices[1:]:
        common_blanks.intersection_update(blanks)
    common_blanks.add(0)
    common_blanks.add(len(lines[0]))
    common_blanks = sorted(list(common_blanks))
    # split each line at common blanks
    math_problems = []
    for col_index in range(len(common_blanks)-1):
        col_values = []
        for line in lines[:-1]:
            # adjust first offset by oen to cut leading space
            start_offset = common_blanks[col_index]+ 1 if col_index > 0 else 0
            col_values.append(line[start_offset:common_blanks[col_index + 1]])
        math_problems.append(col_values)
    # parse numbers from right to left
    results = dict()
    for index, math_problem in enumerate(math_problems):
        math_problem_numbers = []
        num_digits = len(math_problem[0])
        for i in range(num_digits-1, -1, -1):
            math_problem_numbers.append(int(''.join([item[i] for item in math_problem])))
        results[index] = math_problem_numbers
    return results, ops

def parse_input(input_str):
    lines = input_str.strip().splitlines()
    math_problems = defaultdict(list)
    for line in lines[:-1]:
        for col, item in enumerate(line.split()):
            math_problems[col].append(int(item))
    ops = list(map(map_operators, lines[-1].split()))
    return math_problems, ops

def process(math_problems, ops):
    result = math_problems[0]
    for item in math_problems[1:]:
        result = ops(result, item)
    return result

def process_all(math_problems, ops):
    results = []
    for col in range(len(math_problems)):
        res = math_problems[col][0]
        for item in math_problems[col][1:]:
            res = ops[col](res, item)
        results.append(res)
    return results

if __name__ == "__main__":
    # part 1
    math_problems, operators = parse_input(sample_input)
    results = process_all(math_problems, operators)
    print("Part 1 sample input results:", sum(results))

    with open('aoc_input_day6.txt', 'r') as f:
        puzzle_input = f.read()
    math_problems, operators = parse_input(puzzle_input)
    results = process_all(math_problems, operators)
    print("Part 1 real input results:", sum(results))

    # part 2
    math_problems, operators = parse_input_right_to_left(sample_input)
    results = process_all(math_problems, operators)
    print("Part 2 sample input results:", sum(results))

    math_problems, operators = parse_input_right_to_left(puzzle_input)
    results = process_all(math_problems, operators)
    print("Part 2 real input results:", sum(results))

