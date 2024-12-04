import fileinput

input = fileinput.input(files='input', encoding="utf-8")
found = 0
wordSearch = []
for line in input:
    wordSearch.append(line)
input.close()
input = fileinput.input(files='input', encoding="utf-8")

MYWORD = 'XMAS'


def findNextLetter(word, letter):
    print(f'getting next letter for {letter} in {word}')
    i = word.find(letter)
    if i == len(word)-1:
        print("end of word match!")
        return None
    else:
        print(f"next is {word[i+1]}")
        return word[i+1]


def checkFor(letter, oldX, oldY, xMove, yMove):
    x = oldX + xMove
    y = oldY + yMove

    print(f"checking for {letter} at {x},{y} coming from {oldX}, {oldY}")

    if (0 <= x < len(wordSearch[0]) and
        0 <= y < len(wordSearch) and
            wordSearch[y][x] == letter):
        nextLetter = findNextLetter(MYWORD, letter)
        if nextLetter:
            return checkFor(nextLetter, x, y, xMove, yMove)
        else:
            return 1
    else:
        return 0


for y, line in enumerate(input):
    for x, c in enumerate(line):
        print(f"Checking letter {c}")
        if c == MYWORD[0]:
            nextLetter = findNextLetter(MYWORD, MYWORD[0])
            found += checkFor(nextLetter, x, y, 1, 1)
            print(f'found up pos diag: {found}')
            found += checkFor(nextLetter, x, y, -1, -1)
            print(f'found down pos diag: {found}')
            found += checkFor(nextLetter, x, y, 1, -1)
            print(f'found down neg diag: {found}')
            found += checkFor(nextLetter, x, y, -1, 1)
            print(f'found down neg diag: {found}')
            found += checkFor(nextLetter, x, y, 1, 0)
            print(f'found right: {found}')
            found += checkFor(nextLetter, x, y, 0, 1)
            print(f'found down: {found}')
            found += checkFor(nextLetter, x, y, -1, 0)
            print(f'found left: {found}')
            found += checkFor(nextLetter, x, y, 0, -1)
            print(f'found up: {found}')

print(found)
