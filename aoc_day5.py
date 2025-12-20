# advent of code 2025 day 5

def parse_input(puzzle_input):
    sections = puzzle_input.strip().split("\n\n")
    fresh_ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split('-'))
        fresh_ranges.append((start, end))
    
    ingridients = [int(line) for line in sections[1].splitlines()]
    return fresh_ranges, ingridients

def is_fresh(fresh_ranges, ingridient):
    return any(start <= ingridient <= end for start, end in fresh_ranges)

if __name__ == "__main__":
    puzzle_sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    # fresh_ranges, ingridients = parse_input(puzzle_sample)
    with open('aoc_input_day5.txt', 'r') as f:
        puzzle_input = f.read()
    fresh_ranges, ingridients = parse_input(puzzle_input)
    answer = sum((1 if is_fresh(fresh_ranges, ingridient) else 0 for ingridient in ingridients))
    print(f"Number of fresh ingridients: {answer}")


