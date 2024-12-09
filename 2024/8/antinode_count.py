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


def make_antinode(a, b):
    x_d, y_d = a[0] - b[0], a[1] - b[1]

    antinode1 = (a[0] + x_d, a[1] + y_d)
    antinode2 = (b[0] - x_d, b[1] - y_d)

    if ((0 <= antinode1[0] < size[0]) and
            (0 <= antinode1[1] < size[1])):
        seen_antinodes[antinode1] = '#'

    if ((0 <= antinode2[0] < size[0]) and
            (0 <= antinode2[1] < size[1])):
        seen_antinodes[antinode2] = '#'


def antinode_counter(points):
    while points:
        working = points.pop()

        for loc in points:
            make_antinode(working, loc)


for k, v in map.items():
    antinode_counter(v)

print(len(seen_antinodes))
