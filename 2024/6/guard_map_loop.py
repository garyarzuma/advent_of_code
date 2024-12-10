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
    map.append(list(line.rstrip('\n')))


width = len(map[0])
length = len(map)
loc = (guard_x, guard_y)


def guard_move_scalar(x, y):
    if (x == 0):
        return [y*-1, 0]
    else:
        return [0, x]


seen = {}
x, y = (0, -1)

while ((0 <= loc[0] < width) and
       (0 <= loc[1] < length)):
    seen[loc] = 'X'

    # Test next spot
    nx, ny = (loc[0] + x, loc[1] + y)

    if ((0 <= ny < length) and
            (0 <= nx < width) and map[ny][nx] == '#'):
        # Hit wall, move right new x,y
        x, y = guard_move_scalar(x, y)
        loc = (loc[0] + x, loc[1] + y)
    else:
        # Good spot or out of bounds go ahead
        loc = (nx, ny)

loop = 0
hash = {}
for a, line in enumerate(map):
    for b, num in enumerate(line):
        insert = num
        if num == '^':
            insert = '.'
        elif num == '#':
            insert = 0
        hash[(b, a)] = insert
print(len(seen))


def getPlayer(x, y):
    match (x, y):
        case (0, 1):
            return 'v'
        case (1, 0):
            return '>'
        case (-1, 0):
            return '<'
        case (0, -1):
            return '^'


# Add a wall in path
for k, v in seen.items():
    loc = (guard_x, guard_y)
    x, y = (0, -1)
    cPlayer = getPlayer(x, y)
    # print(f'Trying spot {k} for obstacle')
    map2 = hash.copy()
    map2[k] = 0
    # print(map2)
    # Test for a loop
    while ((0 <= loc[0] < length) and
            (0 <= loc[1] < width)):
        # Test next spot
        nLoc = (loc[0] + x, loc[1] + y)
        cSym = map2[loc]
        nSym = map2.get(nLoc)
        map2[loc] = cPlayer
        # print(loc, nLoc, nSym, cSym)
        if nSym == 5:
            loop += 1
            loc = (-1, -1)
            # print("Success, this one loops!")
        elif nSym == 0 or nSym == 1 or nSym == 2 or nSym == 3 or nSym == 4:
            # Hit wall, turn right
            x, y = guard_move_scalar(x, y)
            cPlayer = getPlayer(x, y)
            map2[nLoc] = nSym + 1
        else:
            # Good spot or out of bounds go ahead
            loc = nLoc
    # print(map2)
print(loop)
