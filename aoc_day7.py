# advent of code day 7

from operator import itemgetter

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

def simulate_quantum_beams(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = find_start(grid)
    paths_counts = {pos: 1 if pos == (start_row, start_col) else 0 
                    for pos in [(r, c) for r in range(rows) for c in range(cols)]}
    for r in range(start_row, rows-1):
        for c in range(cols):
            if paths_counts[(r,c)] > 0 and grid[r+1][c] == '.':
                # tachyon beams go down through empty space(.)
                paths_counts[(r+1, c)] += paths_counts[(r, c)]
            elif paths_counts[(r,c)] > 0 and grid[r+1][c] == '^':                
                # otherwise tachyon beams gets split at splitter (^)
                # add left and right positions to frontier if they are withon bounds and not already present
                if c-1 >= 0:
                    paths_counts[(r+1, c-1)] += paths_counts[(r, c)]
                if c+1 < cols:
                    paths_counts[(r+1, c+1)] += paths_counts[(r, c)]
    # sum all paths that reached the bottom row
    return sum(map(itemgetter(1), filter(lambda x: x[0][0] == rows-1, paths_counts.items())))

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
    sample_grid = parse_input(sample_input)
    print_grid(sample_grid)
    beam_splits = simulate_beam(sample_grid)
    print("Number of beam splits:", beam_splits)

    print("Real input:")
    with open('aoc_input_day7.txt', 'r') as f:
        grid = parse_input(f.read())
    print_grid(grid)
    beam_splits = simulate_beam(grid)
    print("Number of beam splits:", beam_splits)

    # # part 2
    beams_count = simulate_quantum_beams(sample_grid)
    print("Number of beams in sample:", beams_count)
    beams_count = simulate_quantum_beams(grid)
    print("Number of beams in puzzle:", beams_count)



