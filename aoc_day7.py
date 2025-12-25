# advent of code day 7

def unique(lst):
    seen = set()
    unique_list = []
    for item in lst:  
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

def parse_input(input_str):
    grid = [line.strip() for line in input_str.strip().splitlines() if line.strip()]
    return grid

def find_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        if 'S' in grid[r]:
            start_row, start_col = r, grid[r].index('S')
            return start_row, start_col
    return None

def print_grid(grid, beams=None):
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if beams and (r, c) in beams:
                print('|', end="")
            else:
                print(ch, end="")
        print("")
    print("---")

def simulate_beam(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = find_start(grid)
    frontier = [(start_row, start_col)]
    beam_positions = []
    beam_splits = 0
    while len(frontier) > 0:
        # explore next position in breath-first manner
        r, c = frontier.pop(0)
        beam_positions.append((r, c))
        # stop if bottom of grid is reached
        if r == rows - 1:
            continue
        # tachyon beams go down through empty space(.)
        if grid[r+1][c] == '.' and (r+1, c) not in frontier:
            frontier.append((r+1, c))
        # otherwise tachyon beams gets split at splitter (^)
        elif grid[r+1][c] == '^':
            #split left and right
            beam_splits +=1
            # add left and right positions to frontier if they are withon bounds and not already present
            if c-1 >= 0 and (r+1, c-1) not in frontier:
                frontier.append((r+1, c-1))
            if c+1 < cols and (r+1, c+1) not in frontier:
                frontier.append((r+1, c+1))
    return beam_splits

if __name__ == "__main__":
    sample_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    # part 1
    print("Sample input:")
    grid = parse_input(sample_input)
    print_grid(grid)
    beam_splits = simulate_beam(grid)
    print("Number of beam splits:", beam_splits)

    print("Real input:")
    with open('aoc_input_day7.txt', 'r') as f:
        grid = parse_input(f.read())
    print_grid(grid)
    beam_splits = simulate_beam(grid)
    print("Number of beam splits:", beam_splits)


