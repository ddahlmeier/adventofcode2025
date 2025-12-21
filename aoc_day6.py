# advent of code day 6

from collections import defaultdict
import operator

sample_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def parse_input(input_str):
    def map_operators(op_str):
        if op_str == '+':
            return operator.add
        elif op_str == '*':
            return operator.mul
        else:
            raise ValueError(f"Unknown operator: {op_str}")

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
    print("Sample input:")
    math_problems, operators = parse_input(sample_input)
    results = process_all(math_problems, operators)
    print("Results:", sum(results))

    print("Real input")
    with open('aoc_input_day6.txt', 'r') as f:
        puzzle_input = f.read()
    math_problems, operators = parse_input(puzzle_input)
    results = process_all(math_problems, operators)
    print("Results:", sum(results))
