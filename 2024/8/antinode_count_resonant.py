import fileinput

input = fileinput.input('input')

map = {}
seen_antinodes = {}
size = [0, 0]

for y, line in enumerate(input):
    line = line.rstrip('\n')
    size[0] = len(line)
    size[1] = max(size[1], y+1)
    for x, node in enumerate(line):
        if node == '.':
            continue

        if map.get(node):
            map[node].append((x, y))
            continue

        map[node] = [(x, y)]


def in_bounds(loc, size=size):
    return ((0 <= loc[0] < size[0]) and
            (0 <= loc[1] < size[1]))


def make_antinode(a, b):
    x_d, y_d = a[0] - b[0], a[1] - b[1]

    num_of_scales = max((size[0] // abs(x_d)), size[1] // abs(y_d))

    scalar = 1

    antinode1s = []
    antinode2s = []

    for scalar in range(0, num_of_scales + 1):
        antinode1s.append((a[0] + (x_d * scalar), a[1] + (y_d * scalar)))
        antinode2s.append((b[0] - (x_d * scalar), b[1] - (y_d * scalar)))

    for n in antinode1s:
        if in_bounds(n):
            seen_antinodes[n] = '#'

    for n in antinode2s:
        if in_bounds(n):
            seen_antinodes[n] = '#'


def antinode_counter(points):
    while points:
        working = points.pop()

        for loc in points:
            make_antinode(working, loc)


for k, v in map.items():
    antinode_counter(v)

print(len(seen_antinodes))
