from os.path import dirname, realpath
from typing import List
from collections import Counter


def part1(data: List[int]) -> int:
    totals = {}
    for i in range(min(data), max(data) + 1):
        total = 0
        for crab in data:
            total += abs(crab - i)
        
        totals[i] = total
        
    return totals[min(totals, key=totals.get)]


def part2(data: List[int]) -> int:
    totals = {}
    for i in range(min(data), max(data) + 1):
        total = 0
        for crab in data:
            distance = abs(crab - i)
            # 1 + 2 + 3 + n... let's get serious! series?
            total += int(distance * (distance + 1) / 2)
        
        totals[i] = total

    return totals[min(totals, key=totals.get)]


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [int(i) for i in list(input_file)[0].strip().split(',')]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
