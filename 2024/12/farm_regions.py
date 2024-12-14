import fileinput

map = {}

for y, line in enumerate(fileinput.input('input')):
    for x, letter in enumerate(line):
        if letter != '\n':
            map[(x, y)] = letter

#


def getPerimeter(loc, char):
    down = int(map.get((loc[0]+1, loc[1])) != char)
    up = int(map.get((loc[0]-1, loc[1])) != char)
    right = int(map.get((loc[0], loc[1]+1)) != char)
    left = int(map.get((loc[0], loc[1]-1)) != char)

    return down + up + right + left


def traverse(char, loc, map, seen):
    area, perimeter, toProcess, toRemove = 0, 0, [loc], []

    while len(toProcess) > 0:
        loc = toProcess.pop()
        if map.get(loc) == char and loc not in seen:
            toRemove.append(loc)
            seen[loc] = char
            area += 1
            perimeter += getPerimeter(loc, char)
            for nLoc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                toProcess.append((loc[0]+nLoc[0], loc[1]+nLoc[1]))
    for x in toRemove:
        map[x] = '%'
    return (area, perimeter)


score = 0
for loc in map:
    seen = {}
    if map[loc] != '%':
        area, perimeter = traverse(map[loc], loc, map, seen)
        score += area * perimeter

print(score)
