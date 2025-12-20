# advent of code 2025 day 5
from operator import itemgetter

def parse_input(puzzle_input):
    sections = puzzle_input.strip().split("\n\n")
    fresh_ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split('-'))
        fresh_ranges.append((start, end))
    
    ingredients = [int(line) for line in sections[1].splitlines()]
    return fresh_ranges, ingredients

def is_fresh(fresh_ranges, ingredient):
    return any(start <= ingredient <= end for start, end in fresh_ranges)

def solve_part2(fresh_ranges):
    ranges_sorted = sorted(fresh_ranges, key=itemgetter(0))
    range_start, range_end = ranges_sorted[0]
    total = 0
    for r in ranges_sorted[1:]:
        start, end = r
        if start <= range_end:
            range_end = max(range_end, end)
        else:
            total += (range_end - range_start + 1)
            range_start, range_end = start, end
    total += (range_end - range_start + 1)
    return total

if __name__ == "__main__":
    with open('aoc_input_day5.txt', 'r') as f:
        puzzle_input = f.read()
    fresh_ranges, ingredients = parse_input(puzzle_input)
    
    # Part 1
    answer1 = sum((1 if is_fresh(fresh_ranges, ingredient) else 0 for ingredient in ingredients))
    print(f"Number of fresh ingredients: {answer1}")

    # Part 2
    answer2 = solve_part2(fresh_ranges)
    print("total fresh ingredients:", answer2)
