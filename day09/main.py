from os.path import dirname, realpath
from typing import Generator
from functools import reduce


def find_minimas(data: list[int]) -> dict[tuple, int]:
    minimas = {}
    max_row = len(data) - 1
    max_number = len(data[0]) - 1
    for row_index, row in enumerate(data):
        for number_index, number in enumerate(row):
            if number_index != 0 and row[number_index - 1] <= number:
                continue

            if number_index != max_number and row[number_index + 1] <= number:
                continue

            if row_index != 0 and data[row_index - 1][number_index] <= number:
                continue

            if row_index != max_row and data[row_index + 1][number_index] <= number:
                continue

            minimas[(number_index, row_index)] = number

    return minimas


def part1(data: list[int]) -> int:
    minimas = find_minimas(data)
    return sum([value + 1 for value in minimas.values()])


def find_adjacent_to(x, y, data) -> Generator[tuple[int, int], None, None]:
    x_bound, y_bound = len(data[0]) - 1, len(data) - 1
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1
    if x < x_bound:
        yield x + 1, y
    if y < y_bound:
        yield x, y + 1


def part2(data: list[int]) -> int:
    minimas = find_minimas(data)
    basin_bound = 9

    basin_sizes = []
    for x, y in minimas.keys():
        visited = set()
        to_visit = [(x, y)]

        while to_visit:
            a, b = to_visit.pop()
            visited.add((a, b))

            for c, d in find_adjacent_to(a, b, data):
                if (c, d) not in visited and data[d][c] != basin_bound:
                    to_visit.append((c, d))

        basin_sizes.append(len(visited))
        # only keep the top 3
        basin_sizes = sorted(basin_sizes)[-3:]

    return reduce(lambda size, tally: size * tally, basin_sizes)


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
    # for file_name in ["input.txt"]:
    # for file_name in ["test_input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [[int(numeric) for numeric in list(line.strip())] for line in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
