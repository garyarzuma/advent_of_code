import fileinput


def getMoveScalar(char):
    match char:
        case '<':
            return (-1, 0)
        case '>':
            return (1, 0)
        case '^':
            return (0, -1)
        case 'v':
            return (0, 1)


def prettyPrint(map, length, width):
    for j in range(length):
        toPrint = ''
        for i in range(width):
            toPrint += map[(i, j)]
        print(toPrint)


def addTuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def subtractTuples(tuple1, tuple2):
    return (tuple1[0] - tuple2[0], tuple1[1] - tuple2[1])


def findNextEmptySpot(loc, scalar, map):
    nextLoc = addTuples(loc, scalar)
    objectAtNextSpot = map.get(nextLoc)
    if objectAtNextSpot == '.':
        return nextLoc
    elif objectAtNextSpot == '#':
        return None
    elif objectAtNextSpot == 'O':
        return findNextEmptySpot(nextLoc, scalar, map)


def nextLoc(loc, scalar, map):
    nextPossibleLoc = addTuples(loc, scalar)
    objectAtNextSpot = map.get(nextPossibleLoc)
    if objectAtNextSpot == '.':
        map[loc] = '.'
        map[nextPossibleLoc] = '@'
        return nextPossibleLoc
    elif objectAtNextSpot == 'O':
        nextDotSpotAfterBox = findNextEmptySpot(nextPossibleLoc, scalar, map)
        if nextDotSpotAfterBox:
            # Move Boxes in between nextDotSpotAfterBox and player loc
            while (nextDotSpotAfterBox != loc):
                map[nextDotSpotAfterBox] = 'O'
                nextDotSpotAfterBox = subtractTuples(
                    nextDotSpotAfterBox, scalar)
            # Move player
            map[loc] = '.'
            map[nextPossibleLoc] = '@'
            return nextPossibleLoc
        else:
            return loc
    else:
        return loc


loc = (0, 0)
map = {}
length, width = 0, 0

for y, line in enumerate(fileinput.input('input')):
    for x, char in enumerate(line):
        if (char == '@'):
            loc = (x, y)
            map[loc] = char
        elif (line != '\n' and char != '\n' and
                (char == '#' or char == 'O' or char == '.' or char == '@')):
            map[(x, y)] = char
            length = max(y+1, length)
            width = max(x+1, width)
        # elif (line == '\n'):
            # prettyPrint(map, length, width)
        elif (char == '<' or char == '^' or char == '>' or char == 'v'):
            # print(f"\n{char}")
            moveScalar = getMoveScalar(char)
            loc = nextLoc(loc, moveScalar, map)
            # prettyPrint(map, length, width)


def calculateMapBoxSum(map):
    score = 0
    for k, v in map.items():
        if v == 'O':
            score += 100*k[1] + k[0]
    return score


print(calculateMapBoxSum(map))
