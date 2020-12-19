import os

with open(os.path.join('Inputs', 'day_11.txt')) as f:
    data = f.read().split('\n')

seat_map = {}
for x in range(len(data)):
    for y in range(len(data[x])):
        seat_map[(x, y)] = data[x][y]


def adj_seats(seat: tuple):
    adj = []
    sx = seat[0]
    sy = seat[1]
    for nx in range(sx - 1, sx + 2):
        for ny in range(sy - 1, sy + 2):
            if nx in range(len(data)) and ny in range(len(data[x])):
                adj.append(data[nx][ny])
    return adj


def part_1():
    pass


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    # print(part_2())
