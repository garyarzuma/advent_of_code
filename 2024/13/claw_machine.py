import fileinput
import re
import math

map = []
for line in fileinput.input('input'):
    map.append(line)


def findLowestTokenCost(ax, ay, bx, by, tx, ty):
    tokens = math.inf
    rangeTop = (max(tx, ty)//min(ax, ay, bx, by))+1
    for i in range(rangeTop):
        for j in range(rangeTop):
            testx = i*ax + j*bx
            testy = i*ay + j*by
            if testx == tx and ty == testy:
                tokens = min(i*3 + j, tokens)
    return tokens


res = 0

for i in range(0, len(map), 4):
    Ax, Ay = re.findall(r'\d{2}', map[i])
    Bx, By = re.findall(r'\d{2}', map[i+1])
    Tx, Ty = re.findall(r'\d{1,100}', map[i+2])
    Ax, Ay, Bx, By, Tx, Ty = int(Ax), int(
        Ay), int(Bx), int(By), int(Tx), int(Ty)
    tokenCost = findLowestTokenCost(Ax, Ay, Bx, By, Tx, Ty)
    if tokenCost != math.inf:
        res += tokenCost

print(res)
