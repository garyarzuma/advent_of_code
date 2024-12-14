import fileinput
import re

map = []
for line in fileinput.input('input'):
    map.append(line)


def findLowestTokenCost(ax, ay, bx, by, tx, ty):
    # pA*ax + pB*bx = tx
    # pA*ay + pB*by = ty
    # | ax bx | = tx
    # | ay by | = ty
    #
    #
    pA = ((tx*by)-(ty*bx))/((ax*by)-(bx*ay))
    pB = ((ty*ax)-(tx*ay))/((ax*by)-(bx*ay))
    if pA > 0 and pA % 1 == 0 and pB > 0 and pB % 1 == 0:
        return (pA*3 + pB)
    else:
        return -1


res = 0

for i in range(0, len(map), 4):
    Ax, Ay = re.findall(r'\d{2}', map[i])
    Bx, By = re.findall(r'\d{2}', map[i+1])
    Tx, Ty = re.findall(r'\d{1,100}', map[i+2])
    Ax, Ay, Bx, By, Tx, Ty = int(Ax), int(
        Ay), int(Bx), int(By), int(Tx) + 10000000000000, int(Ty) + 10000000000000
    tokenCost = findLowestTokenCost(Ax, Ay, Bx, By, Tx, Ty)
    if tokenCost != -1:
        res += tokenCost

print(round(res))
