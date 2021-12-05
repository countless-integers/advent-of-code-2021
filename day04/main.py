from os.path import dirname, realpath
from re import split
from typing import List


def find_winning_round(subset: List[int], numbers: List[int]) -> int:
    for index, number in enumerate(reversed(numbers)):
        if number in subset:
            return len(numbers) - index - 1

    raise Exception(f"no matches from {subset = } in {numbers = }")


def part1(numbers: list, boards: list) -> int:
    winning_board, first_winning_round = None, None
    for board_number, board in enumerate(boards):
        for row in board:
            if all(num in numbers for num in row):
                round = find_winning_round(row, numbers)
                if first_winning_round is None or round < first_winning_round:
                    first_winning_round = round
                    winning_board = board_number

        for i, _ in enumerate(board[0]):
            column = [row[i] for row in board]
            if all(num in numbers for num in column):
                round = find_winning_round(column, numbers)
                if first_winning_round is None or round < first_winning_round:
                    first_winning_round = round
                    winning_board = board_number

    sum_of_others = 0
    matches = set(numbers[:first_winning_round + 1])
    for row in boards[winning_board]:
        for number in row:
            if number not in matches:
                sum_of_others += number

    return sum_of_others * numbers[first_winning_round]


def part2(numbers: list, boards: list) -> int:
    winning_board, last_winning_round = None, None
    for board_number, board in enumerate(boards):
        for row in board:
            if all(num in numbers for num in row):
                round = find_winning_round(row, numbers)
                if last_winning_round is None or round >= last_winning_round:
                    last_winning_round = round
                    winning_board = board_number

        for i, _ in enumerate(board[0]):
            column = [row[i] for row in board]
            if all(num in numbers for num in column):
                round = find_winning_round(column, numbers)
                if last_winning_round is None or round >= last_winning_round:
                    last_winning_round = round
                    winning_board = board_number

    sum_of_others = 0
    matches = set(numbers[:last_winning_round + 1])
    for row in boards[winning_board]:
        for number in row:
            if number not in matches:
                sum_of_others += number

    return sum_of_others * numbers[last_winning_round]


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    # for file_name in ["test_input.txt", "input.txt"]:
    for file_name in ["test_input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            numbers = None
            boards = []
            board = []
            for row in input_file:
                row = row.strip()
                if numbers is None:
                    numbers = [int(number) for number in row.split(',')]
                    continue
                if row:
                    board.append([int(number) for number in split(r"\s+", row)])
                elif board:
                    boards.append(board[:])
                    board = []
            boards.append(board[:])

            print(f"part1: {file_name}: {part1(numbers, boards)}")
            print(f"part2: {file_name}: {part2(numbers, boards)}")
