from os.path import dirname, realpath


def parseLine(line: str) -> list[str|None]:
    """Parse line raising ValueError on character mismatch.
       For incomplete lines return missing characters.
    """
    opening = ['{', '[', '(', '<']
    closing = ['}', ']', ')', '>']

    opened = []
    for char in line:
        if char in opening:
            opened.append(char)
        elif char in closing and opened[-1] == opening[closing.index(char)]:
            opened.pop()
        else:
            raise ValueError(char)

    return [closing[opening.index(opener)] for opener in reversed(opened)]


def part1(lines: list[str]) -> int:
    error_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    total_error_score = 0
    for line in lines:
        try:
            parseLine(line)
        except ValueError as e:
            total_error_score += error_scores[str(e)]

    return total_error_score


def part2(lines: list[str]) -> int:
    completion_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    line_scores = []
    for line in lines:
        try:
            line_score = 0
            missing_chars = parseLine(line)
            for char in missing_chars:
                line_score *= 5
                line_score += completion_scores[char]
            line_scores.append(line_score)
        except:
            pass

    return sorted(line_scores)[int(len(line_scores) / 2)]


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [line.strip() for line in input_file]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
    