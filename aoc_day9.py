# advent of code day 9

from operator import itemgetter
from itertools import combinations

def parse_input(puzzle_input):
    return [tuple(map(int, item.split(","))) for item in puzzle_input.strip().splitlines()]

def print_tiles(tiles):
    max_x = max(map(itemgetter(0), tiles))
    max_y = max(map(itemgetter(1), tiles))

    for y in range(max_y+2):
        for x in range(max_x+3):
            if (x, y) in tiles:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

def size(t1, t2):
    return (abs(t2[0]-t1[0])+1) * (abs(t2[1]-t1[1])+1)

def rectangles_naive(tiles):
    for t1, t2 in combinations(tiles, r=2):
        yield ((t1, t2), size(t1, t2))

def largest_recangle(tiles):
    return max(list(rectangles_naive(tiles)), key=itemgetter(1))


if __name__ == "__main__":
    sample_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    # part 1
    # sample
    tiles_sample = parse_input(sample_input)
    print_tiles(tiles_sample)
    print("Largest rectangle (sample): ", largest_recangle(tiles_sample))

    # puzzle input
    with open("aoc_input_day9.txt", "r") as f:
        tiles = parse_input(f.read())
    print("Largest rectangle (puzzle): ", largest_recangle(tiles))
