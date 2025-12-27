# advent of code day 9

from operator import itemgetter
from itertools import combinations

def parse_input(puzzle_input):
    return [tuple(map(int, item.split(","))) for item in puzzle_input.strip().splitlines()]

def print_tiles(tiles, polygon=None):
    max_x = max(map(itemgetter(0), tiles))
    max_y = max(map(itemgetter(1), tiles))
    tiles_set = set(tiles)
    polygon_set = set(polygon) if polygon else None
    for y in range(max_y+2):
        for x in range(max_x+3):
            if (x, y) in tiles_set:
                print("#", end="")
            elif polygon_set and (x, y) in polygon_set:
                print("X", end="")
            else:
                print(".", end="")
        print("")
    print("")

def size(t1, t2):
    return (abs(t2[0]-t1[0])+1) * (abs(t2[1]-t1[1])+1)

def rectangles(tiles):
    for t1, t2 in combinations(tiles, r=2):
        yield ((t1, t2), size(t1, t2))

def largest_recangle(tiles):
    return max((rectangles(tiles)), key=itemgetter(1))

def largest_filled_recangle(tiles, boundary):
    candidates_sorted = sorted(list(rectangles(tiles)), key=itemgetter(1), reverse=True)
    boundary_set = set(boundary)
    print("Total candidates to check:", len(candidates_sorted))
    for candidate in candidates_sorted:
        # rectangl is filled if all rectangle boundary tiles are in the polygon of the overall shape
        r_boundary = rectangle_boundary(candidate)
        print("Checking candidate:", candidate)
        # print("Rectangle boundary:", r_boundary)
        # print("Polygon boundary:", boundary)
        if all (point_in_polygon(point, boundary_set) for point in r_boundary):
            # print("Found filled rectangle:", candidate)
            return candidate
    # did not find any filled rectangle
    # print("No filled rectangle found")
    return None

def rectangle_boundary(rectangle):
    t1, t2 = rectangle[0]
    return polygon_boundary([t1, (t2[0], t1[1]), t2, (t1[0], t2[1])])

def polygon_boundary(points):
    # add tiles between any two connected tiles
    polygon = points[:]
    for t1, t2 in list(zip(points, points[1:])) + [(points[-1], points[0])]:
        # subsequent red tiles are either on same x or same y coordinates
        if t1[0] == t2[0]:  # same x coordinate
            start, end = (t1, t2) if t2[1] > t1[1] else (t2, t1)
            for y in range(start[1]+1, end[1]):
                polygon.append((start[0], y))
        elif t1[1] == t2[1]: # same y coordinate
            start, end = (t1, t2) if t2[0] > t1[0] else (t2, t1)
            for x in range(start[0]+1, end[0]):
                polygon.append((x, start[1]))
    return polygon

def point_in_polygon(point, polygon):
    # point in polygon test using ray-casting algorithm
    # move ray diagonally upward until x or y are zero
    if point in polygon:
        return True
    inside = False
    ray_x, ray_y = point
    while ray_x > 0 and ray_y > 0:
        # move first, then check
        ray_x -= 1
        ray_y -= 1
        if (ray_x, ray_y) in polygon:
            inside = not inside
            # print("Ray from", point, "hits polygon at", (ray_x, ray_y), "-> inside now", inside)
    # print("Point", point, "inside polygon:", inside)
    return inside

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


    # # part 2
    boundary_sample = polygon_boundary(tiles_sample)
    print_tiles(tiles_sample, boundary_sample)
    print("Largest filled rectangle (sample): ", largest_filled_recangle(tiles_sample, boundary_sample))

    boundary_puzzle = polygon_boundary(tiles)
    print("Largest filled rectangle (puzzle): ", largest_filled_recangle(tiles, boundary_puzzle))

