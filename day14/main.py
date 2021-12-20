from os.path import dirname, realpath
from collections import Counter


def part1(polymer_template: str, pair_insertion_rules: dict[str: str], steps=10) -> int:
    pairs = Counter()
    for i in range(0, len(polymer_template) - 1):
        pairs[polymer_template[i] + polymer_template[i + 1]] = 1

    while steps:
        updated_pairs = Counter()
        for pair, count in pairs.items():
            updated_pairs[pair[0] + pair_insertion_rules[pair]] += count
            updated_pairs[pair_insertion_rules[pair] + pair[1]] += count
        pairs = updated_pairs
        steps -= 1

    letter_count = Counter()
    for pair, count in pairs.items():
        letter_count[pair[0]] += count

    # correct off-by-one
    letter_count[polymer_template[-1]] += 1

    print(letter_count)

    return max(letter_count.values()) - min(letter_count.values())


def part2():
    pass


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
    # for file_name in ["input.txt"]:
    # for file_name in ["test_input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            polymer_template = ''
            pair_insertion_rules = {}
            for line in input_file:
                line = line.strip()
                if line == '':
                    continue
                if '-' in line:
                    key, value = line.split(' -> ')
                    pair_insertion_rules[key] = value
                else:
                    polymer_template = line

            print(f"part1: {file_name}: {part1(polymer_template, pair_insertion_rules)}")
    