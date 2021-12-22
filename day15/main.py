from os.path import dirname, realpath
from typing import Generator
import heapq


def getAdjacentPointTo(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if abs(i) == abs(j):
                continue
            yield (x + i, y + j)


def print_levels(levels: dict[tuple[int, int]], end: tuple[int, int]):
    for y in range(end[1] + 1):
        print()
        for x in range(end[0] + 1):
            print(levels[x,y], end='')
    print()


def scale_risk_levels(risk_levels: dict[tuple[int, int]], times: int, x_bound: int, y_bound: int) -> dict[tuple[int, int]: int]:
    new_levels = {}
    width, height = x_bound + 1, y_bound + 1
    new_end = (times * width - 1, times * height - 1)

    for x in range(new_end[0] + 1):
        for y in range(new_end[1] + 1):
            new_risk = risk_levels[x % width, y % height]
            new_risk = new_risk + x // width + y // height
            new_risk = 1 + (new_risk - 1) % 9
            new_levels[x, y] = new_risk

    return new_levels, new_end


def find_path(risk_levels: dict[tuple[int, int]: int], start: tuple[int, int], end: tuple[int, int]) -> int:
    paths = [(0, start)]

    while True:
        total_risk, last_node = heapq.heappop(paths)

        if last_node == end:
            return total_risk

        for point in getAdjacentPointTo(*last_node):
            if point not in risk_levels or risk_levels[point] == '.':
                continue
            heapq.heappush(paths, (total_risk + risk_levels[point], point))
            risk_levels[point] = '.'


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            risk_levels = {}
            start, end = None, None
            for y, line in enumerate(input_file):
                for x, risk in enumerate(list(line.strip())):
                    if not start:
                        start = x, y
                    risk_levels[x, y] = int(risk)
                    end = x, y
            print(f"part1: {file_name}: {find_path(risk_levels.copy(), start, end)}")

            new_levels, new_end = scale_risk_levels(risk_levels.copy(), 5, *end)
            print(f"part2: {file_name}: {find_path(new_levels, start, new_end)}")
