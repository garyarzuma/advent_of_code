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

for line in fileinput.input('input'):
    nums = re.findall(r"-?\d+", line)
    p = (int(nums[0]), int(nums[1]))
    v = (int(nums[2]), int(nums[3]))

    for x in range(50):
        nLoc = getNextLoc(p, v, width, length)
        p = getNextLoc(nLoc, v, width, length)

    if map.get(p):
        map[p] += 1
    else:
        map[p] = 1

quad = [0, 0, 0, 0]
for k, v in map.items():
    if 0 <= k[0] < width//2:
        if 0 <= k[1] < (length//2):
            quad[0] += v
        elif (length//2) < k[1]:
            quad[2] += v
    elif (width//2) < k[0]:
        if 0 <= k[1] < (length//2):
            quad[1] += v
        elif (length//2) < k[1]:
            quad[3] += v

# print(map)
# print(quad)
print(quad[0]*quad[1]*quad[2]*quad[3])
