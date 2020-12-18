import os

with open(os.path.join('Inputs', 'day_10.txt')) as f:
    adapters = f.read().split('\n')

adapters = [int(a) for a in adapters]
# adding 0 for the charging outlet
adapters.append(0)
adapters.sort()
# adding +3 to last adapter for device
adapters.append(adapters[-1] + 3)


def part_1():
    diffs = [adapters[x + 1] - adapters[x] for x in range(len(adapters)-1)]
    ones = [x for x in diffs if x == 1]
    threes = [x for x in diffs if x == 3]
    return len(ones) * len(threes)


def part_2():
    adapt_dict = {}
    for x in adapters:
        adapt_dict[x] = [y for y in adapters if y in range(x + 1, x + 4)]
    paths = []



if __name__ == '__main__':
    print(part_1())
    # print(part_2())
