from os.path import dirname, realpath
from collections import defaultdict, Counter
from re import compile


def findEdges(paths: list[tuple[str, str]]) -> dict[str: set[str]]:
    edges = defaultdict(set)
    for start, destination in paths:
        edges[start].add(destination)
        edges[destination].add(start)

    return edges


def canVisitCave(cave: str, path: tuple[str], times=2) -> bool:
    is_small_cave = cave.islower()

    if not is_small_cave:
        return True

    if cave == 'start' and cave in path:
        return False

    if is_small_cave and cave not in path:
        return True

    caves_visited = Counter(path)
    if is_small_cave and not [c for c, t in caves_visited.items() if c.islower() and t >= times]:
        return True

    return False


def part1(paths: list[tuple[str, str]]) -> int:
    edges = findEdges(paths)

    visited = set()
    to_visit = [('start', )]
    while to_visit:
        path = to_visit.pop()

        if path[-1] == 'end':
            visited.add(path)
            continue

        for target in edges[path[-1]]:
            if not target.islower() or target not in path:
                to_visit.append((*path, target))

    return len(visited)


def part2(paths: list[tuple[str, str]]) -> int:
    edges = findEdges(paths)

    visited = set()
    to_visit = [('start', )]
    while to_visit:
        path = to_visit.pop()

        if path[-1] == 'end':
            visited.add(path)
            continue

        for cave in edges[path[-1]]:
            if canVisitCave(cave, path):
                to_visit.append((*path, cave))

    return len(visited)


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [line.strip().split('-') for line in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
    