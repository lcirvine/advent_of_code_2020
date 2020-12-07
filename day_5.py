import os


with open(os.path.join('Inputs', 'day_5.txt')) as f_input:
    data = f_input.read().split('\n')


def halver(num, letter, divisions: int = 2):
    half_1 = num // divisions
    half_2 = num - half_1
    if letter in ['F', 'L']:
        return half_1
    elif letter in ['B', 'R']:
        return half_2


def part_1():
    """
    Rows - The first 7 characters will either be F or B; specify exactly one of the 128 rows (0 through 127)
        F means to take the lower half (i.e. lower numbers)
        B means to take the upper half (i.e. higher numbers)
    Columns - The last three characters will be either L or R; specify exactly one of the 8 columns (0 through 7)
        L means to take the lower half (i.e. lower numbers)
        R means to take the upper half (i.e. higher numbers)
    :return:
    """
    def row():
        pass

    def col():
        pass

    seat


if __name__ == '__main__':
    part_1()
