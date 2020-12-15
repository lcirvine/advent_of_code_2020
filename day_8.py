import os
import re

with open(os.path.join('Inputs', 'day_8.txt')) as f:
    instr = f.read().split('\n')

instr_pat = re.compile(r'^(\w{3})\s([+|-]\d*)$')


def parse_instructions(instuction):
    return re.match(instr_pat, instuction).groups()


def part_1():
    accumulator = 0
    steps_taken = []
    i = 0
    carry_on = True
    while carry_on:
        if i in steps_taken:
            carry_on = False
        else:
            steps_taken.append(i)
        arg, num = parse_instructions(instr[i])
        if arg == 'acc' and carry_on:
            accumulator += int(num)
            i += 1
        elif arg == 'jmp' and carry_on:
            i += int(num)
        elif arg == 'nop' and carry_on:
            i += 1
    return accumulator


def part_2():
    accumulator = 0
    steps_taken = []
    i = 0
    while len(steps_taken) <= len(instr):
        steps_taken.append(i)
        arg, num = parse_instructions(instr[i])
        if arg == 'acc':
            accumulator += int(num)
            i += 1
        elif arg == 'jmp':
            i += int(num)
        elif arg == 'nop':
            i += 1
    return accumulator


if __name__ == '__main__':
    print(part_1())
    # print(part_2())
