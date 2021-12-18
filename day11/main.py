from os.path import dirname, realpath
from typing import Generator


def getAdjacentPointTo(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i ==  j == 0:
                continue
            yield (x + i, y + j)


def flash(points: dict[tuple[int, int]: int], points_to_flash: set[tuple[int, int]]) -> int:
    flashes = 0

    while points_to_flash:
        point = points_to_flash.pop()

        if points[point] == 0:
            continue

        points[point] = 0
        flashes += 1

        for adj in [adj for adj in getAdjacentPointTo(*point) if adj in points]:
            if points[adj] == 0:
                continue
            points[adj] += 1
            if points[adj] > 9:
                points_to_flash.add(adj)
    
    return flashes


def part1(points: dict[tuple[int, int]: int], phases=100) -> int:
    total_flashes = 0
    points_to_flash = set()
    while phases:
        for point in points:
            points[point] += 1
            if points[point] > 9:
                points_to_flash.add(point)

        if points_to_flash:
            total_flashes += flash(points, points_to_flash)

        phases -= 1

    return total_flashes 


def part2(points: dict[tuple[int, int]: int]) -> int:
    phase = 0
    points_to_flash = set()
    while sum(points.values()) != 0:
        for point in points:
            points[point] += 1
            if points[point] > 9:
                points_to_flash.add(point)

        if points_to_flash:
            flash(points, points_to_flash)

        phase += 1

    return phase 


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = {}
            for y, line in enumerate(input_file):
                for x, numeric in enumerate(list(line.strip())):
                    data[(x, y)] = int(numeric)
            print(f"part1: {file_name}: {part1(data.copy())}")
            print(f"part2: {file_name}: {part2(data.copy())}")
    