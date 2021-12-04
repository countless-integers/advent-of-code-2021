from os.path import dirname, realpath


def part1(input: list) -> int:
    x, y = 0, 0
    for instruction in input:
        # if I had 3.10 ...
        #  match instruction[0]:
        #      case 'forward': x + int(instruction[1])
        #      case 'up': x - int(instruction[1])
        #      case 'down': x + int(instruction[1])
        #      case _:
        #          raise Exception(f"Unexpected {instruction = }")

        if instruction[0] == 'forward':
            x += int(instruction[1])
        elif instruction[0] == 'up':
            y -= int(instruction[1])
        elif instruction[0] == 'down':
            y += int(instruction[1])
        else:
            raise Exception(f"Unexpected {instruction = }")

    return x * y


def part2(input: list) -> int:
    x, y, aim = 0, 0, 0
    for instruction in input:
        if instruction[0] == 'forward':
            x += int(instruction[1])
            y += aim * int(instruction[1])
        elif instruction[0] == 'up':
            aim -= int(instruction[1])
        elif instruction[0] == 'down':
            aim += int(instruction[1])
        else:
            raise Exception(f"Unexpected {instruction = }")

    return x * y


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [row.strip().split(' ') for row in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
