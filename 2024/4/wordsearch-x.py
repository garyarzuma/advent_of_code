import fileinput

input = fileinput.input(files='input', encoding="utf-8")
found = 0
wordSearch = []
for line in input:
    wordSearch.append(line)
input.close()
input = fileinput.input(files='input', encoding="utf-8")


def checkFor(a, b, x, y):
    if 0 <= x < len(wordSearch[0]) and 0 <= y < len(wordSearch):
        if wordSearch[y][x] == a:
            return a

        if wordSearch[y][x] == b:
            return b
    else:
        return None


for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c == 'A':
            posUp = checkFor('S', 'M', x+1, y+1)
            posDown = checkFor('M', 'S', x-1, y-1)
            negUp = checkFor('S', 'M', x-1, y+1)
            negDown = checkFor('M', 'S', x+1, y-1)

            if ((posUp and posDown and negUp and negDown) and
                    (posUp != posDown and negUp != negDown)):
                found += 1

print(found)
