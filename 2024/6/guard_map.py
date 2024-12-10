import fileinput

input = fileinput.input('input')

map = []
guard_x = -1
guard_y = -1
x_seen = 0

for i, line in enumerate(input):
    if (line.find('^') > -1):
        guard_y = i
        guard_x = line.find('^')
    map.append(line.rstrip('\n'))

width = len(map[0])
length = len(map)
guard_spot = (guard_x, guard_y)

print(guard_spot)


def guard_move_scalar(x, y):
    if (x == 0):
        return [y*-1, 0]
    else:
        return [0, x]


seen = {}
x, y = (0, -1)

while ((0 <= guard_spot[0] < length) and
       (0 <= guard_spot[1] < width)):
    seen[guard_spot] = 'X'

    next_guard_spot = (guard_spot[0] + x, guard_spot[1] + y)

    if map[next_guard_spot[1]][next_guard_spot[0]] == '#':
        x, y = guard_move_scalar(x, y)

    guard_spot = (guard_spot[0] + x, guard_spot[1] + y)


print(len(seen))


# print(guard_x)
# print(guard_y)
# print(map[95][68])
# print(width)
# print(length)
