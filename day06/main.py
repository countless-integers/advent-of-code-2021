from os.path import dirname, realpath
from typing import List
from collections import Counter


def part1(data: List[int], days: int) -> int:
    tally = data[:]
    for _ in range(1, days + 1):
        new_day_tally = []
        for fishy in tally:
            if fishy == 0:
                new_day_tally.append(6)
                new_day_tally.append(8)
                continue
            new_day_tally.append(fishy - 1)
        tally = new_day_tally[:]
            
    return len(tally)


def part2(data: List[int], days: int) -> int:
    counter = Counter(data)
    for _ in range(1, days + 1):
        new_day = {}
        for day, count in counter.items():
            if day == 0:
                if 6 not in new_day: 
                    new_day[6] = 0
                new_day[6] += count
                if 8 not in new_day:
                    new_day[8] = 0
                new_day[8] += count
                continue

            if day - 1 not in new_day:
                new_day[day - 1] = 0
            new_day[day - 1] += count

        counter = new_day
        
    return sum(counter.values())


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [int(i) for i in list(input_file)[0].strip().split(',')]
            print(f"part1: {file_name}: {part1(data, 80)}")
            print(f"part2: {file_name}: {part2(data, 256)}")
