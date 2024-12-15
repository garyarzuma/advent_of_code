import fileinput

input = fileinput.input('input')

map = {}
width = 0
length = 0

for y, line in enumerate(input):
    line = line.rstrip('\n')
    width = len(line)
    for x, num in enumerate(line):
        if num == '.':
            num = -5
        map[(x, y)] = int(num)
    length = max(length, y)


def prettyPrint(map):
    for y in range(length):
        line = ''
        for x in range(width):
            line = line + str(map.get((x, y)))
        print(line)


# prettyPrint(map)
# print(map)


def move(loc, seen):
    if map.get(loc) == 9:
        if loc in seen:
            return 0
        seen.add(loc)
        return 1
    else:
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        localres = 0
        for dir in dirs:
            nLoc = (loc[0]+dir[0], loc[1]+dir[1])
            if map.get(nLoc):
                if map.get(nLoc) - 1 == map.get(loc):
                    localres += move(nLoc, seen)
        return localres


ans = 0

for k, v in map.items():
    if (v == 0):
        newSet = set()
        thisPathTotal = move(k, newSet)
        ans += thisPathTotal

print(ans)
