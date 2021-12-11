from os.path import dirname, realpath
from typing import List
from collections import Counter


def part1(data: List[tuple], min_count: int) -> int:
    points = []
    for a, b in data:
        if a[0] == b[0] and a[1] < b[1]: 
            points += [(a[0], y) for y in range(a[1], b[1] + 1)] 
        # N
        elif a[0] == b[0] and a[1] > b[1]: 
            points += [(a[0], y) for y in range(b[1], a[1] + 1)] 
        # E
        elif a[1] == b[1] and a[0] < b[0]: 
            points += [(x, a[1]) for x in range(a[0], b[0] + 1)] 
        # W
        elif a[1] == b[1] and a[0] > b[0]: 
            points += [(x, a[1]) for x in range(b[0], a[0] + 1)] 

    counts = Counter(points)

    overlaps = [point for point, count in counts.items() if count >= min_count]
    return len(overlaps)


def part2(data: List[tuple], min_count: int) -> int:
    points = []
    for a, b in data:
        # S
        if a[0] == b[0] and a[1] < b[1]: 
            points += [(a[0], y) for y in range(a[1], b[1] + 1)] 
        # N
        elif a[0] == b[0] and a[1] > b[1]: 
            points += [(a[0], y) for y in range(b[1], a[1] + 1)] 
        # E
        elif a[1] == b[1] and a[0] < b[0]: 
            points += [(x, a[1]) for x in range(a[0], b[0] + 1)] 
        # W
        elif a[1] == b[1] and a[0] > b[0]: 
            points += [(x, a[1]) for x in range(b[0], a[0] + 1)] 
        # SW
        elif a[0] < b[0] and a[1] < b[1]: 
            points += zip(range(a[0], b[0] + 1), range(a[1], b[1] + 1))
        # NW
        elif a[0] < b[0] and a[1] > b[1]: 
            points += zip(range(a[0], b[0] + 1), range(a[1], b[1] - 1, - 1))
        # SW
        elif a[0] > b[0] and a[1] < b[1]: 
            points += zip(range(b[0], a[0] + 1), range(b[1], a[1] - 1, - 1))
        # NE
        elif a[0] > b[0] and a[1] > b[1]: 
            points += zip(range(b[0], a[0] + 1), range(b[1], a[1] + 1))

    counts = Counter(points)

    overlaps = [point for point, count in counts.items() if count >= min_count]
    return len(overlaps)


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            pairs = [line.strip().split(' -> ') for line in input_file]
            data = []
            for a, b in pairs:
                ax, ay = a.split(',')
                bx, by = b.split(',')
                data.append([(int(ax), int(ay)), (int(bx), int(by))])
            print(f"part1: {file_name}: {part1(data, 2)}")
            print(f"part2: {file_name}: {part2(data, 2)}")
