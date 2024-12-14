import fileinput

map = {}

for y, line in enumerate(fileinput.input('input')):
    for x, letter in enumerate(line):
        if letter != '\n':
            map[(x, y)] = letter


def checkCornerCount(char, loc, map):
    corners = 0
    if (char != map.get((loc[0], loc[1]+1)) and  # down
            char != map.get((loc[0]+1, loc[1]))):  # right
        corners += 1
    if (char != map.get((loc[0], loc[1]+1)) and  # down
            char != map.get((loc[0]-1, loc[1]))):  # left
        corners += 1
    if (char != map.get((loc[0], loc[1]-1)) and  # up
            char != map.get((loc[0]+1, loc[1]))):  # right
        corners += 1
    if (char != map.get((loc[0], loc[1]-1)) and  # up
            char != map.get((loc[0]-1, loc[1]))):  # left
        corners += 1
    if (char == map.get((loc[0], loc[1]-1)) and  # up
            char == map.get((loc[0]-1, loc[1])) and  # left
            char != map.get((loc[0]-1, loc[1]-1))):  # upleft
        corners += 1
    if (char == map.get((loc[0], loc[1]-1)) and  # up
            char == map.get((loc[0]+1, loc[1])) and  # right
            char != map.get((loc[0]+1, loc[1]-1))):  # upright
        corners += 1
    if (char == map.get((loc[0], loc[1]+1)) and  # down
            char == map.get((loc[0]-1, loc[1])) and  # left
            char != map.get((loc[0]-1, loc[1]+1))):  # downleft
        corners += 1
    if (char == map.get((loc[0], loc[1]+1)) and  # down
            char == map.get((loc[0]+1, loc[1])) and  # right
            char != map.get((loc[0]+1, loc[1]+1))):  # downright
        corners += 1
    return corners


def traverse(char, loc, map, seen):
    area, edges, toProcess, toRemove = 0, 0, [loc], []

    while len(toProcess) > 0:
        loc = toProcess.pop()
        if map.get(loc) == char and loc not in seen:
            toRemove.append(loc)
            seen[loc] = char
            area += 1
            for nLoc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                toProcess.append((loc[0]+nLoc[0], loc[1]+nLoc[1]))
    for loc in toRemove:
        edges += checkCornerCount(char, loc, map)
    for x in toRemove:
        map[x] = '%'
    return (area, edges)


score = 0
for loc in map:
    seen = {}
    if map[loc] != '%':
        area, edges = traverse(map[loc], loc, map, seen)
        score += area * edges

print(score)
