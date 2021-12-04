from os.path import dirname, realpath


def part1(input: list) -> int:
    gamma_rate, epsilon_rate = '', ''

    x_max = len(input[0])
    y_max = len(input)

    for x in range(x_max):
        ones, zeros = 0, 0
        for y in range(y_max):
            if input[y][x] == '1':
                ones += 1
            else: 
                zeros += 1

            if ones > y_max/2:
                gamma_rate += '1'
                break

            if zeros > y_max/2:
                gamma_rate += '0'
                break

    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def o2_rater(numbers: list, i: int) -> list:
    if len(numbers) == 1:
        return numbers

    ones, zeros = [], []
    for number in numbers:
        if number[i] == "1":
            ones.append(number)
        else:
            zeros.append(number)

    if len(ones) >= len(zeros):
        return o2_rater(ones, i+1)

    return o2_rater(zeros, i+1)


def co2_rater(numbers: list, i: int) -> int:
    if len(numbers) == 1:
        return numbers

    ones, zeros = [], []
    for number in numbers:
        if number[i] == "1":
            ones.append(number)
        else:
            zeros.append(number)

    if len(ones) < len(zeros):
        return co2_rater(ones, i+1)

    return co2_rater(zeros, i+1)


def part2(input: list) -> int:
    o2_gen_rating = o2_rater(input, 0)[0]
    co2_scrubber_rating = co2_rater(input, 0)[0]

    print(f"{o2_gen_rating = }, {co2_scrubber_rating = }")

    return int(o2_gen_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [row.strip() for row in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
