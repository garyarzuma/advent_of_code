import fileinput
import re

width = 101
length = 103


def getNextLoc(loc, v, mWidth, mLength):
    nLocX, nLocY = loc[0] + v[0], loc[1] + v[1]
    while nLocX >= width:
        nLocX -= width
    while nLocY >= length:
        nLocY -= length
    while nLocX < 0:
        nLocX += width
    while nLocY < 0:
        nLocY += length
    return (nLocX, nLocY)


map = {}
robots = []

for line in fileinput.input('input'):
    nums = re.findall(r"-?\d+", line)
    p = (int(nums[0]), int(nums[1]))
    v = (int(nums[2]), int(nums[3]))

    robots.append([p, v])


def prettyPrint(map, t):
    good = True
    mapPrint = []
    for j in range(length):
        toPrint = ''
        for i in range(width):
            if map.get((i, j)) == 2:
                good = False
            toPrint += "#" if map.get((i, j)) else ' '
        # print(toPrint)
        mapPrint.append(toPrint)
    if good:
        print(t)
        for line in mapPrint:
            print(line)


for t in range(1, 10000):
    map = {}
    for i, robot in enumerate(robots):

        nLoc = getNextLoc(robot[0], robot[1], width, length)
        robots[i] = [nLoc, robot[1]]

        if map.get(nLoc):
            map[nLoc] += 1
        else:
            map[nLoc] = 1
    prettyPrint(map, t)
