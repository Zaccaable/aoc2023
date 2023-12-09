import re


def find_calibration_value(pattern: str, lines: list) -> int:
    number_translation = {
        "1": "1",
        "one": "1",
        "2": "2",
        "two": "2",
        "3": "3",
        "three": "3",
        "4": "4",
        "four": "4",
        "5": "5",
        "five": "5",
        "6": "6",
        "six": "6",
        "7": "7",
        "seven": "7",
        "8": "8",
        "eight": "8",
        "9": "9",
        "nine": "9",
    }
    calibration_values = []
    for line in lines:
        numbers = re.findall(pattern, line)
        calibration_values.append(int(number_translation.get(
            numbers[0])+number_translation.get((numbers[-1]))))
    return sum(calibration_values)


if __name__ == '__main__':

    with open('day1_input.txt', 'r') as f:
        content = f.read()

    lines = content.splitlines()
    value_part_1 = find_calibration_value("\d", lines)
    print(
        f'For part 1 the sum of all of the calibration values is: {value_part_1}')

    value_part_2 = find_calibration_value(
        r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', lines)
    print(
        f'For part 1 the sum of all of the calibration values is: {value_part_2}')
