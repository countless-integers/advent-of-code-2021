from os.path import dirname, realpath


def show(points: set[tuple[int, int]]) -> None:
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()

    print()


def part1(points: set[tuple[int, int]], folds: list[tuple[int, int]]) -> set[tuple[int, int]]:
    while folds:
        fold_x, fold_y = folds.pop(0)

        for point in points.copy():
            if fold_x == 0:
                if point[1] == fold_y:
                    points.remove(point)
                elif point[1] > fold_y:
                    points.remove(point)
                    points.add((point[0], 2 * fold_y - point[1]))

            if fold_y == 0:
                if point[0] == fold_x:
                    points.remove(point)
                elif point[0] > fold_x:
                    points.remove(point)
                    points.add((2 * fold_x - point[0], point[1]))
        
    return points


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            points = set()
            folds = []
            for line in input_file:
                line = line.strip()
                if line == '':
                    continue
                if line.startswith('fold'):
                    axis, value = line.replace('fold along ', '').split('=')
                    if axis == 'x':
                        folds.append((int(value), 0))
                    else:
                        folds.append((0, int(value)))
                    continue

                x, y = line.split(',')
                points.add((int(x), int(y)))
            print(f"part1: {file_name}: {len(part1(points.copy(), folds[:1]))}")
            print(f"part2: {file_name}: {show(part1(points.copy(), folds))}")
    