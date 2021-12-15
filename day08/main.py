from os.path import dirname, realpath
from typing import List
from collections import Counter


def part1(data: List[dict]) -> int:
    known_segment_counts = [
        7, # 8
        3, # 7
        4, # 4
        2, # 1
    ]
    recognisable_segments = []
    for item in data:
        matches = [segment for segment in item['output'] if len(segment) in known_segment_counts]
        recognisable_segments += matches

    return len(recognisable_segments)

def sort_word(word: str) -> str:
    return ''.join(sorted(word))

def remove_chars(word: str, chars: str) -> str:
    return word.translate(str.maketrans('', '', chars))

def decode_signal(signal: List[str]) -> dict:
    number_to_code = {
        1: sort_word(signal[0]),
        7: sort_word(signal[1]),
        4: sort_word(signal[2]),
        8: sort_word(signal[9]),
    }
    for word in signal[3:-1]:
        if len(word) == 5:
            if len(remove_chars(word, number_to_code[1])) == 3:
                number_to_code[3] = sort_word(word)
            elif len(remove_chars(word, number_to_code[4])) == 3:
                number_to_code[2] = sort_word(word)
            elif len(remove_chars(word, number_to_code[4])) == 2:
                number_to_code[5] = sort_word(word)
            else:
                raise Exception(f"cannot decode {word = }")
        elif len(word) == 6:
            if len(remove_chars(word, number_to_code[1])) == 5:
                number_to_code[6] = sort_word(word)
            elif len(remove_chars(word, number_to_code[4])) == 3:
                number_to_code[0] = sort_word(word)
            elif len(remove_chars(word, number_to_code[4])) == 2:
                number_to_code[9] = sort_word(word)
            else:
                raise Exception(f"cannot decode {word = }")
        else:
            raise Exception(f"cannot decode {word = }, unexpected lenght")
    return {code: number for number, code in number_to_code.items()}

def part2(data: List[int]) -> int:
    """ decode by checking segment lenght difference between known numbers
    (because of their lenght, part 1). Reference:
          dddd
         e    a
         e    a
          ffff
         g    b
         g    b
          cccc
        len = 5: 2 3 5
        len = 6: 6 9 0
    """
    total_output = 0
    for item in data:
        code_to_number = decode_signal(sorted(item['signal'], key=len))
        numeric = ''
        for word in item['output']:
            numeric += str(code_to_number[sort_word(word)])
        total_output += int(numeric)

    return total_output


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    for file_name in ["test_input.txt", "input.txt"]:
        with open(f"{dir_path}/{file_name}") as input_file:
            data = [line.split('|') for line in input_file]
            data = [{'signal': line[0].strip().split(' '), 'output': line[1].strip().split(' ')} for line in data]
            print(f"part1: {file_name}: {part1(data)}")
            print(f"part2: {file_name}: {part2(data)}")
