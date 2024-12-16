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


def checkPushBoxes(loc, scalar, map):
    nextLoc = addTuples(loc, scalar)
    objectAtNextSpot = map.get(nextLoc)
    # moving on x axis easy case
    if scalar[1] == 0:
        if objectAtNextSpot == '.':
            return True
        elif objectAtNextSpot == '#':
            return False
        elif objectAtNextSpot == '[' or objectAtNextSpot == ']':
            return checkPushBoxes(nextLoc, scalar, map)
    # Moving on y axis
    else:
        if objectAtNextSpot == '.':
            return True
        elif objectAtNextSpot == '#':
            return False
        elif objectAtNextSpot == '[':
            nextToNextLoc = addTuples(nextLoc, (1, 0))
            return (checkPushBoxes(nextLoc, scalar, map) and
                    checkPushBoxes(nextToNextLoc, scalar, map))
        elif objectAtNextSpot == ']':
            nextToNextLoc = addTuples(nextLoc, (-1, 0))
            return (checkPushBoxes(nextLoc, scalar, map) and
                    checkPushBoxes(nextToNextLoc, scalar, map))


def pushBoxes(loc, scalar, map):
    if map[loc] == '.':
        return
    nextLoc = addTuples(loc, scalar)
    objectAtNextSpot = map.get(nextLoc)
    # moving on x axis easy case
    if scalar[1] == 0:
        if objectAtNextSpot == '.':
            map[nextLoc] = map[loc]
            map[loc] == '.'
        elif objectAtNextSpot == '[' or objectAtNextSpot == ']':
            pushBoxes(nextLoc, scalar, map)
            map[nextLoc] = map[loc]
            map[loc] == '.'
    # Moving on y axis
    else:
        adjScalar = (1, 0) if map[loc] == '[' else (-1, 0)
        adjLoc = addTuples(loc, adjScalar)
        nextAdjLoc = addTuples(adjLoc, scalar)
        objectAtNextAdjacentSpot = map[nextAdjLoc]
        if objectAtNextSpot == '.' and objectAtNextAdjacentSpot == '.':
            map[nextLoc] = map[loc]
            map[nextAdjLoc] = map[adjLoc]
            map[loc] = '.'
            map[adjLoc] = '.'
        else:
            if objectAtNextSpot != '.':
                pushBoxes(nextLoc, scalar, map)
            if objectAtNextAdjacentSpot != '.':
                pushBoxes(nextAdjLoc, scalar, map)
            map[nextLoc] = map[loc]
            map[nextAdjLoc] = map[adjLoc]
            map[loc] = '.'
            map[adjLoc] = '.'


def nextLoc(loc, scalar, map):
    nextPossibleLoc = addTuples(loc, scalar)
    objectAtNextSpot = map.get(nextPossibleLoc)
    if objectAtNextSpot == '.':
        map[loc] = '.'
        map[nextPossibleLoc] = '@'
        return nextPossibleLoc
    elif objectAtNextSpot == '[' or objectAtNextSpot == ']':
        goodToGo = checkPushBoxes(loc, scalar, map)
        if goodToGo:
            pushBoxes(nextPossibleLoc, scalar, map)
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
            loc = (2*x, y)
            map[loc] = char
            map[addTuples(loc, (1, 0))] = '.'
        elif (line != '\n' and char != '\n' and
                (char == '#' or char == 'O' or char == '.')):
            if char == 'O':
                map[(2*x, y)] = '['
                map[((2*x)+1, y)] = ']'
            else:
                map[(2*x, y)] = char
                map[((2*x)+1, y)] = char
            length = max(y+1, length)
            width = max((2*x)+2, width)
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
        if v == '[':
            score += 100*k[1] + k[0]
    return score


print(calculateMapBoxSum(map))
