# advent of code day 9

from operator import itemgetter
from itertools import combinations

def parse_input(puzzle_input):
    return [tuple(map(int, item.split(","))) for item in puzzle_input.strip().splitlines()]

def print_tiles(tiles, green_tiles=None):
    max_x = max(map(itemgetter(0), tiles))
    max_y = max(map(itemgetter(1), tiles))

    for y in range(max_y+2):
        for x in range(max_x+3):
            if (x, y) in tiles:
                print("#", end="")
            elif green_tiles and (x, y) in green_tiles:
                print("X", end="")
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

def largest_filled_recangle(tiles):
    green_tiles = list(create_green_tiles(tiles))
    red_green = tiles + green_tiles
    return max(list(filter(lambda x: has_only_red_or_green_tiles(x, red_green), rectangles_naive(tiles))), key=itemgetter(1))


def has_only_red_or_green_tiles(rectangle, red_green_tiles):
    (corner1, corner2), _ = rectangle
    step_x = 1 if corner2[0] > corner1[0] else -1
    step_y = 1 if corner2[1] > corner1[1] else -1
    for x in range(corner1[0], corner2[0], step_x):
        for y in range(corner1[1], corner2[1], step_y):
            if (x, y) not in red_green_tiles:
                return False
    return True


def create_green_tiles(red_tiles):
    print("create green tiles")
    green_border = []
    green_inside = []
    # add tiles between two red tiles are green
    for t1, t2 in list(zip(red_tiles, red_tiles[1:])) + [(red_tiles[-1], red_tiles[0])]:
        # subsequent red tiles are either on same x or same y coordinates
        if t1[0] == t2[0]:
            start, end = (t1, t2) if t2[1] > t1[1] else (t2, t1)
            for y in range(start[1], end[1]):
                green_border.append((start[0], y))
        elif t1[1] == t2[1]:
            start, end = (t1, t2) if t2[0] > t1[0] else (t2, t1)
            for x in range(start[0], end[0]):
                green_border.append((x, start[1]))
    print("created border tiles")
    # add any tiles that are enclosed
    max_x = max(map(itemgetter(0), red_tiles))
    max_y = max(map(itemgetter(1), red_tiles))
    border = red_tiles + green_border
    for y in range(max_y):
        for x in range(max_x):
            if is_enclosed((x,y), border):
                green_inside.append((x,y))
    print("created green tiles")
    return green_border + green_inside


def is_enclosed_north(tile, border_tiles):
    return any(tile[0] == other[0] and tile[1] >= other[1] for other in border_tiles)

def is_enclosed_south(tile, border_tiles):
    return any(tile[0] == other[0] and tile[1] <= other[1] for other in border_tiles)

def is_enclosed_west(tile, border_tiles):
    return any(tile[0] >= other[0] and tile[1] ==other[1] for other in border_tiles)

def is_enclosed_east(tile, border_tiles):
    return any(tile[0] <= other[0] and tile[1] ==other[1] for other in border_tiles)

def is_enclosed(tile, border_tiles):
    return is_enclosed_north(tile, border_tiles) and is_enclosed_south(tile, border_tiles) and is_enclosed_west(tile, border_tiles) and is_enclosed_east(tile, border_tiles)


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


    # part 2
    green_tiles_sample = list(create_green_tiles(tiles_sample))
    print_tiles(tiles_sample, green_tiles_sample)
    print("Largest filled rectangle (sample): ", largest_filled_recangle(tiles_sample))
    print("Largest filled rectangle (puzzle): ", largest_filled_recangle(tiles))

