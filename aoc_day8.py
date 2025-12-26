# advent of code day 8

import math

def parse_input(input_str):
    box_coordinates = []
    for line in input_str.strip().splitlines():
        box_coordinates.append(tuple(map(int, line.strip().split(','))))
    return box_coordinates

def straight_line_distance(box1, box2):
    return sum(math.pow(a-b, 2) for a, b in zip(box1, box2))

def compute_distances(box_coordinates):
    distances = {}
    for first_idx, first_box in enumerate(box_coordinates):
        for second_idx, second_box in enumerate(box_coordinates):
            if first_idx >= second_idx:
                continue
            else:
                distances[(first_box, second_box)] = straight_line_distance(first_box, second_box)
    return distances

def connect_boxes(junction_boxes, max_connections=None, return_final_connection=False):
    distances = compute_distances(junction_boxes)
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    circuits = {box : set([box]) for box in junction_boxes}
    # connect shortest boxes
    if max_connections == None:
        max_connections = len(sorted_distances)
    for (box1, box2), _ in sorted_distances[:max_connections]:
        circuit1 = circuits[box1]
        circuit2 = circuits[box2]
        if circuit1 != circuit2:
            new_circuit = circuit1.union(circuit2)
            for box in new_circuit:
                circuits[box] = new_circuit
        if return_final_connection and len(set(map(frozenset, circuits.values()))) == 1:
            return box1, box2
    circuit_sizes = sorted([len(circuit) for circuit in set(map(frozenset, circuits.values()))], reverse=True)
    return circuit_sizes
    
    
if __name__ == "__main__":
    sample_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

    # part 1
    # Sample input
    junction_boxes_sample = parse_input(sample_input)
    circuit_sizes = connect_boxes(junction_boxes_sample, 10)
    print("Part 1. Product of 3 largest circuit size (sample):", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

    # # Puzzle input
    with open('aoc_input_day8.txt', 'r') as f:
        puzzle_input = f.read()
    junction_boxes = parse_input(puzzle_input)
    circuit_sizes = connect_boxes(junction_boxes, 1000)
    print("Part 1. Product of 3 largest circuit size (puzzle):", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])


    # part 2
    # Sample input
    box1, box2 = connect_boxes(junction_boxes_sample, return_final_connection=True)
    print("Part 2. Product of x coodinates of two last connected boxes (sample):", box1[0] * box2[0])

    # Puzzle input
    box1, box2 = connect_boxes(junction_boxes, return_final_connection=True)
    print("Part 2. Product of x coodinates of two last connected boxes (puzzle):", box1[0] * box2[0])




