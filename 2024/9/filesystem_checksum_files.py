import fileinput

input = fileinput.input('input')
line = ''

for line in input:
    line = list(line)
    line.pop()


# Expand
expanded = []
id = '0'
freeBlock = False
for i, num in enumerate(line):
    if num == '0':
        freeBlock = not freeBlock
        continue
    if freeBlock:
        expanded.append(['.']*int(num))
        freeBlock = False
    else:
        expanded.append([id]*int(num))
        freeBlock = True
        id = str(int(id) + 1)
# Compress
for i in range(-1, -len(expanded)-1, -1):
    if -i > len(expanded):
        continue
    num = expanded[i].copy()
    numLen = len(num)

    if '.' in num:
        continue

    for j in range(0, len(expanded)+i):
        if (len(expanded[j]) >= numLen and
                (expanded[j] == len(expanded[j])*['.'])):

            t = expanded[j].copy()

            expanded.insert(j, num)
            if len(t) == numLen:
                expanded.pop(j+1)
                for m, d in enumerate(expanded[i]):
                    expanded[i][m] = '.'
            else:
                expanded[j+1] = t[:(len(t)-numLen)]
                for m, d in enumerate(expanded[i]):
                    expanded[i][m] = '.'
            break

# Checksum
checksum = 0
count = 0
for i, arr in enumerate(expanded):
    for j, num in enumerate(arr):
        if num == '.':
            count += 1
            continue
        checksum += count*int(num)
        count += 1

print(checksum)
