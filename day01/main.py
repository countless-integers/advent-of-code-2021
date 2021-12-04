from os.path import dirname, realpath


def part1(input: list) -> int:
    return len([x for i, x in enumerate(input[1:]) if x > input[i]])


def part2(input: list) -> int:
    return len([sum(input[i+1:i+4]) for i, x in enumerate(input[1:-2]) if sum(input[i+1:i+4]) > sum(input[i:i+3])])


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [int(row.strip()) for row in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
